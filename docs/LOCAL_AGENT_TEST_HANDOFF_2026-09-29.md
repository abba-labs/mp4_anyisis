# mp4_anyisis：独立测试电脑接续交接（从 Git 获取）

> 更新：2026-09-29。测试环境在用户的另一台电脑，由那台电脑上的模型执行。交接文档、代码和测试报告以本仓库为入口，不依赖本次聊天附件、聊天容器、用户当前电脑的目录或聊天文件下载链接。
> 沿用本文件路径以保持旧链接有效；文件名中的 LOCAL_AGENT 指实际测试电脑上的执行者，不是 ChatGPT 所在的临时环境。
> 本次修订核对的分支头为 `fd9df1273bd0c708e2e0acbc016ced56823871e6`；提交本文件后 head 会变化，开始及推送前必须重新查询。本次仅修订交接，未新增 OCR、Office 产物或内容通过项。

## 0. 直接执行的任务

**先取得第2920、2950帧的真实 mobile GeneralOCR 结果，判断第07条下划线丢失、第08条漏行发生在识别还是版面重组阶段。**

执行链路：测试电脑拉取指定 Git 分支 → 从同一私有仓库下载已经存在的运行工件 → 校验输入 → 准备固定环境 → 实际运行两帧 → 核对源位置 → 把原生文字结果、分析和相关改动提交回同一分支。

不需要用户在聊天里传包，不需要取得另一台电脑的绝对路径，不需要创建、修改或手动触发 GitHub Actions 工作流。读取既有 Actions 工件只是在取已有数据，不是启动远程测试。

代码和文档通过 Git 获取；57项二进制缓存目前保存在已有 Actions 工件中，**不在 Git 检出目录内，不要声称一次 git pull 就包含全部缓存。** 下载方法和期限见第3节。

## 1. 当前事实和不能改变的边界

| 项目 | 当前状态 |
|---|---|
| 仓库 | `abba-labs/mp4_anyisis`，私有仓库 |
| 工作分支 | `feat/open-source-thin-pipeline-20260928` |
| PR | 草稿 #3；不修改 main、不强推、不自动合并 |
| 最近实测代码/回归 | `d99ff89a2ae2c65a25e55145b6a451d8a6da06bf`，153项代码回归通过；不是153项OCR准确率验证 |
| 已完成基线 | 110张一秒抽样画面 → 17候选+40原帧 → 57个输入完成、0待处理 |
| 内容验收 | 11个一级资料单元：0完整通过、4有已知失败、7未完成核对 |
| 完整约束锚点 | 原57项结果中4/8，不是项目完成50%或识别准确率50% |
| 待执行诊断 | 两帧×mobile/server两种识别器共4项，尚未产生真实结果；先执行mobile两项 |
| 历史阻塞 | 聊天工具的新工作流创建被拦截，聊天容器缺固定依赖；不能把这些当成测试电脑的运行状况 |

保持三个逻辑模块、一条本地流水线、一个默认 PP-StructureV3 后端。GeneralOCR 只是同一生态的隔离诊断，不是增加生产后端。复用成熟开源能力，不自造OCR、表格求解器、配准算法或插件平台。

不改原文、标点、下划线、编号、单元格、验收真值和缓存指纹；不清空成功缓存；不修改start或抽样参数冒充续跑。旧 `TASKS.md`、`REFACTOR_PLAN.md` 是历史大框架方案，不按其重新开发。

## 2. 测试电脑从 Git 接手

### 2.1 获取工作分支

没有检出目录时，在测试电脑使用已有授权认证克隆；目录由测试电脑自行选择：

```bash
git clone --branch feat/open-source-thin-pipeline-20260928 --single-branch https://github.com/abba-labs/mp4_anyisis.git
cd mp4_anyisis
```

已有仓库时先检查，不覆盖用户改动：

```bash
git status --short
git remote -v
git branch --show-current
git fetch origin
git ls-remote origin refs/heads/feat/open-source-thin-pipeline-20260928
gh pr view 3 --repo abba-labs/mp4_anyisis --json headRefName,headRefOid,baseRefName,isDraft,state
```

仅在工作区干净、分支关系确认后切换并快进：

```bash
git switch feat/open-source-thin-pipeline-20260928
git pull --ff-only origin feat/open-source-thin-pipeline-20260928
git rev-parse HEAD
```

本地尚无该跟踪分支时，使用 `git switch --track origin/feat/open-source-thin-pipeline-20260928`。遇到未提交修改、分叉或并发更新，先保留并审查，不自动reset、clean、stash或强推。可选择新的独立检出目录，禁止覆盖原工作区。没有授权认证时记录阻塞；认证只通过测试电脑的正常授权流程，不在日志或聊天里索要、粘贴PAT。

### 2.2 只读必要入口

按顺序读：

1. 根 `NEXT_CHAT_HANDOFF.md` 和本文。
2. `scripts/probe_saved_text_recognition.py`：实际参数、预检和结果保存契约。
3. `docs/step12_ocr_provenance_2026-09-29.md`：最终overall_ocr_res并非首次OCR快照的归因纠正。
4. `docs/step11_evidence.json` 中 `limit_clauses.records`：8条独立源原文，只用于核对。
5. 需要修复时再读 `src/mp4_analysis/thin/parser.py`、`output.py` 及固定版本上游源码。

**不要调用 `scripts/run_text_control_bundle.py` 作为本流程入口。** 它要求聊天选择性包的目录结构及bundle_manifest；Git检出不包含那个包。本流程直接用仓库的 `probe_saved_text_recognition.py` 和既有完整工件。

## 3. 测试输入全部从 GitHub 获取，不依赖聊天附件

### 3.1 唯一应恢复的完整基线

| 字段 | 值 |
|---|---|
| Run ID | `36439891744` |
| Artifact ID | `10978920126` |
| 工件名 | `full-recording-resumed-validation` |
| 原ZIP字节数 | `103046931` |
| 原ZIP SHA256 | `6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86` |
| 记录的保留期限 | `2026-10-28T15:06:46Z`；下载前实时检查 |
| 解压后的输出根 | `restored/sarc` |
| 正确摘要 | `restored/resume_summary.json`、`restored/sarc/report.json` |
| 不可误用的旧摘要 | `restored/summary.json`，这是31/26历史状态 |

工件页面：https://github.com/abba-labs/mp4_anyisis/actions/runs/36439891744

优先复用测试电脑已经有的同一工件，核对来源和哈希，不重复下载。没有时，在仓库根执行以下只读命令。目标目录必须是新目录：

```bash
gh auth status
gh api repos/abba-labs/mp4_anyisis/actions/runs/36439891744/artifacts --jq '.artifacts[] | select(.id == 10978920126) | {id,name,expired,expires_at,digest,size_in_bytes}'
gh run download 36439891744 --repo abba-labs/mp4_anyisis --name full-recording-resumed-validation --dir work/test_machine_baseline
```

`gh run download` 直接解压文件，并不保存原ZIP，所以不能声称执行该命令就验证了原ZIP SHA256。核对工件ID/名称/是否过期后，必须继续执行下述两帧哈希和脚本预检；若另行取得原始ZIP，才核对上表ZIP哈希。不要通过Windows文本重定向处理二进制ZIP。

GitHub CLI不可用时，可从上述已有运行页面下载同名工件并计算ZIP SHA256，再解压至相同相对路径；无需启动任何工作流。认证失败、工件过期或缺失必须明确报告，不能用旧31/26工件、重新抽帧或重新推理冒充同一缓存。

校验以下文件存在：

```text
work/test_machine_baseline/environment.txt
work/test_machine_baseline/restored/resume_summary.json
work/test_machine_baseline/restored/sarc/report.json
work/test_machine_baseline/restored/sarc/frames/frame_00002920.png
work/test_machine_baseline/restored/sarc/frames/frame_00002950.png
work/test_machine_baseline/restored/sarc/native/frame_00002920/adapter.json
work/test_machine_baseline/restored/sarc/native/frame_00002950/adapter.json
```

两帧PNG独立校验值：

| 帧 | SHA256 |
|---|---|
| 2920 | `567bd31e2447165c93aaee349869edf4c0eb28b16d0137db70799214fb083cb7` |
| 2950 | `d2fe16ef0d8c919e3ed9d48cce4d9920f3e95c420a26bc5e1a28802953b86770` |

原SARC视频SHA256为 `e4f131ad8a2393ca5b6eade841bbce55a2e3ea105c1023954a746a8524d7e09a`。原解析指纹为 `878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb`。五份原MP4已在仓库 `MP4/`，本次两帧实验不解码视频、不重建57项计划，不再次向用户索要视频。

### 3.2 原Linux依赖清单也从工件取得

原清单是下载目录根的 `environment.txt`，不在聊天附件中取。Linux/Python3.11环境可用它生成约束，保留原文件不改。下面是可直接执行的Python语句，解释器换成测试电脑选择的Python3.11：

```python
from pathlib import Path
root = Path('work/test_machine_baseline')
lines = (root / 'environment.txt').read_text(encoding='utf-8-sig').splitlines()
constraints = [s for s in lines if s and not s.startswith(('-e ', 'mp4-analysis'))]
out = root / 'constraints_linux_py311.txt'
if out.exists():
    raise FileExistsError('已有约束文件；先核对，不覆盖')
out.write_text('\n'.join(constraints) + '\n', encoding='utf-8')
```

该约束来自原Linux环境，不保证可直接安装在Windows。Windows固定核心版本并记录其余差异，不修改历史清单，也不因某个包下载失败就全部升级。

## 4. 测试电脑的固定环境

优先复用测试电脑已经存在的合格Python3.11环境；没有时在独立虚拟环境安装，不改系统Python、不擅自安装WSL或修改安全设置。

| 组件 | 固定要求 |
|---|---|
| Python | 3.11；原补丁版本3.11.16，实际版本/路径/架构须记录 |
| PaddleOCR / PaddleX / PaddlePaddle | 3.7.0 / 3.7.2 / 3.2.2 |
| OpenCV | opencv-contrib-python 4.10.0.84，导入版本4.10.0 |
| PyAV | 16.0.1；两帧不解码视频，完整回归会使用 |
| python-docx | 1.2.0 |
| Pandoc | 3.1.11.1；Word阶段需要，不阻塞首次OCR |

所有后续命令从Git仓库根执行，`PY`或`$PY`指向已选解释器。首次建环境可使用：

Linux/WSL：

```bash
python3.11 -m venv .venv-test
PY="$PWD/.venv-test/bin/python"
"$PY" -m pip install -c work/test_machine_baseline/constraints_linux_py311.txt -e '.[parser,dev]' 'python-docx==1.2.0'
"$PY" -m pip check
```

Windows PowerShell（无须激活脚本或修改ExecutionPolicy）：

```powershell
py -3.11 -m venv .venv-test
$PY = (Resolve-Path '.venv-test\Scripts\python.exe').Path
& $PY -m pip install -e '.[parser,dev]' 'python-docx==1.2.0'
if ($LASTEXITCODE -ne 0) { throw '依赖安装失败，保留日志后定位' }
& $PY -m pip check
if ($LASTEXITCODE -ne 0) { throw '依赖冲突，先定位具体包' }
```

上述新环境目录已存在时先检查，不覆盖。如果复用现成环境，依赖合格后只需 `python -m pip install --no-deps -e .` 注册本仓库；python替换成选定的解释器。记录OS、架构、`sys.executable`、Python补丁版本、pip freeze及pip check。原环境是Linux；Windows成功不能冒充同Linux环境复现。

复用已有官方模型缓存；缺少权重时通过测试机获准网络下载公开模型。不把私有帧上传到云端OCR，不关闭TLS验证，不改网络安全控制。保留环境安装、模型初始化、推理耗时，不能混成一次首跑加速比。

## 5. 立即执行mobile两帧，不先跑全量测试

两平台都应保留stdout、stderr、退出码；每次使用新的输出目录。以下相对路径统一为Git仓库根。

### Linux/WSL

```bash
SOURCE="$PWD/work/test_machine_baseline/restored/sarc"
RUN="$PWD/work/test_machine_mobile_01"
test ! -e "$RUN" || { echo '结果目录已存在；请选新目录'; exit 1; }
mkdir -p "$RUN/logs"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONUNBUFFERED=1
export PADDLE_PDX_MODEL_SOURCE=HF
"$PY" -m pip freeze > "$RUN/logs/environment.txt"
"$PY" scripts/probe_saved_text_recognition.py "$SOURCE" --recognizer mobile --preflight > "$RUN/logs/preflight.json" 2> "$RUN/logs/preflight.stderr.log"
PRECHECK_RC=$?
printf '%s\n' "$PRECHECK_RC" > "$RUN/logs/preflight.exitcode.txt"
cat "$RUN/logs/preflight.json"
test "$PRECHECK_RC" -eq 0 || { echo '预检失败，先处理实际阻塞'; exit "$PRECHECK_RC"; }
if "$PY" -u scripts/probe_saved_text_recognition.py "$SOURCE" --recognizer mobile --evidence docs/step11_evidence.json -o "$RUN/results/mobile" > "$RUN/logs/mobile.log" 2>&1; then
  RC=0
else
  RC=$?
fi
printf '%s\n' "$RC" > "$RUN/logs/mobile.exitcode.txt"
tail -n 60 "$RUN/logs/mobile.log"
test "$RC" -eq 0 || { echo '实际运行失败，保留全部结果和日志'; exit "$RC"; }
```

### Windows PowerShell

```powershell
$SOURCE = (Resolve-Path 'work/test_machine_baseline/restored/sarc').Path
$RUN = Join-Path (Get-Location) 'work/test_machine_mobile_01'
if (Test-Path $RUN) { throw '结果目录已存在；请选新目录' }
New-Item -ItemType Directory -Path "$RUN/logs" -Force | Out-Null
$env:OMP_NUM_THREADS = '1'
$env:OPENBLAS_NUM_THREADS = '1'
$env:PYTHONUNBUFFERED = '1'
$env:PADDLE_PDX_MODEL_SOURCE = 'HF'
& $PY -m pip freeze | Out-File "$RUN/logs/environment.txt" -Encoding utf8
& $PY scripts/probe_saved_text_recognition.py $SOURCE --recognizer mobile --preflight 2> "$RUN/logs/preflight.stderr.log" | Out-File "$RUN/logs/preflight.json" -Encoding utf8
$preRC = $LASTEXITCODE
Set-Content "$RUN/logs/preflight.exitcode.txt" $preRC
Get-Content "$RUN/logs/preflight.json"
if ($preRC -ne 0) { throw "预检失败：$preRC" }
& $PY -u scripts/probe_saved_text_recognition.py $SOURCE --recognizer mobile --evidence docs/step11_evidence.json -o "$RUN/results/mobile" 2>&1 | Tee-Object -FilePath "$RUN/logs/mobile.log"
$rc = $LASTEXITCODE
Set-Content "$RUN/logs/mobile.exitcode.txt" $rc
if ($rc -ne 0) { throw "实际运行失败：$rc；保留结果和日志" }
```

`--preflight`只核对选中输入和安装版本元数据，不导入Paddle、不下载模型、不推理。RUNTIME_READY不是模型加载成功。必须实际运行不带preflight的第二条命令。

应得到两份 `raw_ocr.json`，目录分别为 `frame_00002920_mobile`、`frame_00002950_mobile`，每份带 `input.png`、`baseline_layout.json` 和 `observed_text.txt`。检查summary的planned=2、cases两项且ID唯一、pending=0、error=null、native_files_unchanged=true，再核对退出码和返回参数；这仅代表诊断有效完成，不代表条款通过。

返回检测参数必须为limit_side_len=736、limit_type=min、thresh=0.3、max_side_limit=4000、box_thresh=0.6、unclip_ratio=1.5，text_rec_score_thresh=0.0；CPU2线程、MKLDNN，mobile检测及识别，关闭方向分类/展平/文字行方向。任何参数漂移保留raw并报错，不删除校验制造同配置复现。

原研究计划mobile两项与server两项分开记账。若只成功一帧，下次用 `--frame` 选未成功帧并换新输出目录；不重跑成功项，不修改原抽样计划。中断保留日志与summary，硬终止后按文件和记录核实实际状态，不推定成功。

## 6. 如何定位与验收

关键事实：PP-Structure最终 `overall_ocr_res` 经standardized_data修改，不是首次OCR。独立GeneralOCR的raw输出应与源位置和最终结果对照，但不能仅凭两次运行差异宣称已捕获旧调用的具体清空分支。[S3][S4]

| 条款 | 重点核对 |
|---|---|
| LIMIT.05 | 2920对应完整原文与标点；历史2891不同帧结果不能混入本次基线 |
| LIMIT.06 | 找到准确源框和文字差异，区分识别污染和后续重组 |
| LIMIT.07 | 两处vc_en的下划线，在真实raw中是否已经丢失 |
| LIMIT.08 | 2950源首行约[197,146,1082,169]在raw中是否存在；后半句、下划线和编号是否正确 |

按源位置而非相同列表索引匹配前后行；保留原文、raw文字、最终文字、框、分数、输出路径。01—08全部核对，只忽略排版空白，保留标点、大小写、下划线。08跨画面，单帧未显示的部分不能记成该帧漏识别，手工拼原句不能冒充某次模型完整输出。

- raw正确而最终丢失：先捕获同一次局部PP-Structure调用的重组前后快照和相关分支，不先换模型。
- raw错误：先查检测框是否完整；确需对照时只换同生态server识别器，保留同mobile检测器和其余参数。
- 检测框缺失/截断：定位检测或输入层，不靠换recognizer掩盖。
- 环境/参数不符：先纠正实验有效性，不宣布内容修复。

需要server时从仓库根直接执行：

```bash
"$PY" scripts/probe_saved_text_recognition.py "$SOURCE" --recognizer server --evidence docs/step11_evidence.json -o "$RUN/results/server"
```

Windows使用同一参数与 `& $PY`，保留日志/退出码。没有假设和证据，不为了凑满4项盲跑server。

真实改善后才最小接入，回归完整8条及Word。GeneralOCR JSON不是NativeParser完整缓存，不能伪造adapter喂给Word适配器。Word需通过真实匹配契约的结果导出，核对内容、编号、顺序、分页及可见性，原Word/Excel不覆盖。整节PASS还需覆盖与去重说明、无遗漏/多余录屏文字，不能由8个子串命中推导整节通过。

固定源码版本PaddleX v3.7.2、PaddleOCR v3.7.0；不全局改site-packages，不自造重组平台。不要重复g18检测、g78实验、47处静态审计、MemoryMap候选盲换、旧31/26恢复或全片重跑。

## 7. 测试报告和原生结果提交回 Git

**不以“把ZIP传回聊天”作为下一轮的必要步骤。** 测试完成后，其他电脑及后续执行者应从本仓库读取实际结果。

在同一工作分支新建唯一运行目录，例 `docs/test_runs/2026-09-29_<时间>_<机器代号>/`（不要使用敏感主机名）：

```text
docs/test_runs/<RUN_ID>/
  TEST_REPORT.md
  run_metadata.json
  SHA256SUMS.txt
  logs/                    # 脱敏后的环境、预检、运行日志和退出码
  results/mobile/
    summary.json
    frame_00002920_mobile/raw_ocr.json
    frame_00002920_mobile/observed_text.txt
    frame_00002950_mobile/raw_ocr.json
    frame_00002950_mobile/observed_text.txt
  results/server/          # 仅实际执行时存在
  comparisons/             # 源帧/坐标、前后文本与逐条结论
  trace/                   # 仅实际捕获时存在
```

本次两帧的必要JSON/TXT/Markdown经检查确认大小合理、没有凭证后提交到同一私有分支，保留原始识别文字，不润色。报告引用原图的工件ID、相对路径、SHA256；不必把完整103MB缓存或原MP4再次提交。记录实际OS/Python绝对路径等运行信息前，检查路径中是否包含需要脱敏的个人信息。

完整机器侧结果目录继续保留input.png、baseline_layout.json和全部部分失败结果。后续Office/渲染等大二进制如未进入Git，应放到用户已经批准的持久存储并在报告记录稳定位置、哈希、保留期及访问要求；没有这种位置就明确“二进制仍在测试电脑，尚未集中归档”，不虚构工件ID。不私自开公开链接或上传到其他服务，不为存储结果新建工作流。

TEST_REPORT.md必须回答：实际进入head及远端校验；环境差异；命令/时间/退出码；mobile和server各自计划、尝试、有效成功、失败、未处理；LIMIT.01—08逐条源位置与结论；07/08前后证据；是否捕获真实重组轨迹；实现改动；缓存不变性检查范围；Office实际执行范围；仍未完成和下一唯一动作。

更新根 `NEXT_CHAT_HANDOFF.md` 链接该报告，明确原57项基线是否不变、新增实际推理和内容通过数。代码和相关回归提交原目录，推送前重新fetch并检查远端并发更新，只暂存本轮文件，不使用git add .，不强推、不改main、不合并PR。

提交测试/源码可能匹配现有CI触发条件，先查看工作流paths，不为上传报告触发无关全片OCR。本文不要求创建、修改或手动启动任何工作流。不能把新代码测试数量写成资料通过数。

## 8. 执行节奏与来源

先把两帧真实跑起来再做相关诊断。每轮20分钟内报告实际完成、失败和未完成；环境阻塞就记录准确错误，不再靠新增准备脚本或报告数量冒充恢复进展。

[S1] 本次修订前仓库入口与旧附件式交接永久保留：
https://github.com/abba-labs/mp4_anyisis/blob/fd9df1273bd0c708e2e0acbc016ced56823871e6/NEXT_CHAT_HANDOFF.md
https://github.com/abba-labs/mp4_anyisis/blob/fd9df1273bd0c708e2e0acbc016ced56823871e6/docs/LOCAL_AGENT_TEST_HANDOFF_2026-09-29.md

[S2] 当前分支脚本与依赖：`scripts/probe_saved_text_recognition.py`、`pyproject.toml`；先核对实际Git head，不用聊天中旧源码覆盖。

[S3] 源真值与归因边界：`docs/step11_evidence.json`、`docs/step12_ocr_provenance_2026-09-29.md`、`docs/step13_evidence.json`。

[S4] 固定上游：
https://github.com/PaddlePaddle/PaddleX/blob/v3.7.2/paddlex/inference/pipelines/layout_parsing/pipeline_v2.py
https://github.com/PaddlePaddle/PaddleX/blob/v3.7.2/paddlex/inference/pipelines/layout_parsing/utils.py
https://github.com/PaddlePaddle/PaddleOCR/blob/v3.7.0/paddleocr/_pipelines/ocr.py

[S5] GitHub CLI与Python3.11命令参考：
https://cli.github.com/manual/gh_run_download
https://cli.github.com/manual/gh_pr_view
https://docs.python.org/3.11/library/venv.html

本文是测试电脑的执行要求，不是已完成测试报告。此次只更新Git交接，未执行新增OCR，不改变历史验收统计。
