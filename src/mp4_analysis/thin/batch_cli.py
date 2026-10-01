"""Sequential screenshot processing; failed execution is not a document delivery."""
from __future__ import annotations

import argparse
import html
import importlib.metadata
import importlib.util
import json
import re
import shutil
import signal
import sys
import time
import uuid
from pathlib import Path
from urllib.parse import quote

from .pipeline import ScreenshotRunError, run
from .screenshots import _read_json, prepare_screenshots
from .utils import checked_directory, file_hash, json_hash, output_lock, require_disjoint, write_json


def load_plan(path):
    path = Path(path).resolve()
    plan = _read_json(path)
    if not isinstance(plan,dict) or plan.get('schema') != 1:
        raise ValueError('Expected collection plan schema=1')
    if set(plan)-{'schema','output_root','documents','ocr','export'}:
        raise ValueError('Unknown collection plan fields')
    def relative(value):
        if not isinstance(value,str) or not value.strip():
            raise ValueError('A nonempty path is required')
        candidate = Path(value)
        return checked_directory(candidate if candidate.is_absolute() else path.parent/candidate)
    root = relative(plan.get('output_root'))
    require_disjoint(path,root)
    docs = plan.get('documents')
    if not isinstance(docs,list) or not 1 <= len(docs) <= 100:
        raise ValueError('documents must contain 1..100 document objects')
    normalized, ids = [], set()
    for entry in docs:
        if not isinstance(entry,dict) or set(entry)-{'id','source','roi_config','full_image'}:
            raise ValueError('Invalid document plan entry')
        identifier = entry.get('id','')
        if not isinstance(identifier,str) or not re.fullmatch(r'[a-z0-9][a-z0-9_-]{0,39}',identifier) or identifier in ids:
            raise ValueError('Document IDs must be unique short lowercase ASCII names')
        ids.add(identifier)
        source = relative(entry.get('source'))
        require_disjoint(source,root)
        # Invalid/unsafe paths fail globally; unavailable sources fail per group.
        full = entry.get('full_image',False)
        if type(full) is not bool or bool(entry.get('roi_config')) == full:
            raise ValueError('Each document needs roi_config OR explicit full_image=true')
        config = str(relative(entry['roi_config'])) if entry.get('roi_config') else None
        normalized.append({'id':identifier,'source':str(source),'roi_config':config,'full_image':full})
    ocr = {'device':'cpu','threads':2,'mkldnn':True,'table_mode':'default','ocr_models':'server','word':False}
    if not isinstance(plan.get('ocr',{}),dict) or not isinstance(plan.get('export',{}),dict):
        raise ValueError('ocr/export must be objects')
    ocr.update(plan.get('ocr',{}))
    if set(ocr)-{'device','threads','mkldnn','table_mode','ocr_models','word'}:
        raise ValueError('Unknown OCR options')
    if (type(ocr['threads']) is not int or ocr['threads'] < 1 or type(ocr['mkldnn']) is not bool
            or type(ocr['word']) is not bool or not isinstance(ocr['device'],str)
            or ocr['table_mode'] not in {'default','cells'} or ocr['ocr_models'] not in {'server','mobile','mixed'}):
        raise ValueError('Invalid OCR options')
    export = {'word':True,'xlsx':True,'pandoc':'pandoc','timeout':180}
    export.update(plan.get('export',{}))
    if set(export)-{'word','xlsx','pandoc','timeout'} or any(type(export[k]) is not bool for k in ('word','xlsx')):
        raise ValueError('Invalid export options')
    if not isinstance(export['pandoc'],str) or type(export['timeout']) is not int or export['timeout'] < 1:
        raise ValueError('Invalid converter or timeout')
    return {'schema':1,'plan_file':str(path),'output_root':str(root),'documents':normalized,'ocr':ocr,'export':export}


def inspect_runtime(plan):
    """Cheap prerequisite discovery, not model loading, inference or acceptance.

    Inspect THIS interpreter, not another Python on PATH. Do not install packages,
    download weights, invoke a model or read credentials. Actual imports/native
    libraries and the converter version are still checked during their use.
    """
    started = time.monotonic()
    required = ['PIL', 'numpy', 'cv2', 'paddle', 'paddlex', 'paddleocr', 'lxml']
    if plan['export']['xlsx']:
        required.extend(['openpyxl', 'premailer'])
    if plan['ocr']['word']:
        required.append('docx')
    missing = []
    for module in required:
        try:
            present = importlib.util.find_spec(module) is not None
        except (ImportError, ValueError, AttributeError):
            present = False
        if not present:
            missing.append(module)
    packages = {}
    for name in ('paddleocr', 'paddlex', 'paddlepaddle', 'paddlepaddle-gpu', 'numpy', 'Pillow'):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    issues = [f'Missing module in the selected interpreter: {name}' for name in missing]
    converter = None
    if plan['export']['word']:
        converter = shutil.which(plan['export']['pandoc'])
        if converter is None:
            issues.append('Requested Word export but Pandoc is not available to this process')
    warnings = []
    if not ((3, 10) <= sys.version_info[:2] < (3, 13)):
        warnings.append('Python is outside the repository-declared 3.10..3.12 range; this is NOT proof of OCR compatibility')
    for name, expected in (('paddleocr', '3.7.0'), ('paddlex', '3.7.2')):
        if packages[name] is not None and packages[name] != expected:
            warnings.append(f'{name}={packages[name]} differs from the pinned adapter baseline {expected}')
    return {'schema': 1, 'status': 'ENVIRONMENT_BLOCKED' if issues else 'PREREQUISITES_PRESENT',
            'interpreter': sys.executable, 'python_version': sys.version.split()[0],
            'packages': packages, 'missing_modules': missing, 'pandoc': converter,
            'issues': issues, 'warnings': warnings, 'elapsed_seconds': round(time.monotonic()-started, 4),
            'check_scope': 'module discovery and executable presence only; imports, models, DLLs and converter version not verified',
            'ocr_performed': False, 'model_initialized': False, 'accuracy_verified': False}


def _successful_inputs(report):
    """Count actual successful native-result entries, never crops or test cases."""
    return sum(bool(item.get('status') == 'PARSED_UNVERIFIED'
                    and item.get('native', {}).get('files')
                    and not item.get('native', {}).get('errors'))
               for item in report.get('items', []))


def _own_root(plan):
    root = checked_directory(plan['output_root'])
    marker = root/'.collection_project.json'
    owner = {'schema':1,'plan_file':plan['plan_file'],'kind':'screenshot_collection'}
    if marker.exists():
        if marker.is_symlink() or _read_json(marker)!=owner:
            raise ValueError('Collection output belongs to a different plan')
    elif any(p.name!='.screenshot.lock' for p in root.iterdir()):
        raise ValueError('Use an empty collection output root')
    else:
        write_json(marker,owner)
    return root


def _prepare(plan,root):
    entries = []
    for document in plan['documents']:
        row = {'id':document['id'],'status':'PREPARE_FAILED'}
        try:
            manifest = prepare_screenshots(document['source'],root/('d_'+document['id']),
                       roi_config=document['roi_config'],full_image=document['full_image'])
            row.update(status='PREPARED',batch_id=manifest['batch_id'],approval_id=manifest['approval_id'],
                       ready=manifest['ready'],failed=manifest['failed'],
                       preview=(Path(manifest['batch_directory'])/'preview.html').relative_to(root).as_posix())
        except Exception as exc:
            row['error']=f'{type(exc).__name__}: {exc}'
        entries.append(row)
    # Runtime diagnostics and durations are intentionally excluded from approval.
    prepared = {'schema':1,'plan':plan,'documents':entries,'inference_performed':False}
    prepared['approval_id']=json_hash(prepared)
    write_json(root/'collection_preparation.json',prepared)
    links = []
    for row in entries:
        href = quote(row.get('preview',''),safe='/')
        link = f'<a href="{href}">打开裁图预览</a>' if href else ''
        links.append(f'<li>{html.escape(row["id"])}: {html.escape(row["status"])} '
                     f'{link} {html.escape(str(row.get("error","")))}</li>')
    (root/'collection_preview.html').write_text('<!doctype html><meta charset="utf-8">'
        '<h1>多文档裁图预览</h1><p>检查每组全部裁图；错误组也在确认范围内。未运行OCR。</p><ul>'
        +''.join(links)+'</ul><p>--accept-plan '+prepared['approval_id']+'</p>',encoding='utf-8')
    return prepared


def _deliver(run_dir,root,options):
    """Reuse a sealed bundle or build a new one; zero OCR success is diagnostic only."""
    from .document_bundle import build_document,read_bundle
    from .document_format import local_file
    run_dir,root = checked_directory(run_dir),checked_directory(root)
    report = json.loads(local_file(run_dir,'report.json').read_text(encoding='utf-8'))
    if _successful_inputs(report) == 0:
        raise ValueError('No successful OCR inputs: automatic document delivery is disabled; retain diagnostics and fix execution first')
    root.mkdir(parents=True,exist_ok=True)
    approval_hash = file_hash(local_file(run_dir,'crop_approval.json'))
    items = []
    for item in report['items']:
        row = {k:item.get(k) for k in ('id','status','source_sha256','crop_sha256','roi','crop_size','error')}
        if item.get('native'):
            row['files']=item['native'].get('files',{})
            row['signature']=item['native'].get('signature')
            for name,digest in row['files'].items():
                local_file(run_dir,item['directory']+'/'+name,digest)
            row['adapter_sha256']=file_hash(local_file(run_dir,item['directory']+'/adapter.json'))
        if item.get('input_image'):
            crop=(run_dir/item['input_image']).resolve()
            if crop.parent!=(run_dir.parent.parent/'frames').resolve() or file_hash(crop)!=item['crop_sha256']:
                raise ValueError('Delivery input crop changed')
        items.append(row)
    implementation = {name:file_hash(Path(__file__).with_name(name))
                      for name in ('document_bundle.py','document_format.py','document_checks.py','batch_cli.py')}
    request = {'batch_id':report['batch_id'],'approval_id':report['approval_id'],'approval_sha256':approval_hash,
               'items':items,'export':options,'implementation':implementation}
    digest = json_hash(request)
    memo_path = root/('delivery_'+digest[:16]+'.json')
    if memo_path.exists():
        memo = _read_json(memo_path)
        if memo.get('request_sha256')!=digest:
            raise ValueError('Delivery identity prefix collision')
        try:
            if not re.fullmatch(r'v_[0-9a-f]{16}_[0-9a-f]{8}',memo.get('directory','')):
                raise ValueError('Invalid delivery path')
            candidate = root/memo['directory']
            document,receipt = read_bundle(candidate)
            exports = _read_json(candidate/'export_report.json')
            if receipt['bundle_id']==memo.get('bundle_id') and not exports.get('errors'):
                return {'directory':str(candidate),'bundle_id':receipt['bundle_id'],'reused':True,
                        'status':'REVIEW_REQUIRED','unresolved_count':len(document.get('unresolved',[]))}
        except (OSError,ValueError,KeyError,TypeError):
            pass
    target = root/('v_'+digest[:16]+'_'+uuid.uuid4().hex[:8])
    result = build_document(run_dir,target,**options)
    write_json(memo_path,{'request_sha256':digest,'directory':target.name,'bundle_id':result['bundle_id'],
                         'status':result['status']})
    return dict(result,reused=False)


def _publish(root,state):
    write_json(root/'collection_status.json',state)
    links=[]
    for row in state['documents']:
        refs=[]
        for key,filename in (('run_directory','index.html'),('delivery_directory','document.html')):
            if row.get(key):
                relative=(Path(row[key])/filename).relative_to(root).as_posix()
                refs.append(f'<a href="{quote(relative,safe="/")}">{html.escape(key)}</a>')
        success = row.get('successful_ocr_inputs', 0)
        links.append(f'<section><h2>{html.escape(row["id"])}</h2><p>{html.escape(row["status"])} '
                     f'{html.escape(str(row.get("error","")))}</p><p>成功OCR输入：{success}；不是内容准确率。</p>'
                     + ' · '.join(refs)+'</section>')
    runtime_issues = html.escape('; '.join(state.get('runtime', {}).get('issues', [])))
    (root/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>截图批量结果</title>'
        '<h1>截图批量结果（未验收）</h1><p>每组来源和输出独立；失败不隐藏。</p>'
        + f'<p>{runtime_issues}</p>' + ''.join(links),encoding='utf-8')


def execute(plan,*,accept_plan=None):
    begun=time.monotonic()
    root=checked_directory(plan['output_root'])
    with output_lock(root):
        _own_root(plan)
        runtime = None
        if accept_plan is not None:
            runtime = inspect_runtime(plan)
            if runtime['status'] == 'ENVIRONMENT_BLOCKED':
                # Keep historical runs; do not manufacture an all-image fallback
                # delivery when neither OCR nor the requested exporter can run.
                aid = uuid.uuid4().hex[:16]
                if (root/'collection_status.json').exists():
                    write_json(root/'attempts'/(aid+'.previous.json'), _read_json(root/'collection_status.json'))
                message = '; '.join(runtime['issues'])
                state = {'schema':1,'status':'ENVIRONMENT_BLOCKED','attempt_id':aid,
                    'runtime':runtime,'crop_approval_checked':False,
                    'documents':[{'id':d['id'],'status':'ENVIRONMENT_BLOCKED','error':message,
                                  'successful_ocr_inputs':0,'delivery_created':False} for d in plan['documents']],
                    'successful_ocr_inputs':0,'inference_performed':False,'accuracy_verified':False,
                    'elapsed_seconds':round(time.monotonic()-begun,4),
                    'timing_scope':'this failed preflight only; not screenshot OCR throughput'}
                _publish(root,state)
                write_json(root/'attempts'/(aid+'.json'),state)
                return state
        prepare_started=time.monotonic()
        prepared=_prepare(plan,root)
        preparation_seconds=time.monotonic()-prepare_started
        if accept_plan is None:
            return {'status':'CROPS_PREPARED','approval_id':prepared['approval_id'],
                    'preview':str(root/'collection_preview.html'),'documents':prepared['documents'],
                    'elapsed_seconds':round(time.monotonic()-begun,4),
                    'prepare_seconds':round(preparation_seconds,4),'inference_performed':False}
        if accept_plan!=prepared['approval_id']:
            raise ValueError('Collection inputs/settings changed; inspect the new previews and approve again')
        prior=root/'collection_status.json'
        aid=uuid.uuid4().hex[:16]
        if prior.exists():
            write_json(root/'attempts'/(aid+'.previous.json'),_read_json(prior))
        state={'schema':1,'status':'RUNNING','attempt_id':aid,'approval_id':accept_plan,
               'runtime':runtime,'crop_approval_checked':True,
               'documents':[{'id':d['id'],'status':'PENDING','successful_ocr_inputs':0,
                             'delivery_created':False} for d in plan['documents']],
               'accuracy_verified':False,
               'timing_scope':'execute entry including prerequisite discovery and preparation; excludes interpreter startup/plan parsing/final serialization',
               'prepare_seconds':round(preparation_seconds,4)}
        parser=None
        startup_error=None
        current=None
        try:
            _publish(root,state)
            for document,prep,row in zip(plan['documents'],prepared['documents'],state['documents']):
                current=row
                if prep['status']!='PREPARED':
                    row.update(status='PREPARE_FAILED',error=prep.get('error'))
                    _publish(root,state)
                    continue
                row['status']='RUNNING'
                _publish(root,state)
                start=time.monotonic()
                try:
                    if startup_error:
                        raise RuntimeError(startup_error)
                    if parser is None:
                        try:
                            from .parser import NativeParser
                            parser=NativeParser(**{k:v for k,v in plan['ocr'].items() if k!='word'})
                        except Exception as exc:
                            startup_error=f'Parser construction failed: {exc}'
                            raise
                    try:
                        report=run(document['source'],root/('d_'+document['id']),
                                   roi_config=document['roi_config'],full_image=document['full_image'],
                                   accept_crops=prep['approval_id'],parser=parser,**plan['ocr'])
                    except ScreenshotRunError as exc:
                        report=exc.report
                    row.update(run_directory=report['run_directory'],ocr_status=report['status'],
                               counts=report['counts'],cache_hits=report['cache_hits'],
                               cross_batch_cache_hits=report.get('cross_batch_cache_hits',0),
                               pipeline_elapsed_seconds=report['elapsed_seconds'],
                               pipeline_stage_timings=report.get('stage_timings',{}),
                               successful_ocr_inputs=_successful_inputs(report))
                    if getattr(parser,'engine',None) is None and report.get('inference_attempts_this_run'):
                        startup_error='Native engine failed to initialize; other groups retained for resume'
                    if row['successful_ocr_inputs'] == 0:
                        row.update(status='OCR_FAILED', error='No successful OCR inputs; automatic delivery suppressed',
                                   export_elapsed_seconds=0.0)
                    else:
                        export_start=time.monotonic()
                        try:
                            candidate=_deliver(report['run_directory'],root/'deliveries'/('d_'+document['id']),plan['export'])
                        finally:
                            row['export_elapsed_seconds']=round(time.monotonic()-export_start,4)
                        row.update(delivery_directory=candidate['directory'],delivery_reused=candidate['reused'],
                                   delivery_created=not candidate['reused'],unresolved_count=candidate['unresolved_count'])
                        row['status']='PARTIAL_FAILURE' if report['status']=='PARTIAL_FAILURE' else candidate['status']
                        if candidate.get('export_errors'):
                            row['export_errors']=candidate['export_errors']
                except Exception as exc:
                    row.update(status='FAILED',error=f'{type(exc).__name__}: {exc}')
                row['elapsed_seconds']=round(time.monotonic()-start,4)
                _publish(root,state)
        except KeyboardInterrupt:
            if current and current['status']=='RUNNING':
                current['status']='INTERRUPTED'
            raise
        finally:
            total=time.monotonic()-begun
            documents_seconds=sum(r.get('elapsed_seconds',0) for r in state['documents'])
            runtime_seconds=runtime['elapsed_seconds'] if runtime else 0.0
            state['elapsed_seconds']=round(total,4)
            state['successful_ocr_inputs']=sum(r.get('successful_ocr_inputs',0) for r in state['documents'])
            state['stage_timings']={'runtime_check_seconds':runtime_seconds,
                'initial_prepare_seconds':round(preparation_seconds,4),
                'document_execution_seconds':round(documents_seconds,4),
                'other_seconds':round(max(0,total-runtime_seconds-preparation_seconds-documents_seconds),4)}
            state['status']='REVIEW_REQUIRED' if all(r['status']=='REVIEW_REQUIRED' for r in state['documents']) else 'PARTIAL_FAILURE'
            _publish(root,state)
            write_json(root/'attempts'/(aid+'.json'),state)
        return state


def main():
    command_started=time.monotonic()
    command=argparse.ArgumentParser(description='多份截图目录：环境检查、准备、确认、连续OCR/导出、恢复')
    command.add_argument('action',choices=['doctor','prepare','run','status'])
    command.add_argument('plan',help='JSON计划；相对路径以此文件目录为基准')
    command.add_argument('--accept-plan',help='整组预览的完整approval_id')
    args=command.parse_args()
    if args.action=='run' and not args.accept_plan:
        command.error('run requires --accept-plan from the preparation preview')
    if args.action!='run' and args.accept_plan:
        command.error('--accept-plan is valid only for run')
    if hasattr(signal,'SIGTERM'):
        def terminate(*_):
            raise KeyboardInterrupt
        signal.signal(signal.SIGTERM,terminate)
    try:
        plan=load_plan(args.plan)
        if args.action=='doctor':
            result=inspect_runtime(plan)
        elif args.action=='status':
            result=_read_json(Path(plan['output_root'])/'collection_status.json')
        else:
            result=execute(plan,accept_plan=args.accept_plan)
        result['current_command_seconds']=round(time.monotonic()-command_started,4)
        result['current_command_scope']='main entry to stdout snapshot, not previous OCR time or interpreter startup'
        print(json.dumps(result,ensure_ascii=False,indent=2))
        if result['status'] in {'PARTIAL_FAILURE','ENVIRONMENT_BLOCKED'}:
            command.exit(2)
    except KeyboardInterrupt:
        command.exit(130,'已中断；保留成功缓存及状态，使用同一命令恢复。\n')
    except Exception as exc:
        command.exit(1,f'失败：{exc}\n')


if __name__=='__main__':
    main()
