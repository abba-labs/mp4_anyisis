# 第十三轮：执行环境仍阻塞，交付最小两帧运行包

进入head：62cd6774770d7960a68ee72780c3e5352c7502d7。实现及回归提交：d99ff89a2ae2c65a25e55145b6a451d8a6da06bf。日期2026-09-29。本轮没有新增真实文字推理、识别修复或通过验收的成品。

## 1. 先报告结果，不将准备工作冒充修复

原57项处理仍已完成，约束完整锚点仍4/8，11个一级资料单元仍0完整通过。原两帧×两种识别器共4项诊断仍执行0项、待执行4项；本包只优先选择mobile两项，执行也是0、待执行2，没有通过缩小计划制造完成率。

本轮未重建上轮被拒绝的工作流、未使用其他GitHub端点绕过。没有重新跑全片、g18、g78或47处只读枚举，也没有修改生产三个模块或默认参数。

## 2. 实际执行检查

当前沙箱Python为3.13.5，未安装paddleocr、paddlex、paddlepaddle，没有Python3.11解释器。对pypi.org、files.pythonhosted.org及github.com的DNS解析返回Temporary failure in name resolution；一次公开包元数据下载也失败，未进行反复安装重试。

已连接ET Harness的只读capabilities调用返回404，明确提示隧道客户端300秒未出现。当前可发现的该连接只有health/capabilities两项只读能力，不能因为重新在线就假定它提供代码执行。这里没有索取账号或PAT，没有更改权限。

这意味着本轮没有可用、获准且具备固定依赖的OCR执行环境。GitHub正常代码回归仍可执行，但不能拿不加载OCR的回归充当两帧真实实验。

## 3. 最小实现调整

现有scripts/probe_saved_text_recognition.py新增：
- --recognizer mobile：只执行两张原图的既有mobile识别器；默认四项兼容保留，不自动改生产模型。
- --preflight：仅验证源图/原生产物哈希和Python/三个解析包版本，不导入Paddle或推理。环境不满足返回2，准确报告executed=0和pending。
- 各选中源帧的保存检测参数/识别阈值必须相同；实际返回参数（含max_side_limit）及阈值必须与基线一致。不同则保存raw JSON并报错，不能称同配置对照。
- 原生JSON必须属于已哈希manifest；异常信息进入summary。非空识别文字、标点、下划线均不改写。

新增scripts/run_text_control_bundle.py只负责本地文件manifest校验、设置已打包源码路径并调用原脚本。它不创建工作流，不安装依赖，不携带凭证。真实初始化仍可能需要上游模型下载；RUNTIME_READY只说明检查的元数据满足要求，不证明依赖都能导入、模型已就绪或识别成功。

## 4. 两帧包的实际内容及校验

交付文件：mp4_step13_two_frame_run_bundle.zip；841220字节；SHA256：ff69c1ce0d20c01c056508bc1606c7e87bb4fbfffdde434b692e04a69b813ab1。

这是选择性输入运行包，不是新的OCR结果，也不是完整57项缓存。包含frames/2920、2950两张原图、对应9个完整native文件、未经修改的原report.json，以及脚本、8条约束基线和逐文件SHA256清单。report仍登记原57项；另外55项没有打包。实际核对12个原工件成员逐字节相同。完整原工件仍是10978920126，ZIP SHA256为6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86，原包未改。

包内docs/step11_evidence.json与固定提交62cd677的对应文件逐字节一致，Git blob为409c04e32e33120ca5ed26b2f711813188f917b8；其中历史“原始OCR”表述由第十二轮纠正，本轮只使用expected_text作核对，不以它填充识别结果。

图像SHA256：
- frame_00002920.png：567bd31e2447165c93aaee349869edf4c0eb28b16d0137db70799214fb083cb7。
- frame_00002950.png：d2fe16ef0d8c919e3ed9d48cce4d9920f3e95c420a26bc5e1a28802953b86770。

在解压目录中，用已经安装固定依赖/模型的Python3.11执行：

```bash
python scripts/run_text_control_bundle.py --preflight
python scripts/run_text_control_bundle.py
```

Windows使用Python启动器时可用py -3.11替换python。输出results/mobile，拒绝覆盖现存目录；需要新尝试时传--output新目录。返回完整results/mobile，包括summary.json、raw_ocr.json和baseline_layout.json。包不含解释器、wheel或模型，不宣称开箱即用。

直接在完整缓存上运行仍支持：

```bash
python scripts/probe_saved_text_recognition.py work/full/restored/sarc --recognizer mobile --preflight
python scripts/probe_saved_text_recognition.py work/full/restored/sarc --recognizer mobile -o work/mobile_before_layout
```

在本轮沙箱实际执行包入口的预检，源文件校验通过，退出码2，status=BLOCKED_RUNTIME，planned=2、executed=0、pending=2。没有出现raw_ocr.json或新Office。

## 5. 测试与证据边界

本地Python3.13.5仅运行相关16项：8项原脚本保护加8项新测试，全部通过。新测试包含模拟识别器，验证只加载选择的mobile、返回参数漂移保留raw并报错等；模拟结果不是OCR产物。

现有adapter-tests工作流run36504291037，工件11006127883，4974字节，SHA256为951e2f4e9355d26b2b60a1d462dddc146c4ac8deb2335ad31f9948d449cc59e9，到期2026-10-29T00:41:41Z。已下载重算ZIP哈希并读取JUnit：153通过，0失败/错误/跳过。没有创建新的推理工作流。

没有进行新Word/Excel生成或渲染验收，没有新增整片或资料单元通过数。下一动作是使已有两帧实验在获准的固定运行环境真实执行，而不是继续新增候选或重复增加诊断脚本。运行环境未恢复前，再做同样一轮不能增加资料恢复进度。
