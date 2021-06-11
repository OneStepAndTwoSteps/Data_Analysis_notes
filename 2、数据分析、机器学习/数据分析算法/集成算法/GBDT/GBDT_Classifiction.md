# GBDT_Classifiction


## `数据`

<div align=center><img  src="./static/GBDT_Classifiction/data.png"/></div>


## `损失函数`

假设类别数为N，则此时我们的对数似然损失函数为：

<div align=center><img  src="./static/GBDT_Classifiction/loss_function.png"/></div>

### 公式介绍：

* `yi：`对于二分类，正例即为1，负例即为 0。

* `p：`预测概率，从上面的数据中可以看出喜欢 `Loves Troll 2` 的概率为:

<div align=center><img  src="./static/GBDT_Classifiction/probability.png"/></div>
   
    log(odds) = log(2/1) 


对于上述的数据则有：

    (1 * log(0.67) + (1-1) * log(1-0.67)) + (1 * log(0.67) + (1-1) * log(1-0.67)) + (0 * log(0.67) + (1-0) * log(1-0.67)) =

    log(0.67) + log(0.67) + log(1 - 0.67) 


















