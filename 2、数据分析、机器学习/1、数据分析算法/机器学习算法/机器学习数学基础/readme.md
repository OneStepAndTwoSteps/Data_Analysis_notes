# `机器学习数学基础`

## `一、微积分：`

### `1.1、泰勒公式推导：`


* 通过极限推导泰勒公式：https://zhuanlan.zhihu.com/p/89717331

* 泰勒公式和 hessian 矩阵：https://www.zhongxiaoping.cn/2019/02/26/%E6%B3%B0%E5%8B%92%E5%85%AC%E5%BC%8F%E4%B8%8EHessian%E7%9F%A9%E9%98%B5/


### `1.2、梯度：`



* `1.2.1、梯度和梯度的推导：`https://www.zhihu.com/question/36301367/answer/688053762



* `1.2.2、形象理解“梯度”与“法向量”的关系：`https://zhuanlan.zhihu.com/p/62718992


    <div align=center><img  height=100 src="./static/梯度1.jpg"/></div>


    在大地平面上有一个小山包z=f(x, y)，你站在山包的山脚处，往上山最陡的方向走。
    你走的这一瞬间的方向向量，是相切于这座山包的，这个向量在地平面上的投影是梯度向量(z偏x, z偏y)；同时，这个投影向量是垂直于山包与地平面相交的二维山脚线的，也就是该二维曲线f(x, y)=0的法向量。


* `1.2.3、梯度和法向量：`https://blog.csdn.net/Queen0911/article/details/100611797



#### `1.2.4、导数、偏导数、方向导数、梯度：`

* 如何直观形象地理解方向导数与梯度以及它们之间的关系？：https://www.zhihu.com/question/36301367/answer/142096153







### `1.3、函数间隔和几何间隔`


* 函数间隔和几何间隔：

    <div align=center><img  height="550"  src="./static/函数间隔和几何间隔.jpg"/></div>

* 关于SVM数学细节逻辑的个人理解（一） ：得到最大间隔分类器的基本形式：https://www.cnblogs.com/xxrxxr/p/7535587.html




### `1.4、矩阵求导：`

* https://www.cnblogs.com/pinard/p/10773942.html

* https://fei-wang.github.io/matrix.html



* 标量对向量求导：https://www.cnblogs.com/yanghh/p/13756471.html

### `1.5、求偏导：`

* 求偏导

    <div align=center><img  height="250" src="./static/偏导公式.jpg"/></div>

    <div align=center><img height="250" src="./static/求偏导1-1.png"/></div>
    <div align=center><img height="400" src="./static/求偏导1.jpg"/></div>


    <div align=center><img height="400"  src="./static/求偏导2.jpg"/></div>



## `二、统计：`


### `概率分布和概率密度函数：`

* `如何简单理解概率分布函数和概率密度函数？：`https://blog.csdn.net/anshuai_aw1/article/details/82626468

* `概率密度函数：`https://zh.wikipedia.org/wiki/%E6%A9%9F%E7%8E%87%E5%AF%86%E5%BA%A6%E5%87%BD%E6%95%B8


### `期望：`


#### `期望和积分：`

* 概率统计中期望就是积分，拿 EM算法 举例，表示方式可以：

    <div align=center><img  height="230"  src="./static/期望的性质.jpg"/></div>


    <div align=center><img src="./static/期望和积分.jpg"/></div>


    `积分` 转换 `期望` 的时候，需要将其中的 `某个乘子` 作为概率分布，因此用了这种巧妙转换把 `q(Φ)` 拿出来，然后转换为他的 `期望` 。


### `平均值和期望：`

<div align=center><img  height="230"  src="./static/平均数和期望.jpg"/></div>

* 如果我们能进行无穷次随机实验并计算出其样本的平均数的话，那么这个平均数其实就是期望。当然实际上根本不可能进行无穷次实验，但是实验样本的平均数会随着实验样本的增多越来越接近期望，就像频率随着实验样本的增多会越来越接近概率一样。

    如果说 `概率` 是 `频率` 随样本趋于`无穷`的`极限`

    那么 `期望` 就是 `平均数` 随样本趋于`无穷`的`极限`




### `经验风险、期望风险、结构风险`

* `经验风险、期望风险、结构风险：`https://www.jianshu.com/p/903e35e1c95a



## `三、线性代数：`

### 3.1、基础知识：

* 编程学习线性代数：https://zihengcat.github.io/2018/03/27/%E7%BC%96%E7%A8%8B%E5%AD%A6%E4%B9%A0%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B003-%E5%90%91%E9%87%8F%E9%95%BF%E5%BA%A6%E4%B8%8E%E5%8D%95%E4%BD%8D%E5%90%91%E9%87%8F/


* 编程学习线性代数：https://zihengcat.github.io/2018/03/28/%E7%BC%96%E7%A8%8B%E5%AD%A6%E4%B9%A0%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B004-%E5%90%91%E9%87%8F%E6%95%B0%E9%87%8F%E7%A7%AF%E4%B8%8E%E5%A4%B9%E8%A7%92/


### 3.2、格拉姆矩阵（Gram matrix）详细解读


格拉姆矩阵（Gram matrix）详细解读：https://www.cnblogs.com/yifanrensheng/p/12862174.html