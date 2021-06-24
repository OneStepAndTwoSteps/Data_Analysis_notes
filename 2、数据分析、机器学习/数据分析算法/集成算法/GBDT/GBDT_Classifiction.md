# GBDT_Classifiction

`注意：`公式中的 `log` 是以 `e` 为底的 `ln`

## `数据`

<div align=center><img  src="./static/GBDT_Classifiction/data.png"/></div>

## `多元 GBDT分类算法 - 损失函数`

假设类别数为N，则此时我们的 `对数似然损失函数` 为：

<div align=center><img  src="./static/GBDT_Classifiction/likelihood.png"/></div>

最小化 `损失函数` 其实就是在 `似然函数` 前面加一个 `负号` 可得：

<div align=center><img width="600" height="120"  src="./static/GBDT_Classifiction/loss_function.jpg"/></div>


可以将 `预测概率为 p ` 的函数转化成，预测 `对数赔率` 函数

<div align=center><img  width="800" height="400"  src="./static/GBDT_Classifiction/loss_function_transform.jpg"/></div>



此时：`对数赔率函数` 就是 `损失函数`。


### `损失函数 - 公式介绍：`

* `yi：`对于二分类，正例即为1，负例即为 0。

* `p：`预测概率，计算步骤如下：

    <div align=center><img  src="./static/GBDT_Classifiction/probability.png"/></div>
    
    `注意：`公式中的 `log` 是以 `e` 为底的 `ln`:

    喜欢 `Loves Troll 2` 的人数为 `2`，不喜欢的人数为 `1` ，则有： 

        log(odds) = log(2/1) = ln(2) ≈ 0.7

        p = e ^ log(odds) / (1+ e ^ log(odds)) = e ^ 0.7 / (1+ e ^ 0.7) ≈ 0.67 


## 流程：

### `Step 1：`

* 初始化模型 `F0(x)`：

    <div align=center><img width="800" height="200" src="./static/GBDT_Classifiction/步骤1.jpg"/></div>

        公式介绍：

        其中 y 为观察值 observed，γ 指理论上的对数赔率值 log(odds)。

    接下来将 `y` 和 `gamma` 代入到表达式中，得到：

    <div align=center><img width="800" height="280" src="./static/GBDT_Classifiction/步骤1-1.jpg"/></div>


    可以将 `对数赔率函数` 转化成 `概率p的函数` ，因为要 `最小化损失函数`，所以求导为 `0` 可得，p = 2/3:

    <div align=center><img width="800" height="250" src="./static/GBDT_Classifiction/步骤1-2.jpg"/></div>


    将` p = 2/3` 代入到 `log(odds)` 中，得到 `F0(x) = log(odds) = log(2/1) = 0.69`



    <div align=center><img src="./static/GBDT_Classifiction/log(odds).jpg"/></div>


### `Step 2：`

* 流程：

    <div align=center><img width="800" height="500" src="./static/GBDT_Classifiction/step2.jpg"/></div>


* 第一步：`计算负梯度`，简化得到结果为：`Observed - p`

    <div align=center><img width="800" height="400" src="./static/GBDT_Classifiction/step2-1.jpg"/></div>























