## FP-Growth 算法的工作原理
### 例子
首先我们把上面案例中的商品用 ID 来代表，牛奶、面包、尿布、可乐、啤酒、鸡蛋的商品 ID 分别设置为 1-6，上面的数据表可以变为：

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/2.png)

### FP-Growth 算法的特点

一、创建了一棵 FP 树来存储频繁项集。在创建前对不满足最小支持度的项进行删除，减少了存储空间。我稍后会讲解如何构造一棵 FP 树；
二、整个生成过程只遍历数据集 2 次，大大减少了计算量。

所以在实际工作中，我们 __常用 FP-Growth 来做频繁项集的挖掘__ ，下面我给你简述下 FP-Growth 的原理。

### FP-Growth 算法的工作原理
__1. 创建项头表（item header table）__
创建项头表的作用是为 FP 构建及频繁项集挖掘提供索引。
这一步的流程是先扫描一遍数据集(第一次扫描数据)，对于满足最小支持度的单个项（K=1 项集） __按照支持度从高到低进行排序，这个过程中删除了不满足最小支持度的项__，然后将1项频繁集放入项头表，__并按照支持度降序排列__。接着第二次扫描数据，将读到的原始数据剔除非频繁1项集，并按照支持度降序排列。

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/9-1.png)


__详细介绍：__ 

__第一次扫描数据：__ 我们现在有5条数据(看上面的例子图)，所以我们每个商品出现一次我们的支持度就增加20%，首先第一次扫描数据并对1项集计数，这里我们假设支持度设置成大于40%，那么可乐和鸡蛋这两个商品就无法成为我们的表头项，剩下的牛奶、面包、尿布、啤酒按照支持度的大小降序排列，组成了我们的项头表。

__第二次扫描数据：__ 对于每条数据剔除非频繁1项集，并按照支持度降序排列。比如订单编号2，里面4是非频繁1项集，因此被剔除，只剩下了2、3、5。按照支持度的顺序排序，它变成了3、2、5。其他的数据项以此类推。为什么要将原始数据集里的频繁1项数据项进行排序呢？这是为了我们后面的FP树的建立时，可以尽可能的共用祖先节点。

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/21.png)


通过两次扫描，项头表已经建立，排序后的数据集也已经得到了，下面我们再看看怎么建立FP树。

__2. 构造 FP 树__
FP 树的根节点记为 NULL 节点。
整个流程是需要再次扫描数据集，对于每一条数据，按照支持度从高到低的顺序进行创建节点（也就是第一步中项头表中的排序结果），节点如果存在就将计数 count+1，如果不存在就进行创建(什么意思呢？ __看下面的补充介绍__)。同时在创建的过程中，需要更新项头表的链表。

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/10-3.png)

我们可以在图中观察到，第一个节点的支持度为5，我们右侧的树状结构图的第一个节点也是5，接下来的节点层数(比如说第二层)他的总的支持度相加也是5，第三层同理，因为我们所有的物品组合中都包含尿布，所以他的支持度最高。我们把它放在最上面。

__补充介绍：__
举个例子当我们第一个组合为ACEBF,此时FP树没有节点，因此ACEBF是一个独立的路径，所有节点计数为1项头表通过节点链表链接上对应的新增节点。

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/14.png)

接着插入数据ACG，如图4所示。由于ACG和现有的FP树可以有共有的祖先节点序列AC，因此只需要增加一个新节点G，将新节点G的计数记为1。同时A和C的计数加1成为2。当然，对应的G节点的节点链表要更新。

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/13.png)


__3. 通过 FP 树挖掘频繁项集__
到这里，我们就得到了一个存储频繁项集的 FP 树，以及一个项头表。我们可以通过项头表来挖掘出每个频繁项集。
具体的操作会用到一个概念，叫 __“条件模式基”__ ，它指的是以要挖掘的节点为叶子节点， __自底向上求出 FP 子树__ ，然后 __将 FP 子树的祖先节点设置为叶子节点之和。__
我以“啤酒”的节点为例，从 FP 树中可以得到一棵 FP 子树，将祖先节点的支持度记为叶子节点之和，得到：

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/11.png)

我们可以看出来，相比于原来的 FP 树，尿布和牛奶的频繁项集数减少了。这是因为我们求得的是以“啤酒”为节点的 FP 子树，也就是说，在频繁项集中一定要含有“啤酒”这个项。我们可以再看下原始的数据，其中订单 1{牛奶、面包、尿布}和订单 5{牛奶、面包、尿布、可乐}并不存在“啤酒”这个项，所以针对订单 1，尿布→牛奶→面包这个项集就会从 FP 树中去掉，针对订单 5 也包括了尿布→牛奶→面包这个项集也会从 FP 树中去掉，所以你能看到以“啤酒”为节点的 FP 子树，尿布、牛奶、面包项集上的计数比原来少了 2。

__条件模式基不包括“啤酒”节点，__ 而且祖先节点如果小于最小支持度就会被剪枝，所以“啤酒”的条件模式基为空。  

__条件模式基讲解：__ FP -Growth中有一个概念叫：条件模式基。它在FP树创建的时候还用不上，创建的时候主要是通过扫描整个数据，和项头表来构造FP树。条件模式基用于挖掘频繁项的过程。通过数找到每个项（item）的条件模式基，递归挖掘频繁项集

## 条件模式基补充： FP 树挖掘

把FP树建立起来后，怎么去挖掘频繁项集呢？下面讲如何从FP树里挖掘频繁项集。得到了FP树和项头表以及节点链表，首先要从项头表的底部项依次向上挖掘。对于项头表对应于FP树的每一项，我们要找到它的条件模式基。 __所谓条件模式基是以我们要挖掘的节点作为叶子节点所对应的FP子树__ 。得到这个FP子树，将子树中每个节点的的计数设置为叶子节点的计数，并删除计数低于支持度的节点。 __从这个条件模式基，我们就可以递归挖掘得到频繁项集了。__

__以下图这个的例子来讲解__

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/19.png)


__先从最底下的F节点开始，寻找F节点的条件模式基，由于F在FP树中只有一个节点，因此候选就只有下图左所示的一条路径，对应{A:8,C:8,E:6,B:2, F:2}。接着将所有的祖先节点计数设置为叶子节点的计数，即FP子树变成{A:2,C:2,E:2,B:2, F:2}。一般我们的条件模式基可以不写叶子节点，因此最终的F的条件模式基如下图右所示。__

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/15.png)

__通过它很容易得到F的频繁2项集为{A:2,F:2}, {C:2,F:2}, {E:2,F:2}, {B:2,F:2}。递归合并二项集，得到频繁三项集为{A:2,C:2,F:2}，{A:2,E:2,F:2},...还有一些频繁三项集，就不写了。当然一直递归下去，最大的频繁项集为频繁5项集，为{A:2,C:2,E:2,B:2,F:2}。__

__F挖掘完了，我们开始挖掘D节点。D节点比F节点复杂一些，因为它有两个叶子节点，因此首先得到的FP子树如下图左。接着将所有的祖先节点计数设置为叶子节点的计数，即变成{A:2, C:2,E:1 G:1,D:1, D:1}此时E节点和G节点由于在条件模式基里面的支持度低于阈值，被我们删除，最终在去除低支持度节点并不包括叶子节点后D的条件模式基为{A:2, C:2}。__ 通过它，我们很容易得到D的频繁2项集为{A:2,D:2}, {C:2,D:2}。递归合并二项集，得到频繁三项集为{A:2,C:2,D:2}。D对应的最大的频繁项集为频繁3项集。

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/16.png)

__同样的方法可以得到B的条件模式基如下图右边，递归挖掘到B的最大频繁项集为频繁4项集{A:2, C:2, E:2,B:2}。__

G和E省略.....

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/17.png)

__C的条件模式基如下图右边，递归挖掘到C的最大频繁项集为频繁2项集{A:8, C:8}。__

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/Apriori/18.png)

至此我们得到了所有的频繁项集，如果我们只是要最大的频繁K项集， __从上面的分析可以看到，最大的频繁项集为5项集。包括{A:2, C:2, E:2,B:2,F:2}。__

