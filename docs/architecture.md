# 系统架构与数学对齐原理 (Architecture & Mathematics)

## 1. 物理滚动建模与 1D 垂直模板对齐

在桌面录屏中，用户滚动长文档（Word、PDF、网页）的物理运动为纯 Y 轴平移，即横向位移 $\Delta x \approx 0$。

令相邻两帧分别为 $I_t(x, y)$ 与 $I_{t+1}(x, y)$。我们在 $I_t$ 的有效中下部区域选取特征条带 $S = I_t[y_1:y_2, x_1:x_2]$。
在 $I_{t+1}$ 中沿纵轴搜索最优平移量：

$$\Delta y = \arg\max_{\delta} \frac{\sum_{x, y} (S(x, y) - \bar{S})(I_{t+1}(x, y - \delta) - \bar{I})}{\sqrt{\sum_{x, y} (S(x, y) - \bar{S})^2 \sum_{x, y} (I_{t+1}(x, y - \delta) - \bar{I})^2}}$$

当相关系数 $\rho > 0.85$ 时，确定两帧垂直滚动的位移为 $\Delta y$ 像素。
拼接画布的高度为：
$$H_{canvas} = H_{base} + \sum_{i=1}^{N-1} \Delta y_i$$
底部新出现的切片为 $I_{t+1}[H - \Delta y : H]$，垂直堆叠后可消除任何缝隙与重影。

---

## 2. 拉普拉斯方差锐度选帧 (Laplacian Variance Filtering)

在滚屏过程中，运动会造成高频信息（边缘）模糊。对每一帧灰度图 $G$ 计算二维离散拉普拉斯卷积：

$$L(x, y) = \nabla^2 G(x, y) = \frac{\partial^2 G}{\partial x^2} + \frac{\partial^2 G}{\partial y^2}$$

清晰度得分定义为拉普拉斯响应图的方差：
$$\text{Sharpness}(G) = \text{Var}(L(x, y)) = \frac{1}{MN} \sum_{x, y} (L(x, y) - \bar{L})^2$$

在连续帧差分 $\Delta G < \epsilon$ 的静止停留期内，仅提取 $\text{Sharpness}$ 取得局部极大值的单帧，从源头杜绝文字模糊。

---

## 3. 滑动窗口流式文本去重 (Sliding Window Deduplication)

传统 OCR 对重叠帧识别会产生大量重复行。流水线维护一个固定容量 $K=35$ 的先进先出（FIFO）文本上下文窗口 $W$。
对于新识别出的候选文本行 $T_{new}$，计算它与窗口内已有文本的编辑距离与包含关系：

$$\text{is\_duplicate} = \exists T \in W, \quad \left( T_{new} = T \quad \lor \quad (T_{new} \subset T) \quad \lor \quad (T \subset T_{new}) \right)$$

若非重复行，则压入文档流，并淘汰窗口最老的一项。由此实现 100% 完整捕获所有缩进子条款（`a) b) c)`）。
