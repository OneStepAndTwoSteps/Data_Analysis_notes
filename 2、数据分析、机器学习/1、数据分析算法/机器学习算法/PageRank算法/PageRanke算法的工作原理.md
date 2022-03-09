
## PageRanke算法的工作原理

PageRank的作用是评价网页的重要性，以此作为搜索结果的排序重要依据之一。

### 早期的搜索引擎的做法：

  __一、根本不评价结果重要性:__ 
  
  直接按照某自然顺序（例如时间顺序或编号顺序）返回结果，只能适用于结果集比较少的情况。
      
  __二、基于检索词的评价 TF-IDF：__
  
  基于检索词评价的思想非常朴素： __检索词匹配度越高的页面重要性越高。__ “匹配度”就是要定义的具体度量。一个最直接的想法是关键词出现次数越多的页面匹配度越高。但是这样会造成一种情况。 __如果我们的的文章比较长，那么比较长的文章比比较短的文章网页关键词出现的次数就会多一些，这样我们基于检索词评价结果的重要性就显得不合理。__ 所以有人对算法做了 __改进__ ， __使用关键词出现的次数/文章的总词数__ ，这种算法看起来很合理但是非常容易受到"Term Spam”的攻击。
    
  通过一个例子介绍 __Term Spam:__
    现在假设Google单纯使用关键词占比评价页面重要性，而我想让我的文章在搜索结果中排名更靠前（最好排第一）。那么我可以这么做：在页面中加入一个隐藏的html元素（例如一个div），例如我知道现在欧洲杯很火热，我就在我博客的隐藏div里加一万个“欧洲杯”，当有用户搜索欧洲杯时，我的博客就能出现在搜索结果较靠前的位置。 __这种行为就叫做“Term Spam”。__ 这种行为甚至可以干扰别的关键词搜索结果。

早期搜索引擎深受这种作弊方法的困扰，加之基于关键词的评价算法本身也不甚合理，因此经常是搜出一堆质量低下的结果，用户体验大大打了折扣。而Google正是在这种背景下，提出了PageRank算法。


### 简单的PageRank计算：
  
  假设我们现在只有四个网页A,B,C,D他们之间的链接关系为下图所示：
  
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/PageRank%E7%AE%97%E6%B3%95/1.png)
  
  图中的每一个网页表示一个节点，每一条有向边，表示网页之间的入链和出链，入链表示指向自己，出链表示指向别的网页。
  
  __PageRank的算法公式：__
    
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/PageRank%E7%AE%97%E6%B3%95/3.png)
  
u 为待评估的页面，Bu 为页面 u 的入链集合。针对入链集合中的任意页面 v，它能给 u 带来的影响力是其自身的影响力 PR(v) 除以 v 页面的出链数量，即页面 v 把影响力 PR(v) 平均分配给了它的出链，这样统计所有能给 u 带来链接的页面 v，得到的总和就是网页 u 的影响力，即为 PR(u)。

__所以我们会发现，我们出链链接如果增多，会降低我们该页面的影响力，出链链接链接的这些页面会增强被链接页面的影响力。__ 当我们统计了一个网页链接出去的数量，就可以统计出这个网页的跳转概率。

在这个例子中，你能看到 A 有三个出链分别链接到了 B、C、D 上。那么当用户访问 A 的时候，就有跳转到 B、C 或者 D 的可能性，跳转概率均为 1/3。

B 有两个出链，链接到了 A 和 D 上，跳转概率为 1/2。

这样我们就可以得到A,B,C,D四个网页之间的 __转移矩阵__ ，一共4个网页也就形成了这样一个4 * 4维矩阵，N为就是N * N维矩阵

 ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/PageRank%E7%AE%97%E6%B3%95/4.png)

然后，设初始时每个页面的rank值为1/N，这里就是1/4。按A-D顺序将页面rank为向量v：
  
 ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/PageRank%E7%AE%97%E6%B3%95/5.png)

注意，M第一行分别是A、B、C和D转移到页面A的概率，而v的第一列分别是A、B、C和D当前的rank，因此用M的第一行乘以v的第一列，所得结果就是页面A最新rank的合理估计，同理，Mv的结果就分别代表A、B、C、D新rank：

 ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/PageRank%E7%AE%97%E6%B3%95/6.png)

然后用M再乘以这个新的rank向量，又会产生一个更新的rank向量。迭代这个过程，可以证明v最终会收敛，即v约等于Mv，此时计算停止。最终的v就是各个页面的pagerank值。 __例如上面的向量经过几步迭代后，大约收敛在（0.3333，0.2222，0.2222，0.2222），这就是A、B、C、D最后的pagerank，也就是对应着 A、B、C、D 四个页面最终平衡状态下的影响力。__

__通过矩阵相乘验证判断最后影响力确实几乎不发生变化：__

https://github.com/OneStepAndTwoSteps/data_mining_analysis/blob/master/PageRank%E7%AE%97%E6%B3%95/%E5%88%A4%E6%96%AD%E5%BD%B1%E5%93%8D%E5%8A%9B%E4%B8%8D%E5%9C%A8%E5%8F%91%E7%94%9F%E5%8F%98%E5%8C%96.py


### 但是这样简单的PageRank会带来两个问题：
  
  __1. 等级泄露（Rank Leak）：__ 如果一个网页没有出链，就像是一个黑洞一样，吸收了其他网页的影响力而不释放，最终会导致其他网页的 PR 值为 0。 __上面的算法之所以能成功收敛到非零值，很大程度依赖转移矩阵这样一个性质：每列的加和为1。__ 而在这个图中，M第四列将全为0。在没有等级泄露的情况下，每次迭代后向量v各项的和始终保持为1，而有了等级泄露，迭代结果将最终归零(矩阵论的知识,此处略）。

 ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/PageRank%E7%AE%97%E6%B3%95/2.png)



  __2. 等级沉没（Rank Sink）：__ 如果一个网页只有出链，没有入链，计算的过程迭代下来，会导致这个网页的 PR 值为 0（也就是不存在公式中的 V）。

__我们需要一种方法，可以同时解决等级泄露和等级沉没这两个问题。__

### PageRank随机浏览模式：

为了解决简化模型中存在的等级泄露和等级沉没的问题，拉里·佩奇提出了 PageRank 的随机浏览模型。

他定义了阻尼因子 d，这个因子代表了用户按照跳转链接来上网的概率，通常可以取一个固定值 0.85，而 1-d=0.15 则代表了用户不是通过跳转链接的方式来访问网页的，比如直接输入网址。

 ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/PageRank%E7%AE%97%E6%B3%95/7.png)


其中 N 为网页总数，这样我们又可以重新迭代网页的权重计算了， __因为加入了阻尼因子 d，一定程度上解决了等级泄露和等级沉没的问题。__

通过数学定理（这里不进行讲解）也可以证明，最终 PageRank 随机浏览模型是可以收敛的，也就是可以得到一个稳定正常的 PR 值。
