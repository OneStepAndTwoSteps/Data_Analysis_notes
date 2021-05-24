# roc和auc曲线

ROC曲线和PR不是只适用于二分类，多分类模型一样可以使用，但是你需要把它 __看成若干个二分类问题__，分别求出各个阈值对应的指标，然后取平均。

### `一般使用场景`

这一般用于写论文的时候，比如某个公开数据集上目前最好的分类AUC是多少，然后你用另一个分类算法，你觉得有提高，那么你也得看看你算法的AUC，去和它比较，证明你的算法的价值。

当然，在实际产品项目中不需要这么做。

## `什么是 roc 曲线？`

ROC曲线指受试者工作特征曲线 / 接收器操作特性曲线(receiver operating characteristic curve), 是反映敏感性和特异性连续变量的综合指标,是用构图法揭示敏感性和特异性的相互关系，它通过将连续变量设定出多个不同的临界值，从而计算出一系列敏感性和特异性，再 __以敏感性为纵坐标__、__（1-特异性）为横坐标__ 绘制成曲线，__曲线下面积越大，诊断准确性越高。__ 在ROC曲线上，__最靠近坐标图左上方的点为敏感性和特异性均较高的临界值。__

__曲线越靠近左上角，意味着越多的正例优先于负例，模型的整体表现也就越好。__


这些指标从各个不同的角度评价了你的分类模型的准确度和性能。你自己找做算法模型，可以选择一种指标评价你的算法即可。但是如果是要和别人的算法做比较，那么就得使用别人算法使用的指标。目前roc曲线，pr曲线是比较主流的比较算法优劣的工具。

### `TP FP TN FN 分别代表含义`

-《[TP FP TN FN 分别代表含义](https://github.com/OneStepAndTwoSteps/Data_Analysis/tree/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0)》

## `roc曲线的作用`

二分类问题在机器学习中是一个很常见的问题，经常会用到。ROC (Receiver Operating Characteristic) 曲线和 AUC (Area Under the Curve) 值常被用来评价一个二值分类器 (binary classifier) 的优劣。


## `roc曲线`

在roc曲线中，我们绘制出来的图像他的横坐标表示 FPR 他的纵坐标表示 TPR __如下图所示__

<div align=center><img width="500" height="400" src="./static/roc.png"/></div>

其中 FPR 的计算公式为 `FP/(FP+TN)` ,表示伪正类率(False positive rate， FPR)，预测为正但实际为负的样本占所有负例样本的比例；通俗来讲就是 当我们设置男性为正类，那么将女性预测为男性占所有女性的比例。__`FPR越大，预测正类中实际负类越多。`__

其中 TPR 的计算公式为 `TP/(TP+FN)`，表示真正类率(True positive rate， TPR 也称召回率)，预测为正且实际为正的样本占所有正例样本的比例。通俗来讲就是 当我们设置男性为正类，那么预测为男性的占所有男性的比例。__`TPR越大，预测正类中实际正类越多。`__

__计算公式图：__

<div align=center><img  src="./static/%E5%85%AC%E5%BC%8F%E5%9B%BE%E8%A7%A3.png"/></div>


#### `我们再来看看ROC曲线中的“四点一线”`

第一个点，(0,1)，即FPR=0, TPR=1，这意味着FN（false negative）=0，并且FP（false positive）=0。这是一个完美的分类器，它将所有的样本都正确分类。

第二个点，(1,0)，即FPR=1，TPR=0，类似地分析可以发现这是一个最糟糕的分类器，因为它成功避开了所有的正确答案。

第三个点，(0,0)，即FPR=TPR=0，即FP（false positive）=TP（true positive）=0，可以发现该分类器预测所有的样本都为负样本（negative）。__此时我们的threshold值最大__，为什么呢？因为我们判断正类需要该样本的分数大于阈值，此时FP=TP=0 意味着所有的正类分数都小于阈值，即判断为正类为0，

第四个点（1,1），即FPR=TPR=1，分类器实际上预测所有的样本都为正样本。__此时threshold最小__，即把所有的样本都视为正类。

对于ROC曲线，我们可以这样理解，对于二分类问题，曲线的每一个点都代表一个阈值，分类器给每个样本一个得分，得分大于阈值的我们认为是正样本，小于阈值的我们认为是负样本。


通过阈值我们可以得到 各个评估值 的得分，比如TPR,FPR值，通过这些值我们可以得到在不同阈值下，我们模型预测的好坏，这样我们之后也可以通过设置阈值来帮助我们模型进行准确度的提升。__（ROC曲綫和PR曲綫主要还是用于算法评估）__

如下面这幅图，(a)图中实线为ROC曲线，线上每个点对应一个阈值。

<div align=center><img  src="./static/roc3.png"/></div>

(a) 理想情况下，TPR应该接近1，FPR应该接近0。ROC曲线上的每一个点对应于一个threshold，对于一个分类器，每个threshold下会有一个TPR和FPR。比如Threshold最大时，TP=FP=0，对应于原点；Threshold最小时，TN=FN=1，对应于右上角的点(1,1)。

(b) P和N得分不作为特征间距离d的一个函数，随着阈值theta增加，TP和FP都增加。


### `在如上图所示的 roc 曲线中如何评估模型的优劣`

    1、在ROC空间，ROC曲线越凸向左上方向效果越好。

    2、若学习器A的ROC曲线将另外一个学习器B的曲线完全包住，则A的性能一定比B好，否则若二者曲线有交叉，则可以较为合理的认为ROC曲线越接近左上角，也就是AUC值越大，整个分类器的性能越好。

    3、对于并不是完全包住，那我们得从实际情况对那种参数更加偏好来考虑，但是一般我们就考察ROC围成的面积，也就是AUC值。哪个AUC值大，哪个分类器就好。


### `为什么使用roc曲线`

ROC曲线有个很好的特性：当测试集中的正负样本的分布变化的时候，ROC曲线能够保持不变。在实际的数据集中经常会出现类不平衡（class imbalance）现象，即负样本比正样本多很多（或者相反），而且测试数据中的正负样本的分布也可能随着时间变化。下图是 ROC 曲线和 PR 曲线对比图。

<div align=center><img src="./static/roc%E5%92%8Cpr.png"/></div>


在上图中，(a)和(c)为ROC曲线，(b)和(d)为Precision-Recall曲线。(a)和(b)展示的是分类其在原始测试集（正负样本分布平衡）的结果，(c)和(d)是将测试集中负样本的数量增加到原来的10倍后，分类器的结果。可以明显的看出，ROC曲线基本保持原貌，而Precision-Recall曲线则变化较大。

#### `为什么当测试集中的正负样本的分布变化的时候，ROC曲线能够保持不变?`

__根据公式__

    FPR = FP/(FP+TN)
    TPR = TP/(TP+FN)

注意TPR用到的TP和FN同属P列，FPR用到的FP和TN同属N列，所以即使P或N的整体数量发生了改变，也不会影响到另一列。也就是说，即使正例与负例的比例发生了很大变化，ROC曲线也不会产生大的变化，而像Precision使用的TP和FP就分属两列，则易受类别分布改变的影响。

## `AUC值`

`AUC值 Area Under Curve (曲线下面积)`，也就是 `ROC曲线` 之下与坐标轴围成的面积。我们很容易就会看出来，`AUC` 其实是 `ROC曲线` 的积分，但是这样很不直观，也不能感性理解，其实 `AUC` 确实是有物理意义的。`AUC` 是指 `随机给定一个正样本和一个负样本，分类器输出的正样本的概率比分类器输出负样本的概率大的可能性。`

从上图的 `roc曲线` 中我们可以发现，经过虚线划分，我们的虚线下的面积为0.5，所以我们的 `AUC` 一般来说都是大于0.5的。当 `AUC` 值等于0.5时，我们可以认为分类器不起作用。`AUC` 小于0.5时，实际情况基本不会出现，不符合真实情况。

### `为什么会造成，AUC越大，正确率越高呢？`

<div align=center><img  src="./static/roc4.png"/></div>


以上图为例，图中[0,0]到[1,1]的虚线即为随机线，该线上所有的点都表示该阈值下TPR=FPR。

`ROC曲线围成的面积 (即AUC)可以解读为：从所有正例中随机选取一个样本A，再从所有负例中随机选取一个样本B，分类器将A判为正例的概率比将B判为正例的概率大的可能性。`可以看到位于随机线上方的点(如图中的A点)被认为好于随机猜测。在这样的点上TPR总大于FPR，意为正例被判为正例的概率大于负例被判为正例的概率。

从另一个角度看，由于画ROC曲线时都是先将所有样本按分类器的预测概率排序，所以AUC反映的是分类器对样本的排序能力，依照上面的例子就是A排在B前面的概率。AUC越大，自然排序能力越好，即分类器将越多的正例排在负例之前。


__`简单说：AUC值越大的分类器，正确率越高。`__


## `roc曲线的缺点`

__1、__ 上文提到ROC曲线的优点是不会随着类别分布的改变而改变，但这在某种程度上也是其缺点。因为负例N增加了很多，而曲线却没变，这等于产生了大量FP。像信息检索中如果主要关心正例的预测准确性的话，这就不可接受了。

__2、__ 在类别不平衡的背景下，负例的数目众多致使FPR的增长不明显，导致ROC曲线呈现一个过分乐观的效果估计。ROC曲线的横轴采用FPR，根据FPR = FP/N = FP/(FP+TN) ，当负例N的数量远超正例P时，FP的大幅增长只能换来FPR的微小改变。结果是虽然大量负例被错判成正例，在ROC曲线上却无法直观地看出来。（当然也可以只分析ROC曲线左边一小段）

## `小结`

__1、__ 通过比较roc曲线的左上凸的趋势，以用来评估我们二分类模型的优劣，在ROC空间，ROC曲线越凸向左上方向效果越好

__2、__ 若学习器A的ROC曲线将另外一个学习器B的曲线完全包住，则A的性能一定比B好，否则若二者曲线有交叉，则可以较为合理的认为ROC曲线越接近左上角，也就是AUC值越大，整个分类器的性能越好。

__3、__ 对于并不是完全包住，那我们得从实际情况对那种参数更加偏好来考虑，但是一般我们就考察ROC围成的面积，也就是AUC值。哪个AUC值大，哪个分类器就好。

__4、__ 通过阈值我们可以得到 各个评估值 的得分，比如TPR,FPR值，通过这些值我们可以得到在不同阈值下，我们模型预测的好坏，这样我们之后也可以通过设置阈值来帮助我们模型进行准确度的提升。

__5、__ AUC值越大的分类器，正确率越高。

## `sklearn.metrics.roc_curve使用说明`

### `导入包`

    from sklearn.metrics import roc_curve, auc


### `参数说明`

    参数：

        y_true：数组，存储数据的标签，维度就是样本数，形如[0,1,1,0,1...]这样的，也可以是-1和1，只要有两个值

    　　y_score：数组，存储数据的预测概率值，维度也是样本数，形如[0.38,0.5,0.8]这样的

    　　pos_label：整型或字符串，当y_true中只有一个值时，比如都是1或者都是0，无法判断哪个是正样本，需要用一个数字或字符串指出

    　　sample_weight：采样权重，可选择取其中的一部分进行计算。

    　　drop_intermediate：即可选择去掉一些对于ROC性能不利的阈值，使得得到的曲线有更好的表现性能。

    返回值：一共三个，分别是fpr,tpr,thresholds

    　　fpr：数组，根据不同阈值求出的fpr。

    　　tpr：数组，根据不同阈值求出的tpr。

    　　thresholds：数组，对预测值排序后的score列表，作为阈值，排序从大到小

        这三个返回值阈值对应的 fpr tpr 是一一对应的。

### `案例`

    import numpy as np
    from sklearn import metrics
    y = np.array([1, 1, 2, 2])
    scores = np.array([0.1, 0.4, 0.35, 0.8])
    fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)

    print('取不同阈值时fpr的变化：',fpr)
    print('取不同阈值时tpr的变化：',tpr)


    print('\n')
    print('阈值：',thresholds)


    # 取不同阈值时fpr的变化： [0.  0.5 0.5 1. ]
    # 取不同阈值时tpr的变化： [0.5 0.5 1.  1. ]
    #
    #
    # 阈值： [0.8  0.4  0.35 0.1 ]

pos_label帮助我们选择正类，这里我们将2设置为正类。

这里我们的阈值默认为 预测值排序后的score列表 在案例中也就是 [0.1, 0.4, 0.35, 0.8]，此时当我们的分数超过我们的阈值，比如当阈值取0.1时，socres所有的分数都大于等于0.1，所有我们将其都人作为正类，之后我们就可以进行计算得出 TP,FP,FN,TN,然后也就可以计算出 fpr 和 tpr。

输出的fpr和tpr是根据不同阈值得出的结果。



### `绘制曲线`


    from sklearn.metrics import roc_curve, auc
    #plt.style.use('seaborn-pastel')
    y_score = logreg.decision_function(X_test)

    FPR, TPR, _ = roc_curve(y_test, y_score)
    ROC_AUC = auc(FPR, TPR)
    print (ROC_AUC)

    plt.figure(figsize =[11,9])
    plt.plot(FPR, TPR, label= 'ROC curve(area = %0.2f)'%ROC_AUC, linewidth= 4)
    plt.plot([0,1],[0,1], 'k--', linewidth = 4)
    plt.xlim([0.0,1.0])
    plt.ylim([0.0,1.05])
    plt.xlabel('False Positive Rate', fontsize = 18)
    plt.ylabel('True Positive Rate', fontsize = 18)
    plt.title('ROC for Titanic survivors', fontsize= 18)
    plt.show()


#### `示意图`




<div align=center><img width="500" height="400" src="./static/roc2.png"/></div>




#### 笔记参考链接：

-《[机器学习之分类性能度量指标 : ROC曲线、AUC值、正确率、召回率](https://www.jianshu.com/p/c61ae11cc5f6)》

-《[sklearn.metrics.roc_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)》

-《[ROC曲线与AUC值及其铺垫](https://juejin.im/post/5a1a768251882535cd4a8984#heading-11)》

-《[ROC 曲线与 PR 曲线](https://wulc.me/2018/06/16/ROC%20%E6%9B%B2%E7%BA%BF%E4%B8%8E%20PR%20%E6%9B%B2%E7%BA%BF/)》

-《[机器学习之类别不平衡问题 (2) —— ROC和PR曲线](https://zhuanlan.zhihu.com/p/34655990)》

