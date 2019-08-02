##  MAE、MSE、RMSE 和 RMSLE指标

在回归模型中我们主要使用的评估指标为 RMSE 和 RMLSE，但是在介绍 RMSE 和 RMLSE之前，我们还会先介绍一下 MAE 和 MSE

### 1、MAE

平均绝对误差MAE（Mean Absolute Error）又被称为 L1范数损失。

#### 公式：

<div align=center><img  src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/%E5%9B%9E%E5%BD%92%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/mae.png"/></div>


#### MAE 的不足？

MAE虽能较好衡量回归模型的好坏，但是绝对值的存在导致函数不光滑，在某些点上不能求导，可以考虑将绝对值改为残差的平方，这就是均方误差。

### 2、MSE

均方误差MSE（Mean Squared Error）又被称为 L2范数损失。

__均方误差是反映估计量与被估计量之间差异程度的一种度量__。

换句话说，参数估计值与参数真值之差的平方的期望值。 __MSE可以评价数据的变化程度，MSE的值越小，说明预测模型描述实验数据具有更好的精确度。__

均方误差 __指的就是模型预测值 f(x) 与样本真实值 y 之间距离平方的平均值。__

#### 其公式如下所示：

<div align=center><img  src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/%E5%9B%9E%E5%BD%92%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/mse.png"/></div>

仔细看一下，这不就是回归常用的均方损失函数吗？

由于MSE与我们的目标变量的量纲不一致，为了保证量纲一致性，我们需要对MSE进行开方 。

### 3、RMSE

均方根误差 RMSE

均方根误差是用来 __衡量预测值同真实值之间的偏差。__

均方根误差亦称 __标准误差__，是均方误差的算术平方根。
 
换句话说，是所有样本预测与真实值的误差和的平方与样本数1/n的平方根。标准误差对一组测量中的特大或特小误差反映非常敏感，所以，标准误差能够很好地反映出测量的精密度。这正是标准误差在工程测量中广泛被采用的原因。因此， __标准差是用来衡量一组数自身的离散程度__ ，而 __均方根误差是用来衡量预测值同真实值之间的偏差。__

在回归模型中，这个不就是我们所有样本的 (预测值 - 真实值) ^2 之和取平均 然后开庚号吗？

#### 公式：

从公式来看，其实就是MSE的开庚号， __开庚号之和有什么意义呢？__ 上面说了 __为了保证量纲一致性__ ，我们需要对MSE进行开方 。否则那就是误差的平方倍了呀，举个例子，假如房价预测值为100W 真实值为98W，那么不开庚号，的出来的结果就是 2W的平方呀，那么单位就对不上了，所以要开方。

<div align=center><img  src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/%E5%9B%9E%E5%BD%92%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/rmse.png"/></div>


上面的几种衡量标准的取值大小与具体的应用场景有关系，很难定义统一的规则来衡量模型的好坏。


### 4、RMSLE

均方根平方对数误差（RMSLE）

#### 公式：

<div align=center><img  src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/%E5%9B%9E%E5%BD%92%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/rmsle.png"/></div>

## 在回归模型中我们主要使用的评估指标为 RMSE 和 RMLSE

### RMSE 和 RMSE 的对比

如果预测的值的范围很大，RMSE会被一些大的值主导。这样即使你很多小的值预测准了，但是有一个非常大的值预测的不准确，RMSE就会很大。 相应的，如果另外一个比较差的算法对这一个大的值准确一些，但是很多小的值都有偏差，可能RMSE会比前一个小。先取log再求RMSE，可以稍微解决这个问题。 __RMSE一般对于固定的平均分布的预测值才合理。__


__使用RMSLE的好处一：__  

  假如真实值为1000，若果预测值是600，那么RMSE=400， RMSLE=0.510
  
  假如真实值为1000，若预测结果为1400， 那么RMSE=400， RMSLE=0.336  

可以看出来在均方根误差相同的情况下，预测值比真实值小这种情况的错误比较大，即对于预测值小这种情况惩罚较大。 __如果预测值比实际值低时，它的惩罚更高。__


__如下图:__ 图的最低点是真实值：3，从图来看，越偏离真实值，误差越大。但偏左边和偏右边误差增长幅度不一样，预测值比真实值小这种情况的错误比较大，反正亦如

<div align=center><img width="500" height="400"  src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/%E5%9B%9E%E5%BD%92%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/rmsle2.jpg"/></div>

__使用RMSLE的好处二：__ 

当数据当中有少量的值和真实值差值较大的时候，使用log函数能够减少这些值对于整体误差的影响。


### 各种回归指标对比：

MSE和MAE适用于误差相对明显的时候，大的误差也有比较高的权重， __RMSE则是针对误差不是很明显的时候__ ；MAE是一个线性的指标，所有个体差异在平均值上均等加权，所以它更加凸显出异常值，相比MSE；

RMSLE: __主要针对数据集中有一个特别大的异常值__，这种情况下，data会被skew，RMSE会被明显拉大，这时候就需要先对数据log下，再求RMSE，这个过程就是RMSLE。对低估值（under-predicted）的判罚明显多于估值过高(over-predicted)的情况（RMSE则相反）


### 小结

__均方根误差（RMSE）和均方根平方对数误差（RMSLE）都是找出机器学习模型预测值与实际值之间差异的技术。__

要了解这些概念及其差异，了解均方误差（MSE）的含义非常重要。MSE结合了预测变量的方差和偏差。RMSE是MSE的平方根。在无偏估计的情况下，RMSE只是方差的平方根，实际上是标准偏差。

注意：方差的平方根是标准偏差。

在RMSLE的情况下，您可以记录预测和实际值。所以基本上，你所测量的方差会有什么变化。__我相信RMSLE通常用于当你不想在预测值和真值都是巨大数字时惩罚预测值和实际值的巨大差异时。__

    如果预测值和实际值都很小：RMSE和RMSLE相同。

    如果预测或实际值很大：RMSE> RMSLE

    如果预测值和实际值都很大：RMSE> RMSLE（RMSLE几乎可以忽略不计）
