# 高斯混合模型


`高斯混合模型 GMM` 可以看成是多个高斯模型的混合叠加而成，每一个高斯模型对应一个权重,并且所有权重相加值为1，概率分布公式如下：

<div align=center><img width="450" height="130" src="./static/高斯混合模型公式.jpg"/></div>

*   其中 `α` 为第 `k` 个高斯分布所对应的权重。


`GMM` 是一个生成模型，它假设数据是从多个高斯分布中生成的，可以这样理解生成流程：有 K 个高斯分布，赋予每一个分布一个权重，每当生成一个数据时，就按权重的比例随机选择一个分布，然后按照该分布生成数据。

那么根据数据进行反推，可以假定一个样本有一个潜在的类别，而这个类别是无法观测到的，也就是隐变量，所以对于样本在给定参数 `θ` 的条件下边际概率为：


<div align=center><img width="450" height="60" src="./static/引出EM.jpg"/></div>

其中 `z= c_i` 表示样本属于某个类别， `p(z = c_i)` 也就是 `隐变量` 的 `概率分布`。

<div align=center><img width="450" height="130" src="./static/z.jpg"/></div>

所以就需要通过 `EM算法` 来辅助推断。


## 参考：

* 高斯混合模型（GMM）推导及实现：https://zhuanlan.zhihu.com/p/85338773

* 机器学习-白板推导系列(十一)高斯混合模型GMM（Gaussian Mixture Model）笔记：https://zhuanlan.zhihu.com/p/344689506






