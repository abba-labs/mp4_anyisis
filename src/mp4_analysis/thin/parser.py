"""One upstream PP-StructureV3 engine; native results and native exporters."""
from __future__ import annotations

import hashlib
import importlib.metadata
import json
from collections import Counter
from pathlib import Path


class NativeParser:
    def __init__(self, *, device='cpu', threads=2, config=None):
        self.options = dict(device=device, cpu_threads=threads, enable_mkldnn=False,
                            use_doc_orientation_classify=False, use_doc_unwarping=False,
                            use_textline_orientation=False, use_formula_recognition=False,
                            use_seal_recognition=False, use_chart_recognition=False,
                            markdown_ignore_labels=[])
        if config is not None:
            # Upstream YAML config, not a second model/schema maintained here.
            self.options['paddlex_config'] = str(Path(config).resolve())
        self.versions = {}
        for package in ['paddleocr', 'paddlepaddle', 'paddlex']:
            try:
                self.versions[package] = importlib.metadata.version(package)
            except importlib.metadata.PackageNotFoundError:
                self.versions[package] = 'not-installed'
        identity = {'options': self.options, 'versions': self.versions,
                    'config_sha256': hashlib.sha256(Path(config).read_bytes()).hexdigest() if config else None,
                    'adapter_schema': 1}
        self.fingerprint = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
        self.engine = None

    def parse(self, image, target, *, word=False):
        """Cache only successful, intact native output; no fuzzy text deletion."""
        from .video import file_hash
        image, target = Path(image), Path(target)
        signature = {'input_sha256': file_hash(image), 'parser': self.fingerprint, 'word': word}
        cache = target / 'adapter.json'
        if cache.is_file():
            previous = json.loads(cache.read_text(encoding='utf-8'))
            if previous.get('signature') == signature and not previous.get('errors'):
                files = previous.get('files', {})
                if files and all((target/name).is_file() and file_hash(target/name) == digest for name,digest in files.items()):
                    return dict(previous, cache_hit=True)
        target.mkdir(parents=True, exist_ok=True)
        # Stale exports must not be counted as new results after an error.
        if any(target.iterdir()):
            import shutil
            shutil.rmtree(target)
            target.mkdir()
        if self.engine is None:
            from paddleocr import PPStructureV3
            self.engine = PPStructureV3(**self.options)
        result = next(iter(self.engine.predict(str(image))))
        errors = []
        # Raw upstream JSON first: every later export is derived, not the evidence.
        result.save_to_json(save_path=str(target))
        for method in ['save_to_markdown', 'save_to_html', 'save_to_xlsx'] + (['save_to_word'] if word else []):
            try:
                getattr(result, method)(save_path=str(target))
            except Exception as exc:
                errors.append({'stage': method, 'message': str(exc)})
        payloads = sorted(target.glob('*.json'))
        if not payloads:
            raise RuntimeError('upstream did not write its native JSON result')
        raw = json.loads(payloads[0].read_text(encoding='utf-8'))
        data = raw.get('res', raw)
        blocks = data.get('parsing_res_list', [])
        labels = Counter(block.get('block_label', 'unknown') for block in blocks)
        scores = data.get('overall_ocr_res', {}).get('rec_scores', [])
        if not blocks:
            errors.append({'stage': 'parse', 'message': 'no layout blocks detected'})
        exported = {str(path.relative_to(target)):file_hash(path) for path in target.rglob('*') if path.is_file()}
        info = {'signature': signature, 'versions': self.versions,
                'block_count': len(blocks), 'labels': dict(labels),
                'low_confidence_observations': sum(float(s) < 0.85 for s in scores),
                'table_count': len(data.get('table_res_list', [])),
                'files': exported, 'errors': errors, 'cache_hit': False,
                'verified': False, 'native_json': payloads[0].name}
        cache.write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding='utf-8')
        return info
