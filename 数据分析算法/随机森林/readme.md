# 集成算法-随机森林

## 集成算法模型：

### Bagging：

 __并行。__ 训练多个分类器取平均,如随机森林中我们并行运行多个随机数，如果是回归任务我们可以取决策树们的平均值，如果是分类问题我们可以取分类结果中的众数(比如分类结果 0 和 1 ，如果决策出的结果0较多，那么最终分类结果取0) __典型的算法就是随机森林__，可以帮助我们提高泛化能力。

__公式：__

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97/1.png"/></div>


### Boosting:

 __串行。__ 从弱学习器开始加强，通过加权来进行训练，__常见的Boosting模型算法有Adaboost，Xgboost算法__。

举个例子：当我们去银行贷款1000元，但是第一颗树模型(A)预测结果为贷款950元，但是我们的真实值是贷款了100，我们的误差为1000-950=50，接下来我们就需要减少这个误差(50),在我们第二棵树模型(B)就需要在这个50上再进行预测，假设预测结果为30，假设我们就只有三颗树，那么第三颗树(C) 就不再看第B颗树的结果了，而是结合A和B的结果(1000-950-30=20),C树预测的残差值就是20，这个时候如果C数预测的是18，__这个时候根据下面的公式，意思就是我们的之前模型(红色框)+我们现在的模型(紫色框)__ 我们将我们的所有树的结果相加我们的预测值就是998，这个时候我们的效果就很好了。按这个例子来讲的话boosting就是算出A树然后在A树的基础上计算出残差，然后再构造B树，然后C树。串行。

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97/2.png"/></div>


__公式：__

### Stacking:

__堆叠算法__，可以堆叠各种各样的分类器（KNN,SVM,RF等等），堆叠算法分阶段：第一阶段得出各自结果，第二阶段再用前一阶段结果训练。

举个例子：__第一阶段：__ 现在我们分别构建了RF、LR、KNN、SVM算法分类模型，分类器之间的分类结果可能不同，假如我们现在的分类是二分类，现在分类第一个样本，可能 RF分类的结果为1、LR分类的结果为1、KNN分类的结果为1、SVM分类的结果为0，分类第二个样本，可能 RF分类的结果为0、LR分类的结果为1、KNN分类的结果为1、SVM分类的结果为0，分类第三个样本，可能 RF分类的结果为0、LR分类的结果为0、KNN分类的结果为0、SVM分类的结果为0。接下来开始 __第二个阶段：__ 第二个阶段会将第一个阶段的分类结果输入到一个模型(如LR模型)中，然后输出最终的分类结果。

__简而言之:__ 第一个阶段：我们制造多个模型(如分类器)，然后进行特征的输入，得到各个模型的预测结果。第二个阶段，我们将第一个阶段的所有预测结果作为我们这个阶段的输入，输入到我们的一个模型中，最终输出我们的最终结果。



## 随机森林

<div align=center><img width="600" height="400" src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97/3.png"/></div>

我们先按照随机森林这个名称进行讲解：

__随机：__ 1、数据采样随机(如随机抽取60%的样本进行训练) 2、特征选择随机(在样本中随机抽取60%的特征进行训练) (每棵树数据量都是一致的) 因为二重随机，所以我们构造出的树基本都是不同的。一般数据都取总量的(60%-80%)

<div align=center><img width="600" height="400" src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97/4.png"/></div>

__森林：__ 很多颗决策树组成的森林。


### 随机森林优势: 

__1、它能够处理很高维度（feature很多）的数据，并且不用做特征选择__

__2、在训练完后，它能够给出哪些feature比较重要__

如何比较哪个feature比较重要呢？

__如下图：__

<div align=center><img width="600" height="400" src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97/6.png"/></div>

    
假设我们现在有4个特征A,B,C,D现在我们来判断B特征重不重要，假设现在B特征是我们的年龄，并且岁数如我们框中所示，现在我们将四个特征输入到我们的模型中，我们得到一个误差值err1，之后我们破坏我们的B特征，我们将数据破坏成一些没有意义的值，得到我们的新特征B'，我们将 A+B'+C+D这四个特征输入到我们的模型中得到err2，之后我们比较err1和err2，如果相差不大几乎相等，__那么说明B特征不重要__，反之，如果err2远大于err1，__则说明B特征很重要__。

在sklearn中就是用我们上述这样的方法进行特征的判断的，判断之后我们会得到各个特征的重要程度值，__如下图__。


<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97/5.png"/></div>


在这张图中我们大可将最底下的三条特征删除，因为这三条特征看起来并不重要。所以为了避免过拟合我们可以将其删除。

__3、容易做成并行化方法，速度比较快__

__4、可以进行可视化展示，便于分析__



### 注意 

__1、在随机森林中并不是决策树越多越好，实际上基本超过一定数量准确率就会在差不多的基础上上下浮动。(基本在100-200颗树就已经开始饱和)__

<div align=center><img width="600" height="400" src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97/7.png"/></div>



