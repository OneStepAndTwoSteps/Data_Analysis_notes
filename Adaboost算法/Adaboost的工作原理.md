## Adaboost算法：

__AdaBoost 算法__ 在数据挖掘中，分类算法可以说是核心算法，其与随机森林算法一样都属于 __分类算法中的集成算法。__

### 什么是集成？
集成用我们通俗的话来说就是“三个臭皮匠，顶个诸葛亮”。通过构建并结合多个机器学习器来完成学习任务，并且达到一个更好的结果。

### 为什么要集成？
因为臭皮匠好训练，诸葛亮却不好求。因此要打造一个诸葛亮，最好的方式就是训练多个臭皮匠，然后让这些臭皮匠组合起来，这样往往可以得到很好的效果。 __这就是 Boosting 算法的原理。__

### 集成算法的两种方式：
集成算法通常有两种方式，分别是投票选举（bagging）和再学习（boosting）。

__投票选举__ 的场景类似把专家召集到一个会议桌前，当做一个决定的时候，让 K 个专家（K 个模型）分别进行分类，然后选择出现次数最多的那个类作为最终的分类结果。

__再学习__ 相当于把 K 个专家（K 个分类器）进行加权融合，形成一个新的超级专家（强分类器），让这个超级专家做判断。

__投票选举和再学习的区别__ 。Boosting 的含义是提升，它的作用是每一次训练的时候都对上一次的训练进行改进提升，在训练的过程中这 K 个“专家”之间是有依赖性的，当引入第 K 个“专家”（第 K 个分类器）的时候，实际上是对前 K-1 个专家的优化。而 bagging 在做投票选举的时候可以并行计算，也就是 K 个“专家”在做判断的时候是相互独立的，不存在依赖性。

### Adaboost的工作原理：

举个例子 我们将弱分类器G1(x),弱分类器G2(x)，......弱分类器Gn(x)，通过不同的权重α1,α2,α3进行一个组合，集成为我们的诸葛亮(强分类器)。

假设弱分类器为Gi(x)，他在强分类器中的权重为αi，那么我们可以得到这个强分类器的公式：

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/1.png"/></div>

也就是将我们的弱分类器进行一个组合，变成强分类器。

这里我们引入一个概念， __最优弱分类器__ ，我们在进行弱分类器的组合的时候，我们需要选出最优弱分类器，为它赋予更高的 __权重__ ，分类器的效果不好我们就降低它的权重。那么我们 __在进行迭代训练过程中如何知道哪个分类器是最优弱分类器__ ，还有如何计算每个分类器对应的权重呢？

我们通常采用 __弱分类器对样本分类的错误率进行一个权重的分配__ ，用公式表示就是：

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/2.png"/></div>

其中 __ei表示的是第 i 个分类器的分类错误率。__

同时我们会选择错误率最低的弱分类器作为最优弱分类器。

 通常我们使用 __Dk+1 代表第 k+1 轮训练中，样本的权重集合__ ，其中 Wk+1,1 代表第 k+1 轮中第 N 个样本的权重，因此用公式表示为：
 
<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/3.png"/></div>

__第 k+1 轮中的样本权重求解__ ，是根据该样本在第 k 轮的权重以及第 k 个分类器的准确率而定，具体的公式为：
<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/4.png"/></div>


### AdaBoost 算法示例

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/12.png"/></div>

首先在第一轮训练中，我们得到 10 个样本的权重为 1/10，即初始的 10 个样本权重一致，D1=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)。

假设我有 3 个基础分类器：

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/5.png"/></div>


我们可以知道分类器 f1 的错误率为 0.3，也就是 x 取值 6、7、8 时分类错误；分类器 f2 的错误率为 0.4，即 x 取值 0、1、2、9 时分类错误；分类器 f3 的错误率为 0.3，即 x 取值为 3、4、5 时分类错误。

这 3 个分类器中，f1、f3 分类器的错误率最低，因此我们选择 f1 或 f3 作为最优分类器，假设我们选 f1 分类器作为最优分类器，即第一轮训练得到：

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/6.png"/></div>


根据分类器权重公式得到：
<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/7.png"/></div>



然后我们对下一轮的样本更新求权重值，代入 Wk+1,i 和Dk+1 的公式，可以得到新的权重矩阵：D2=(0.0715, 0.0715, 0.0715, 0.0715, 0.0715, 0.0715, 0.1666, 0.1666, 0.1666, 0.0715)。

在第二轮训练中，我们继续统计三个分类器的准确率，可以得到分类器 f1 的错误率为 0.1666*3，也就是 x 取值为 6、7、8 时分类错误。分类器 f2 的错误率为 0.0715*4，即 x 取值为 0、1、2、9 时分类错误。分类器 f3 的错误率为 0.0715*3，即 x 取值 3、4、5 时分类错误。

在这 3 个分类器中，f3 分类器的错误率最低，因此我们选择 f3 作为第二轮训练的最优分类器，即：

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/8.png"/></div>


根据分类器权重公式得到：

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/9.png"/></div>


然后我们对下一轮的样本更新求权重值，代入 Wk+1,i 和Dk+1  的公式，可以得到 D3=(0.0455,0.0455,0.0455,0.1667, 0.1667,0.01667,0.1060, 0.1060, 0.1060, 0.0455)。

在第三轮训练中，我们继续统计三个分类器的准确率，可以得到分类器 f1 的错误率为 0.1060*3，也就是 x 取值 6、7、8 时分类错误。分类器 f2 的错误率为 0.0455*4，即 x 取值为 0、1、2、9 时分类错误。分类器 f3 的错误率为 0.1667*3，即 x 取值 3、4、5 时分类错误。

在这 3 个分类器中，f2 分类器的错误率最低，因此我们选择 f2 作为第三轮训练的最优分类器，即：

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/10.png"/></div>


根据分类器权重公式得到：

<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Adaboost%E7%AE%97%E6%B3%95/11.png"/></div>


假设我们只进行 3 轮的训练，选择 3 个弱分类器，组合成一个强分类器，那么最终的强分类器 G(x) = 0.4236G1(x) + 0.6496G2(x)+0.7514G3(x)。


实际上 AdaBoost 算法是一个框架，你可以指定任意的分类器，通常我们可以采用 CART 分类器作为弱分类器。通过上面这个示例的运算，你体会一下 AdaBoost 的计算流程即可。



