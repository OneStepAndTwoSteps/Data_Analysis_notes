 # EM 期望最大算法

主要用于解决包含 `隐变量` 的混合模型的参数估计（极大似然问题）

EM 算法的核心思想非常简单，分为两步：
`Expection-Step` 和 `Maximization-Step`:

* `E-Step`: 主要通过观察数据和现有模型来估计参数，然后用这个估计的参数值来计算似然函数的期望值；

* `M-Step`: 是寻找似然函数最大化时对应的参数。由于算法会保证在每次迭代之后似然函数都会增加，所以函数最终会收敛。

首先，我们要知道EM只是近似计算，EM要解决的问题并不是：我们已知模型的所有参数都有什么，所有的结果我们都能观测得到，然后去估计参数（如果这样的话就直接MLE求解完事了）。

`EM是通过保证关于θ的函数的下界尽可能大,从而使得关于θ的函数尽可能大。`或者说，我根本不知道关于θ的函数最大值在哪儿，但是我可以通过保证关于θ的函数的下界尽可能大，从而保证θ的函数尽可能大。相当于一个班的最低分从60分提到80分，那么我们就知道这个班的最高分肯定不低于80分（因为问题限制所以我们只能绕路来估测参数）。

`综上所述：`

（1）EM只能找到一个不错的局部最优解，不能保证找到全局最优解。

（2）EM对初始值比较敏感，我们最好多找几个θ的初值进行迭代，从中选取最好的。

## `KL 、吉布斯不等式 和 jensen 不等式`


* `1、jensen 不等式：`https://blog.csdn.net/Asher117/article/details/103644674

    * <div align=center><img  src="./static/jensen不等式.jpg"/></div>

    * 如果 `f(x)` 是 `凹函数(比如 log 函数)`，那么 `不等号` 与 `凸函数` 相反


* `2、吉布斯不等式：`https://zh.wikipedia.org/wiki/%E5%90%89%E5%B8%83%E6%96%AF%E4%B8%8D%E7%AD%89%E5%BC%8F

* `3、KL散度：`https://zh.wikipedia.org/wiki/%E7%9B%B8%E5%AF%B9%E7%86%B5

    * 根据定义有：KL ≥ 0 成立


## `EM 公式推导：`

### `推导一：`

<div align=center><img width="800" height="400" src="./static/EM公式推导.jpg"/></div>

补充说明：

* 公式中的 `logP(z|x,θt)` 之所以被社区是因为他与我们要推得 `θ^hat` 无关，因为他只是一个 `常数`。

    理论上在 `log` 符号外的 `P(z|x,θt)` 也可以去掉的，去掉它不影响取极值的时候的参数的值。`不过由于有这一项可以方便EM算法的E步和M步的持续迭代更新，所以这一项都是保留的。`


### `推导二：`

<div align=center><img width="800" height="400" src="./static/EM公式推导2.jpg"/></div>

补充说明：

* 上述 `jensen 不等式` 什么时候 `取等号`：当 `p(x,z|θ) ÷ q(z) = c` (`c是一个常数`时)

* 紧接着我们通过 `q(z) = 1/c * p(x,z|θ)` 推出 `q(z)` 其实就是一个 `后验概率`。


### 广义 EM


<div align=center><img width="800" height="400" src="./static/广义em.jpg"/></div>





## `EM 资料`

* https://zhuanlan.zhihu.com/p/343353302


    关于第二节KL相对熵的补充：

    <div align=center><img  src="./static/ELBO和KL2.png"/></div>


    <div align=center><img  src="./static/1.png"/></div>


* https://zhuanlan.zhihu.com/p/78311644

* https://www.cnblogs.com/pinard/p/6912636.html


    关于式子：

    <div align=center><img  src="./static/3.jpg"/></div>

    这里就是基于x，z的联合分布，来通过求和得到x的边缘分布

    [关于联合概率分布和边缘分布 👆](https://www.zybuluo.com/blueband21c/note/1790855)


* https://www.cnblogs.com/jerrylead/archive/2011/04/06/2006936.html

 
