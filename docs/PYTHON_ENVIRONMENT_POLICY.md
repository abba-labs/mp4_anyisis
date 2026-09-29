# Python环境策略：兼容范围不等于历史基线

更新：2026-09-29。用户要求放宽不必要的Python限制。本页覆盖旧交接中“只有Python3.11才能测试”的要求；历史测试使用3.11.16的事实不改写。读取本页不改变下一实际任务：复用testvm01已可用环境，继续2950同次PP-Structure轨迹、最小修复及成品检查。

## 1. 当前规则

| 场景 | 规则 |
|---|---|
| 仓库安装/日常测试 | 遵循现有pyproject.toml的 `>=3.10,<3.13`，即3.10、3.11、3.12；不锁补丁版本 |
| 保存输入的OCR探针 | 不再要求解释器minor必须为3.11；依赖和输入校验通过时，允许上述范围执行 |
| 复现历史结果 | 3.11.16是历史参考，优先复用已经可用的该环境；不是所有工作强制安装的版本 |
| 新任务选择 | 用户可把3.12作为默认，使用独立虚拟环境，不修改系统Python和其他项目环境 |
| 已能执行的本次任务 | 当前testvm01的3.11.16已跑通，不为切换版本再次安装环境或重跑成功实验 |
| Python3.13 | PaddlePaddle轮子已存在，但仓库目前仍声明 `<3.13`；本次不扩展项目范围，不伪称全依赖/全流水线已验证 |
| Python3.9 | 在本仓库声明范围之外；是否能安装Paddle不是仓库支持3.9的依据 |

“允许执行”不是“所有版本的OCR已实测通过”。不升级或降级解释器只是为了消除一个历史版本差异；先用已可用环境推进实际缺陷。

## 2. 已核查的依赖事实

PaddlePaddle官方发布的PyPI 3.2.2页面已有：

```text
paddlepaddle-3.2.2-cp312-cp312-manylinux1_x86_64.whl
paddlepaddle-3.2.2-cp313-cp313-manylinux1_x86_64.whl
```

上述Linux x86-64文件记录上传于2025-11-19。核查来源：
https://pypi.org/project/paddlepaddle/3.2.2/#files

因此“3.12/3.13有没有PaddlePaddle3.2.2轮子”已经可以从官方文件列表回答，无需先耗时安装来猜。但单包有轮子不等于PaddleOCR、PaddleX、全部可选依赖及本项目都能在该平台工作。实际新环境仍需安装、pip check、导入和小范围真实执行；本次未做3.12/3.13整套OCR实测。

仓库范围来源：pyproject.toml在本轮进入提交4f5887330fa46537f0e63e43de402e7bce37e9ce已经为 `>=3.10,<3.13`，本次没有改变安装元数据。仅修正探针比项目元数据更严格的不一致。

## 3. 对照结论如何保持可靠

Python变成3.12，不会自动让所有结论无效。关键是把比较条件说清：

- 在同一个3.12环境中，固定图像、权重、Paddle版本和参数，对比原实现与修改实现，可形成该环境下的有效对照。
- 用3.12的新结果直接比较3.11的历史结果时，版本差异是额外变量；先保留差异记录，必要时在同环境补原实现对照，不能把所有变化都归功于修复。
- 仅Python恰好等于3.11.16，也不能证明完整环境、平台、模型文件和参数完全一致。

当前故障诊断仍固定PaddleOCR3.7.0、PaddleX3.7.2、PaddlePaddle3.2.2，以及既有模型/参数。这是为了对应正在研究的上游源码，不是禁止将来开展明确的依赖兼容性实验。图片哈希、真实返回参数、源文字、标点、下划线、失败记录与成品验收标准不放宽。

## 4. 实际代码变化

`scripts/probe_saved_text_recognition.py`：

- Python准入由 `== (3,11)` 改为 `(3,10) <= version < (3,13)`。
- preflight.runtime记录 `python_requirement`、`python_supported`、`baseline_python`、`baseline_python_match` 与 `warnings`。
- 实际summary保存整个runtime记录。不同受支持Python版本给出说明，不再仅因此拒绝执行。
- `baseline_python_match`仅表示Python版本字符串相同，绝非“整个环境已一致”。
- 保持原有包版本检查、输入/输出哈希、参数漂移拒绝、独立新目录、不修改native和未验收标记。
- preflight仍不导入Paddle、不加载模型、不推理；RUNTIME_READY仍只是元数据检查通过。

无须新增命令行参数。原命令继续使用选定虚拟环境解释器；不要改用依赖聊天附件的bundle入口。正在进行的2950诊断仍复用 `.venv-test`，不为验证该环境策略重跑已经成功的两帧。

## 5. 本轮验证范围

本轮只修改环境准入及记录，无新增真实OCR、Word或资料通过项。没有修改main、模型、工作流或旧缓存。

本地相关测试：

```bash
python -m pytest -q tests/test_saved_text_recognition.py tests/test_saved_text_preflight.py tests/test_text_probe_python_policy.py
```

结果：29 passed、0 failed、0 skipped。运行宿主Python3.13.5；版本范围用模拟的解释器元数据测试，模型执行分支使用明确的FakeEngine。**这不是在3.10/3.11/3.12分别安装运行了OCR，也不是宣称项目支持在3.13安装。**

新增13项覆盖范围边界、补丁版本不锁死、声明范围一致、缺失/错误Paddle包仍被拒绝、预检不导入模型、跨Python身份进入summary。既有16项继续保护源输入、模型选择和返回参数。

本次测试提交会按既有adapter-tests.yml触发低成本代码回归；未新建、修改或手动触发工作流，不包含新的OCR实验。该CI的实际状态以GitHub运行记录为准，不提前记为通过。当前内容修复仍以REVIEW_AND_NEXT.md的2950局部任务为准。
