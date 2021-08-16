# `BN - batch normalization (批归一化)`


[在 2015 年的一篇论文中](https://links.jianshu.com/go?to=https%3A%2F%2Farxiv.org%2Fabs%2F1502.03167)，Sergey Ioffe 和 Christian Szegedy 提出了一种称为批归一化（`Batch Normalization，BN`）的方法来解决梯度消失/爆炸问题。

该方法包括在每层的激活函数之前或之后在模型中添加操作。操作就是将输入平均值变为 0，方差变为 1，然后用两个新参数，一个做缩放，一个做偏移。换句话说，这个操作可以让模型学习到每层输入值的最佳缩放值和平均值。大大多数情况下，如果模型的第一层使用了 BN 层，则不用标准化训练集（比如使用 `StandardScaler` ）；BN 层做了标准化工作（虽然是近似的，每次每次只处理一个批次，但能做缩放和平移）。



## `参考：`

`Batch Normalization导读:` https://zhuanlan.zhihu.com/p/38176412

`什么是批标准化 (Batch Normalization)：` https://zhuanlan.zhihu.com/p/24810318


`Batch-Normalization深入解析：`https://hellozhaozheng.github.io/z_post/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0-Batch-Normalization%E6%B7%B1%E5%85%A5%E8%A7%A3%E6%9E%90/