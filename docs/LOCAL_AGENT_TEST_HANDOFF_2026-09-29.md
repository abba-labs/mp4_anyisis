# mp4_anyisis：本地模型测试交接

> 日期：2026-09-29。交接对象：能够在用户本机执行命令、读取文件和操作 Git 的本地大模型。
> 本文是执行任务，不是让你再次设计方案。优先取得真实模型结果，再据证据修复；不要用新增报告、脚本数量或单元测试数量代替内容恢复。
> 本次交接只整理文档及已有输入，不代表已经完成本地 OCR。用户现已选择本地执行，不需要创建、修改或触发 GitHub Actions 工作流。

## 1. 接手后先做什么

**第一目标：使用已有第2920、2950帧，实际运行同一 mobile 模型的 GeneralOCR，保存版面重组前结果，判断第08条漏行与第07条下划线丢失发生在哪一层。**

按以下顺序推进：

1. 核对当前分支与交接，保护已有改动；本机仓库路径自行发现，不假设用户盘符。
2. 复用本机已有 Python 3.11 环境；没有合适环境时在独立目录安装固定依赖，不修改系统 Python。
3. 校验附件中的两帧输入包，执行预检，然后立即执行两帧真实 mobile OCR。
4. 对比源图、`raw_ocr.json` 和原 `baseline_layout.json`，给出逐行证据。
5. 有明确证据后才决定补捕版面重组轨迹，或运行同检测器的 server 识别器对照。不要原样重复已成功的 mobile 两项。
6. 在证据充分时做最小修复，再核对完整8条及 Word；不充分则提交明确诊断与全部原生结果，不冒充修复。
7. 返回 `LOCAL_TEST_REPORT.md` 和 `LOCAL_TEST_RESULTS.zip`，并把应归档的代码、测试、报告同步原开发分支。

**不要先花一轮重新审查框架、跑全部视频或只增加防护测试。** 小范围实验先于与本任务无关的完整回归。每轮20分钟内汇报实际结果；超出本轮范围的工作保留状态，不声称会自动后台交付。

## 2. 当前事实与开发边界

| 项目 | 本交接核实的状态 |
|---|---|
| 仓库 | `https://github.com/abba-labs/mp4_anyisis`，私有仓库 |
| 工作分支 | `feat/open-source-thin-pipeline-20260928` |
| PR | 草稿 PR #3；不改 main、不自动合并、不强推 |
| 交接时实际 head | `d8ccdfccdd7e0178c91bdd699343a3b5439388a4`；开始及推送前重新查询 |
| 最近代码/回归提交 | `d99ff89a2ae2c65a25e55145b6a451d8a6da06bf` |
| 原流程 | 110张一秒抽样画面 → 17候选+40原帧 → 57项完成、0待处理 |
| 最近代码回归 | 153通过、0跳过；包含模拟测试，不是153项OCR准确率验证 |
| 内容状态 | 11个一级单元：0完整通过、4已知失败、7未完成核对 |
| 约束锚点 | 原57项结果中完整字符串命中4/8，不是项目完成50%或识别准确率50% |
| 待执行诊断 | 原研究计划2帧×2种识别器共4项，实际尚未执行；先执行mobile两项 |
| 原有阻塞 | 聊天端创建新工作流被工具拦截；聊天沙箱缺固定依赖。本地环境是否可用需要你实际检查 |

来源：仓库根 `NEXT_CHAT_HANDOFF.md`、`docs/step13_execution_readiness_2026-09-29.md`、`docs/step13_evidence.json`，均以本交接 head 下版本为基线。

保持三个逻辑模块、一条本地流水线、单一 PP-StructureV3 默认解析后端。GeneralOCR 是同一生态的隔离诊断，不是新增生产后端。只复用成熟开源能力；不自造 OCR、表格求解器、配准算法或插件平台。

不得修改原文、单元格、标点、下划线、验收真值或缓存指纹制造通过。不得清空成功缓存，不得用修改 start、采样间隔冒充续跑。旧 `TASKS.md`、`REFACTOR_PLAN.md` 是历史方案，不照其重做框架。

## 3. 先读入口，不遍历全部历史

依次读取：

- `NEXT_CHAT_HANDOFF.md`：最新状态；若远端有更新，先解释相对本文发生了什么变化。
- `scripts/probe_saved_text_recognition.py`、`scripts/run_text_control_bundle.py`：实际参数和运行行为。
- `docs/step12_ocr_provenance_2026-09-29.md`：重要归因纠正。
- `docs/step11_evidence.json` 的 `limit_clauses.records`：8条独立源原文，保留完整标点。
- 需要修复时再读 `src/mp4_analysis/thin/parser.py`、`output.py`，以及对应固定版本上游源码。

已有仓库先运行：

```bash
git status --short
git remote -v
git branch --show-current
git fetch origin
gh pr view 3 --repo abba-labs/mp4_anyisis --json headRefName,headRefOid,baseRefName,isDraft,state
git ls-remote origin refs/heads/feat/open-source-thin-pipeline-20260928
```

仅在工作区干净、目标分支关系已确认时切换并快进：

```bash
git switch feat/open-source-thin-pipeline-20260928
git pull --ff-only origin feat/open-source-thin-pipeline-20260928
```

发现用户未提交改动时不要 reset、clean、自动 stash 或覆盖；使用独立检出目录保护原工作。没有仓库时，可通过用户已授权的本地 Git/GitHub CLI 克隆指定分支。未登录只需用户完成浏览器认证，不索要或输出 PAT。

**Git 网络或登录暂不可用，不必阻止附件输入包的第一阶段测试。** 输入包自带必要脚本；将 `remote_head_verified=false` 写入报告即可，待恢复连接后再同步代码。不要假装已核查远端。

## 4. 输入与环境：选择最快可复现路径

### 4.1 首选已有两帧输入包

交接附件中的原包为 `mp4_step13_two_frame_run_bundle.zip`：

```text
字节数：841220
SHA256：ff69c1ce0d20c01c056508bc1606c7e87bb4fbfffdde434b692e04a69b813ab1
```

将其解压到一个新目录，以下称 `BUNDLE`。解压后根目录必须直接看到 `bundle_manifest.json`、`scripts/`、`baseline/`。该包只包含两帧、9个对应 native 文件、原 report、源原文和必要脚本，**不是完整57项缓存**。原 report 仍登记57项只是保留原始证据，其他55项没有打包。

两帧 PNG 的 SHA256：

| 帧 | SHA256 |
|---|---|
| 2920 | `567bd31e2447165c93aaee349869edf4c0eb28b16d0137db70799214fb083cb7` |
| 2950 | `d2fe16ef0d8c919e3ed9d48cce4d9920f3e95c420a26bc5e1a28802953b86770` |

本次交接重新核验了原包 SHA256、23个清单文件，以及其中12个原工件成员与完整ZIP的字节一致性；没有执行 OCR。你仍应运行包内预检，确认传输后的文件未变。不得修改原包的 `bundle_manifest.json` 以接受损坏文件。

### 4.2 固定环境

优先复用已有 Linux/WSL 的 Python 3.11 环境，因为原推理环境为 GitHub Actions Linux。已有 Windows 原生固定环境也可先运行，但必须记录平台差异，不能称为相同 Linux 环境复现；不得未经授权安装 WSL、改系统设置或关闭安全控制。

| 组件 | 本轮约束 |
|---|---|
| Python | 3.11；原环境为3.11.16，实际补丁版本必须记录 |
| PaddleOCR | 3.7.0 |
| PaddleX | 3.7.2 |
| PaddlePaddle | 3.2.2，首轮 CPU |
| OpenCV | `opencv-contrib-python==4.10.0.84`，导入版本4.10.0 |
| PyAV | 16.0.1；两帧诊断不解码视频，完整回归需要 |
| python-docx | 1.2.0；Office阶段需要 |
| Pandoc | 3.1.11.1；仅可选Word重导出阶段需要，不阻塞首次OCR |

附件附带原 `environment.txt` 和过滤编辑安装行后的 `baseline_constraints_linux_py311.txt`。约束文件用于 Linux/Python3.11 复现，**不是跨平台通用安装保证**。先复用合格环境；没有时才新建虚拟环境。不要无理由升级全部包或安装多套冲突的 OpenCV 发行包。

Linux/WSL，在新虚拟环境路径执行，`PY` 使用绝对路径：

```bash
python3.11 -m venv /你的工作目录/venv_mp4_py311
PY=/你的工作目录/venv_mp4_py311/bin/python
"$PY" -m pip install -c /交接目录/baseline_constraints_linux_py311.txt \
  'paddlepaddle==3.2.2' 'paddlex==3.7.2' 'paddleocr[doc-parser]==3.7.0' \
  'opencv-contrib-python==4.10.0.84' 'av==16.0.1' 'python-docx==1.2.0' 'pytest>=8,<10'
"$PY" -m pip check
```

Windows PowerShell，直接调用虚拟环境解释器，无须修改脚本执行策略：

```powershell
py -3.11 -m venv C:\你的工作目录\venv_mp4_py311
$PY = 'C:\你的工作目录\venv_mp4_py311\Scripts\python.exe'
& $PY -m pip install 'paddlepaddle==3.2.2' 'paddlex==3.7.2' 'paddleocr[doc-parser]==3.7.0' 'opencv-contrib-python==4.10.0.84' 'av==16.0.1' 'python-docx==1.2.0' 'pytest>=8,<10'
if ($LASTEXITCODE -ne 0) { throw '依赖安装失败，保留日志，不继续假报运行' }
& $PY -m pip check
if ($LASTEXITCODE -ne 0) { throw '依赖冲突，先定位具体包' }
```

以上路径只是模板，由你替换为已发现或获准的新目录。Windows示例只固定核心版本，必须保存与原Linux依赖清单的差异；若固定包不可安装，先看具体平台/解释器/下载错误，不随意换版本冒充复现。

包入口自行加载其 `src`，不需要为了第一阶段安装整个项目。需要运行仓库测试或修复脚本时，在依赖已满足后到仓库根执行 `python -m pip install --no-deps -e .`，其中 python 必须替换成选定的解释器。

保留 `python --version`、操作系统/架构、解释器绝对路径、`pip freeze`、`pip check` 日志。优先使用已有上游模型缓存。首次缺模型允许通过获准网络下载公开权重；不要上传私有帧到云端OCR，也不要关闭TLS验证或绕过网络策略。

### 4.3 完整缓存仅在后续需要时获取

首轮两帧无需先下载全部MP4或99MiB完整工件。后续单元/Office复核需要完整缓存时再取：

```text
Run：36439891744
Artifact：10978920126
名称：full-recording-resumed-validation
ZIP字节数：103046931
ZIP SHA256：6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86
到期记录：2026-10-28T15:06:46Z，下载前实时确认
输出根：restored/sarc
```

使用已授权的 GitHub CLI，可下载并解压至新目录：

```bash
gh run download 36439891744 --repo abba-labs/mp4_anyisis \
  --name full-recording-resumed-validation --dir /你的工作目录/full_baseline
```

`gh run download` 返回解压文件，不能因此宣称已经校验上面的原ZIP哈希。取得原ZIP时再计算ZIP SHA256；解压后必须按 adapter 与输入哈希检查。不要把 `restored/summary.json` 的旧31/26状态当最新状态；应读 `restored/resume_summary.json` 和 `restored/sarc/report.json`。

五份原MP4已在仓库 `MP4/`。本轮不需要用户再次上传，也不要重建57-job计划。

## 5. 真正执行：先mobile两项

设 `BUNDLE` 为两帧包解压根，`RUN` 为独立的新结果目录。**RUN不能位于 `baseline/sarc` 内，不覆盖任何旧结果。**

### Linux/WSL

```bash
# 先设置 PY、BUNDLE、RUN 为本机绝对路径。
# RUN必须是本次新目录；不要执行rm -rf清理旧实验。
test ! -e "$RUN" || { echo '结果目录已存在，请选新目录'; exit 1; }
mkdir -p "$RUN/logs" "$RUN/results"
export PYTHONUNBUFFERED=1
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export PADDLE_PDX_MODEL_SOURCE=HF

"$PY" -m pip freeze > "$RUN/logs/environment.txt"
"$PY" "$BUNDLE/scripts/run_text_control_bundle.py" --preflight > "$RUN/logs/preflight.json" 2> "$RUN/logs/preflight.stderr.log"
PRECHECK_RC=$?
cat "$RUN/logs/preflight.json"
test "$PRECHECK_RC" -eq 0 || { echo '预检未通过；修正真实环境或输入问题后再继续'; exit "$PRECHECK_RC"; }

if "$PY" -u "$BUNDLE/scripts/run_text_control_bundle.py" --output "$RUN/results/mobile" > "$RUN/logs/mobile.log" 2>&1; then
  RC=0
else
  RC=$?
fi
printf '%s\n' "$RC" > "$RUN/logs/mobile.exitcode.txt"
tail -n 60 "$RUN/logs/mobile.log"
```

### Windows PowerShell

```powershell
# $PY、$BUNDLE、$RUN先设为本机绝对路径。
if (Test-Path $RUN) { throw '结果目录已存在，请选新目录' }
New-Item -ItemType Directory -Path "$RUN\logs", "$RUN\results" | Out-Null
$env:PYTHONUNBUFFERED = '1'
$env:OMP_NUM_THREADS = '1'
$env:OPENBLAS_NUM_THREADS = '1'
$env:PADDLE_PDX_MODEL_SOURCE = 'HF'

& $PY -m pip freeze | Out-File "$RUN\logs\environment.txt" -Encoding utf8
& $PY "$BUNDLE\scripts\run_text_control_bundle.py" --preflight 2> "$RUN\logs\preflight.stderr.log" | Out-File "$RUN\logs\preflight.json" -Encoding utf8
$precheckRC = $LASTEXITCODE
Get-Content "$RUN\logs\preflight.json"
if ($precheckRC -ne 0) { throw "预检未通过，退出码 $precheckRC" }

& $PY -u "$BUNDLE\scripts\run_text_control_bundle.py" --output "$RUN\results\mobile" 2>&1 | Tee-Object -FilePath "$RUN\logs\mobile.log"
$rc = $LASTEXITCODE
Set-Content "$RUN\logs\mobile.exitcode.txt" $rc
```

预检 `RUNTIME_READY` 只证明元数据和选中输入合格，不证明模型可加载或已经推理。实际运行失败要保存日志与任何部分结果，再按失败层修复。网络/模型初始化未发生推理，写 `NOT_RUN/BLOCKED`；有 raw 文件但参数不符，写“已执行但对照无效”，不能当成功或假装完全未运行。

不能把直接打开源图、手工抄写文字当成真实模型测试。源原文仅用于验收，绝不注入、替换或润色模型输出。

## 6. 第一阶段完成标准及必须保存的证据

成功运行应保存：

```text
RUN/
  logs/
    environment.txt
    preflight.json
    preflight.stderr.log
    mobile.log
    mobile.exitcode.txt
  results/mobile/
    summary.json
    frame_00002920_mobile/
      input.png
      baseline_layout.json
      raw_ocr.json
      observed_text.txt
    frame_00002950_mobile/
      input.png
      baseline_layout.json
      raw_ocr.json
      observed_text.txt
```

检查 `summary.json`：`planned=2`、`len(cases)=2`、`pending=0`、`error=null`、`native_files_unchanged=true`，两个case ID必须各出现一次。再核对原图SHA、运行退出码和每份raw的参数。**满足这些只代表mobile诊断执行完成，不代表条款或成品验收通过。**

固定诊断参数：

```text
text_detection_model_name = PP-OCRv5_mobile_det
text_recognition_model_name = PP-OCRv5_mobile_rec
device = cpu, cpu_threads = 2, enable_mkldnn = true
use_doc_orientation_classify = false
use_doc_unwarping = false
use_textline_orientation = false
text_det_params = {limit_side_len:736, limit_type:min, thresh:0.3,
                   max_side_limit:4000, box_thresh:0.6, unclip_ratio:1.5}
text_rec_score_thresh = 0.0
```

脚本会核对返回的检测参数和识别阈值。校验失败时保留 raw，并定位配置传递差异；不得删校验、篡改期望参数或把参数漂移算作同配置改善。

`native_files_count=9` 在最小包上是正常的，只证明该选择性副本9个native文件的前后状态；不能声称又检查了全部344个文件。完整原4项研究计划需另记mobile已完成数、server未执行/完成数，不能以2/2冒充4/4。

**中断恢复：** 优先正常中断，保留summary和已有case。若只成功了一帧，下一次用仓库现有脚本的 `--frame` 只选未成功帧、新建输出目录，不重复成功帧；不能改变原视频抽样参数。进程硬终止时summary可能不完整，必须根据原始文件和日志核实，不能自行推定通过。

## 7. 对照方法：先区分识别与版面重组

关键纠正：PP-Structure最终JSON中的 `overall_ocr_res` 会被上游 `standardized_data` 改写，**不是首次GeneralOCR快照**。本轮保存的 `raw_ocr.json` 才是这个独立GeneralOCR对照的原生输出。独立对照与历史最终结果不同，尚不能自动证明历史运行的具体清空分支；需要时捕获同一次PP-Structure调用的前后快照。[S4]

重点核对：

| 目标 | 既有证据 | 本次要回答 |
|---|---|---|
| LIMIT.05 | 当前57项无完整锚点；历史不同帧2891曾完整出现 | 2920真实raw有何文字/标点差异，污染是在何阶段进入？ |
| LIMIT.06 | 当前57项无完整锚点 | 找出源位置对应的真实输出差异，不只报告命中数 |
| LIMIT.07 | 最终结果出现 `vcen` | 重组前是否已经丢掉 `vc_en` 的下划线？两处标识符分别核对 |
| LIMIT.08 | 2950源首行框约 `[197,146,1082,169]`；最终索引6为空且保留0.99185分数 | raw中该长行是否存在、内容是什么、框与分数如何？后半句是否正确？ |

方法：按源位置/框对应行，记录原文字、raw文字、最终文字及索引/坐标；不能假定前后索引不变。核对01—08全部条款，保持编号、括号、标点、大小写、下划线，仅忽略排版空白。08在2920/2950间跨画面，不要把单帧不可见的内容算成该帧漏识别；也不要直接拼两帧字符串冒充某次模型的完整输出。

依据真实结果选择下一步：

| 实际观察 | 下一步 |
|---|---|
| raw已正确、最终结果丢失/变错 | 优先在隔离PP-Structure调用中捕获重组前/后快照与相关分支，定位组装副作用；不先换识别模型 |
| raw就漏字或丢下划线 | 先确认检测框是否覆盖源文字，再执行同检测器+server识别器的受控对照，保存原生输出 |
| 检测框缺失或截断 | 归为检测/输入问题，不能只换recognizer；有假设后一次只改一个因素 |
| 参数、模型或依赖不一致 | 先记录并修复实验有效性，不宣布内容改善 |
| 环境无法导入或模型下载失败 | 保留准确命令、stderr、退出码及阶段；不修改识别算法掩盖环境问题 |

上游源码核对版本必须固定 `PaddleX v3.7.2`、`PaddleOCR v3.7.0`。新诊断只用公开接口和必要的隔离观测；不在用户环境全局改site-packages，不自行重写重组平台。真实证据未证实之前，不将假设写成已解决根因。

### 需要server组时的正确入口

**不要给 `run_text_control_bundle.py` 追加 `--recognizer server`。** 该包装器固定插入mobile参数，追加server会连mobile一起选中，造成重复执行。

在已安装项目的仓库根，直接调用现有底层脚本，输出新目录：

```bash
"$PY" scripts/probe_saved_text_recognition.py "$BUNDLE/baseline/sarc" \
  --recognizer server --evidence docs/step11_evidence.json \
  -o "$RUN/results/server"
```

Windows使用相同参数及 `& $PY`。没有仓库/可编辑安装时先使用包内 `src` 设置对应Python搜索路径，再直接调用包内probe；不要修改原包清单绕过完整性检查。

## 8. 修复与单元验收：不能停在生成JSON

第一阶段得到真实证据后，能明确修复的只做最小改动，保留原版本和新版本结果。修复内容若不确定，交付可复核结果，不凭人工真值“修正”输出。

要把“2.4约束说明”标成通过，至少完成：8条原文和顺序逐条核对、源可见范围与跨屏关联说明、无缺条/重复/错误编号、无多余录屏文本混入，以及真实Word导出后文本和分页/可见性检查。需要明确覆盖范围；不能由8个子串命中推出所有可见内容完整。

必须复用现有Word导出适配；GeneralOCR JSON不是NativeParser完整结果，不能伪造adapter后交给 `export_saved_word.py`。需要Office验证时，在证据充分的修复后局部运行原PP-Structure链路，或使用确实匹配其输入契约的既有结果；旧Word/Excel保持原样。

仅对相关实现补回归，再执行适用现有测试。完整153项回归有固定Pandoc等依赖，依赖缺失/跳过要如实记录，不阻塞首次两帧结果。所有测试通过也不能替代内容验收。未执行的Word渲染、Excel核对及其他视频明确列为未完成。

不要再做：g18原样裁剪/检测对照、g78原样cells实验、47处空文字重扫、MemoryMap盲换后端、旧31/26续跑、全片从头处理。暂未解决的其他问题继续保留FAIL，后续按资料台账闭环，不每轮重新选题。

## 9. 回传、归档与提交

本地执行者必须交付：

```text
LOCAL_TEST_RESULTS/
  LOCAL_TEST_REPORT.md
  run_metadata.json
  SHA256SUMS.txt
  logs/                         # 环境、安装/导入、预检、运行日志与退出码
  results/mobile/               # 完整原生结果，不能只留截图
  results/server/               # 仅实际执行时存在
  comparisons/                  # 每条源位置、前后文字、坐标与差异
  trace/                        # 仅实际捕获重组轨迹时存在
  office/                       # 仅实际导出/渲染时存在
  changes.patch                 # 仅有实现改动时存在
```

把上述目录打包为 `LOCAL_TEST_RESULTS.zip`，提供ZIP的SHA256。保留失败、中断及参数漂移的原始结果，不只回传成功项。不要打包 `.venv`、模型权重、缓存全集、字体文件、密钥、PAT或带认证信息的URL。私有源资料仅回传用户授权位置；日志若含凭证，回传脱敏副本，勿公开原日志。

`LOCAL_TEST_REPORT.md` 用以下固定栏目：

```text
1. 实际进入的repo路径、分支、head；远端是否核实。
2. OS/架构/Python绝对路径与版本、核心依赖、与原Linux环境的差异。
3. 执行命令、开始/结束时间、退出码；环境安装/模型初始化/推理耗时分开。
4. mobile计划/实际尝试/成功有效/失败/待处理；server同样单列。
5. LIMIT.01—08逐条：源帧/坐标、raw观察、最终观察、差异及判定。
6. LIMIT.07下划线与LIMIT.08长行的明确证据；是否捕获实际重组轨迹。
7. 改动及验证范围、未完成项、缓存不变性检查范围（9或344，不混写）。
8. 原生结果路径、ZIP SHA256、实现/文档提交、下一唯一可执行动作。
```

代码/测试/文字报告按仓库规则提交同一工作分支，更新 `NEXT_CHAT_HANDOFF.md`，说明“原57项基线未变”和本次真实新增的结果。提交前检查 `git status` 与差异，只暂存本轮相关文件；不得 `git add .` 把视频、输入包、环境和大工件一起提交。

推送前重新查询远端head；有并发更新先审阅并协调，正常整合后再推送，不强推。不改main、不合并PR、不改仓库权限、不修改workflow。现有自动工作流的触发范围须先看，避免通过无关源码改动误触发全片OCR。

**本地试验尚未执行时，不写“已解决”“已验收”，也不提高项目完成度。** 本轮首要交付是两份有效原生OCR结果及归因；内容单元通过需额外满足第8节。

## 10. 来源与复核入口

[S1] 项目固定交接（本交接核查基线）：
https://github.com/abba-labs/mp4_anyisis/blob/d8ccdfccdd7e0178c91bdd699343a3b5439388a4/NEXT_CHAT_HANDOFF.md

[S2] 当前真实脚本及依赖：同一提交下的 `scripts/probe_saved_text_recognition.py`、`scripts/run_text_control_bundle.py`、`pyproject.toml`。

[S3] 源原文与历史边界：同一提交下 `docs/step11_evidence.json`、`docs/step12_ocr_provenance_2026-09-29.md`、`docs/step13_evidence.json`。第11轮把最终overall结果当首次OCR的说法已由第12轮纠正，不沿用旧归因。

[S4] 固定上游：
https://github.com/PaddlePaddle/PaddleX/blob/v3.7.2/paddlex/inference/pipelines/layout_parsing/pipeline_v2.py
https://github.com/PaddlePaddle/PaddleX/blob/v3.7.2/paddlex/inference/pipelines/layout_parsing/utils.py
https://github.com/PaddlePaddle/PaddleOCR/blob/v3.7.0/paddleocr/_pipelines/ocr.py

[S5] 环境与本地命令依据：
https://docs.python.org/3.11/library/venv.html
https://cli.github.com/manual/gh_pr_view
https://cli.github.com/manual/gh_run_download

本文中的执行步骤、阶段完成标准和回传结构是本次本地交接要求；历史结果以原生工件和固定提交为证，不把文档要求当已经完成的事实。
