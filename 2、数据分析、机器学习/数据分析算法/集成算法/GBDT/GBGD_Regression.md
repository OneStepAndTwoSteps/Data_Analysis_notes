# `GBDT Regression`

`在下面算法中我们先使用 均方误差 作为 损失函数 对算法进行举例说明`

<div align=center><img width="900" height="450" src="./static/gbdt/gbdt算法.jpg"/></div>


<div align=center><img width="900" height="500" src="./static/gbdt/gbdt算法2.jpg"/></div>

## `Input：`

* `input：training: ` set 中的 x 是特征，y 是真实值，n 是样本个数

* `loss function：`要是一个可微的损失函数，迭代次数为 M （每次迭代加一个树）



## `Algorithm：`
<br>

`1、Initialize model with a constant value:`

*   ` F0(x)：` 第一个树模型，yi 为观测值，γ 为预测值，我们想要真实值和预测值之间的差距极小化，初始化时，γ 为 所有观测值取的平均数。


`2、For m = 1 to M:`

*   `Step (A)：`

    <div align=center><img  src="./static/gbdt/GBDT算法_a计算负梯度.jpg"/></div>

    `A、`计算负梯度中因为损失函数是均方误差，所以 rim 为残差，[为什么是残差请点击这里](#补充说明)。


*   `Step (B)：`

    <div align=center><img  src="./static/gbdt/GBDT算法_b.jpg"/></div>


    `B、`对 `rmi` 拟合一颗回归树，得到第 m 棵树的叶节点区域 `Rjm`，`j = 1, 2, 3, ... , j`, 该例子和李航书上写的相反，李航书上写的 `Rmj` ，这里是 `Rjm` ，其实无所谓，这里只是提示一下。
    
    * `m：`为索引，表示地几棵树

    * `j：`为每片叶子的索引

        对于第一棵树进行二分类，则有 `Rjm` 如图：
    
        <div align=center><img  src="./static/gbdt/rmj.jpg"/></div>


*   `Step (C)：`

    <div align=center><img  src="./static/gbdt/GBDT算法_c.jpg"/></div>

    `C:` `γjm` 为预测值，我们的目标就是极小化 `γjm` ，






<br>
<br>
<br>

## `补充说明:`

`一、为什么均方误差的负梯度是残差：`

<div align=center><img  src="./static/gbdt/均方误差求负梯度.jpg"/></div>

* 因为是对 predicted 进行求导，根据链式法则，求导之后算式为：(observed - predicted)(-1)，即 (predicted - observed)，`因为是负梯度，所以最终式子为：(observed - predicted)，即残差。`

* `rim` 中：i 为第几个样本，m 为迭代的次数，那么每次迭代就是计算这n个样本的残差。



## `参考：`

* Gradient Boost Part 2 (of 4): Regression Details：https://www.youtube.com/watch?v=2xudPOBz-vs&t=737s
