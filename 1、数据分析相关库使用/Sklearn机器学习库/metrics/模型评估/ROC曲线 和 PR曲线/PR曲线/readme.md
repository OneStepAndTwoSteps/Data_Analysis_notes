## PR (Precision Recall) 曲线

PR曲线展示的是Precision vs Recall的曲线，PR曲线与ROC曲线的相同点是都采用了TPR (Recall)，都可以用AUC来衡量分类器的效果。不同点是ROC曲线使用了FPR，而PR曲线使用了Precision，因此 __PR曲线的两个指标都聚焦于正例__ 。

*   P-R 图直观地显示出学习器在样本总体上的查全率、 查准率。

*   类别不平衡问题中由于主要关心正例，所以在此情况下PR曲线被广泛认为优于ROC曲线。

PR 曲线是以 Recall 为横轴，Precision 为纵轴；而 ROC曲线则是以 FPR 为横轴，TPR 为纵轴。__如下图所示__


<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis_notes/master/1%E3%80%81%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%9B%B8%E5%85%B3%E5%BA%93%E4%BD%BF%E7%94%A8/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/pr/pr2.png"/></div>


### 如何对比多个学习器的性能

__在ROC空间，ROC曲线越凸向左上方向效果越好。与ROC曲线左上凸不同的是，PR曲线是右上凸效果越好。__

`未发生交叉`：在进行比较时，若一个学习器的 P-R 曲线被另一个学习器的 P-R 曲线完全"包住" ，则可断言后者的性能优于前者,如 图中的学习器A和学习器C。

`发生交叉`：如果两个学习器的P - R曲线发生交叉，那么可以比较 P-R曲线下方的面积，但是不容易求，所以可以采用`“平衡点”`作为度量方法，它是`“查全率”`和`“查准率”`相等时的取值，如图中的学习器B的BEP为0.75，A为0.8，可以判断出学习器A优于学习器B。

但是BEP过于简化，更常用的是使用F1度量值。

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis_notes/master/1%E3%80%81%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%9B%B8%E5%85%B3%E5%BA%93%E4%BD%BF%E7%94%A8/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/Performance_metrics/F1.png"/></div>

在一些应用中，`对查准率和查全率的重视程度不同`，可以采用F1度量的一般形式 --- `Fβ`

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis_notes/master/1%E3%80%81%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%9B%B8%E5%85%B3%E5%BA%93%E4%BD%BF%E7%94%A8/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/Performance_metrics/Fβ.png"/></div>


### 使用场景

ROC曲线由于兼顾正例与负例，所以适用于评估分类器的整体性能，相比而言 __PR曲线完全聚焦于正例。__

如果有多份数据且存在不同的类别分布，比如信用卡欺诈问题中每个月正例和负例的比例可能都不相同，这时候如果只想单纯地比较分类器的性能且剔除类别分布改变的影响，则ROC曲线比较适合，因为类别分布改变可能使得PR曲线发生变化时好时坏，这种时候难以进行模型比较；反之，如果想测试不同类别分布下对分类器的性能的影响，则PR曲线比较适合。

如果想要 __评估在相同的类别分布下正例的预测情况__，则宜选 __PR曲线__。

__类别不平衡问题中__ ，__ROC曲线通常会给出一个乐观的效果估计__，所以大部分时候还是 __PR曲线更好__。

最后可以根据具体的应用，在曲线上找到最优的点，得到相对应的precision，recall，f1 score等指标，去调整模型的阈值，从而得到一个符合具体应用的模型。


#### 笔记参考链接：

-《[机器学习之类别不平衡问题 (2) —— ROC和PR曲线](https://zhuanlan.zhihu.com/p/34655990)》





