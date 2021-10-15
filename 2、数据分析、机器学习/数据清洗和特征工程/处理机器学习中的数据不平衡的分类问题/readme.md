
# 处理机器学习中的不平衡分类问题

在信用卡诈骗案例中，我们将诈骗信息和正常交易信息进行可视化显示，我们可以发现正常交易的交易数远远大于诈骗交易的交易数。这样就会影响模型的输出。

如果数据存在严重的不平衡，预测得出的结论往往也是有偏的，即分类结果会偏向于较多观测的类。


### `对于处理数据不平衡问题需要注意的是：`

* 你要对你要分类的问题的数据分布有足够理解。

    * 1、如果原数据分布你的理解应该是均衡的，但是你的训练数据不均衡，那么就要考虑不平衡样本处理。

    * 2、如果原数据分布不是均衡的，但是你的训练集的类别样本分布和原数据分布相同，那么可以不考虑分布不平衡的问题。但是如果两者相差较大，还是要做处理。

### `举例: `

* 1、“如果训练集和测试集的数据分布一样呢？是否需要下采样处理？”，这里要考虑原数据分布的情况，如果和训练集测试集不一样，还是要处理类别不平衡问题。

* 2、“患病的样本比没患病的样本低得多，是否需要下采样处理呢？”，这里首先考虑你的类别分布（先验概率），比如先验是95:5，那么如果你的训练集的分布和这个类别比例差异较大，就需要处理类别不平衡问题。第二要考虑对你对预测效果的期望。`比如你宁愿错把没有疾病的分类为疾病，也不愿意将一个病人误判为没有疾病。这时你需要提高患病类别的权重。`


## `imblearn`

* [imbalance-learn 文档](https://imbalanced-learn.readthedocs.io/en/stable/user_guide.html)


## `什么时候我们应该处理不平衡问题`

* `1、`如果原数据分布你的理解应该是均衡的，但是你的训练数据不均衡，那么就要考虑不平衡样本处理。
    
* `2、`如果原数据分布不是均衡的，但是你的训练集的类别样本分布和原数据分布相同，那么可以不考虑分布不平衡的问题。如果两者相差较大，还是要做处理。

## `为什么类别不平衡会影响模型的输出`

* 许多模型的输出类别是基于阈值的，例如逻辑回归中小于0.5的为反例，大于则为正例。在数据不平衡时，默认的阈值会导致模型输出倾向与类别数据多的类别，体现在模型整体的准确率很高。

* 对于极不均衡的分类问题，比如仅有1%的人是诈骗交易，99%的人是正常交易，最简单的分类模型就是将所有交易都划分为正常交易，模型都能得到99%的准确率，显然这样的模型并没有提供任何的信息。

* 在类别不平衡的情况下，对模型使用F值或者AUC值是更好的选择。

## `处理不平衡数据，可以从两方面考虑：`

* `一、`是改变分类算法，在传统分类算法的基础上对不同类别采取不同的 `加权方式`，使得模型更看重少数类。

* `二、`是 `改变数据分布` ，从数据层面使得类别更为平衡；

### `一、权重法`

    权重法是比较简单的方法，我们可以对训练集里的每个类别加一个权重class weight。

    如果该类别的样本数多，那么它的权重就低，反之则权重就高。

    如果更细致点，我们还可以对每个样本加权重sample weight，思路和类别权重也是一样，即样本数多的类别样本权重低，反之样本权重高。

    sklearn中，绝大多数分类算法都有class weight和 sample weight可以使用。

### `二、改变数据分布`

对数据层面的一些方法，改变数据分布的方法 主要是以下几种重采样

    1）过采样：增加少数类样本的数量

    2）欠采样：减少多数类样本的数量

    3）综合采样：将过采样和欠采样结合


两种方法的先后顺序：我们一般都是 `先采用权重法`，如果权重法做了以后发现预测效果还不好，`再考虑采样法`。


### `查看2D数据的分布`

* `1、`定义绘图函数：

        def plot_2d_space(X, y, label='Classes'):   
            colors = ['#1F77B4', '#FF7F0E']
            markers = ['o', 's']
            for l, c, m in zip(np.unique(y), colors, markers):
                plt.scatter(
                    X[y==l, 0],
                    X[y==l, 1],
                    c=c, label=l, marker=m
                )
            plt.title(label)
            plt.legend(loc='upper right')
            plt.show()


* `2、`如果数据存在多维特征可使用PCA来降维，使其能在2D图中展示

        from sklearn.decomposition import PCA

        pca = PCA(n_components=2)
        X = pca.fit_transform(X)

        plot_2d_space(X, y, 'Imbalanced dataset (2 PCA components)')

* `3、`效果图：

    <div align=center><img width="450" height="300" src="./static/plot_2d_space.jpg"/></div>




## `下采样和过采样`

这里我们先提出两种解决方案也是数据分析中最常用的两种方法，下采样和过采样！

### `一、随机欠采样（下采样）`

* `随机欠采样（下采样）`的目标是通过随机地消除占多数的类的样本来平衡类分布；直到多数类和少数类的实例实现平衡，目标才算达成。

* `随机下采样的优点：`
    
    它可以提升运行时间；并且当训练数据集很大时，可以通过减少样本数量来解决存储问题。

* `随机下采样的缺点：`
    
    它会丢弃对构建规则分类器很重要的有价值的潜在信息。

    被随机欠采样选取的样本可能具有偏差。它不能准确代表大多数。从而在实际的测试数据集上得到不精确的结果。

### `二、随机过采样（Over-Sampling）`

* `随机过采样` 通过随机复制少数类来增加其中的实例数量，从而可增加样本中少数类的代表性。

* `随机过采样的优点：`

    与欠采样不同，这种方法不会带来信息损失。

    表现优于欠采样。

* `随机过采样的缺点：`
    
    由于复制少数类事件，它加大了过拟合的可能性。

## `一、欠采样`

### `1.1、Tomek Links 欠采样`

* `Imbalanced-learn` --> `imblearn` 提供的方法之一是 `Tomek Links`，指的是在两个不同类的样本中最近邻的对方。

* 在这个算法中，最终要将多数类样本从 `Tomek Links` 中移除，这为分类器提供了一个更好的决策边界。

    <div align=center><img width="650" height="200" src="./static/tomek_links.png"/></div>

* 案例：

        from imblearn.under_sampling import TomekLinks

        tl = TomekLinks(return_indices=True, ratio='majority')
        X_tl, y_tl, id_tl = tl.fit_sample(X, y)

        print('Removed indexes:', id_tl)

        plot_2d_space(X_tl, y_tl, 'Tomek links under-sampling')





### `1.2 Cluster Centroids`

* 该技术通过基于聚类方法生成质心来执行欠采样。 数据将按照相似性预先分组，以保留信息。

* 在此示例中，我们将传递参数比率的{0：10}字典，以保留多数类（0）和所有少数类（1）中的10个元素。

* 案例：


        from imblearn.under_sampling import ClusterCentroids

        cc = ClusterCentroids(ratio={0: 10})
        X_cc, y_cc = cc.fit_sample(X, y)

        plot_2d_space(X_cc, y_cc, 'Cluster Centroids under-sampling')



## `二、过采样`

### `2.1、信息性过采样：合成少数类 过采样技术（SMOTE）: `
 
 SMOTE（Synthetic minoritye over-sampling technique,SMOTE）是Chawla在2002年提出的过抽样的算法，一定程度上可以避免数据不平衡的问题。可以参考
    
* `正负样本分布:`
 
   <div align=center><img width="600" height="350" src="./static/1.png"/></div>  
   
    很明显的可以看出，蓝色样本数量远远大于红色样本，在常规调用分类模型去判断的时候可能会导致之间忽视掉红色样本带了的影响，只强调蓝色样本的分类准确性，这边需要增加红色样本来平衡数据集。

    为了让数据平衡，我们采用SMOTE算法对少数类A进行过采样， `SMOTE算法过程是这样的：`
 
* `假设A类样本数为N,对于每个样本x:`
 
    
    <div align=center><img width="600" height="350" src="./static/3.png"/></div>  

    （1）在N个样本中取x(i)的的k个近邻点，从中 `随机选一个点x(j)`,，在x(i)和x(j)之间插入一个点x(i=new)作为新样本：

    <div align=center><img src="./static/smote公式.jpg"/></div>  
    
    （2）将步骤（1）重复N次，就得到M个新样本。
    
    （3）对M个样本全部执行（1）（2）操作，构造新样本。

### `SMOTE 的使用`

用于过采样

    imblearn.over_sampling.SMOTE(sampling_strategy='auto', random_state=None, k_neighbors=5, m_neighbors='deprecated',
     out_step='deprecated', kind='deprecated', svm_estimator='deprecated', n_jobs=1, ratio=None)


* 版本问题：旧版本 `ratio` 参数改为 `sampling_strategy`

* `sampling_strategy`: 
    
    用于指定重抽样的比例，如果指定 `str` 时，指重采样目标的类。不同类别中的样本数量将相等。可能的选择是：

    * 可以是 `minority` ，仅对少数群体重新采样、`not majority`，重新采样除多数类外的所有类、`not minority` 对少数群体以外的所有阶层重新采样、`all`表示采用过采样方法，默认为`auto`，相当于 `not minority`;如果指定字典型的值，其中键为各个类别标签，值为类别下的样本量;

    当为时 `dict`，键对应于目标类。该值对应于每个目标类别的所需样本数。

* `random_state：`用于指定随机数生成器的种子，默认为None,表示使用默认的随机数生成器;

* `k_neighbors：`指定近邻个数，默认为5个;

* `m_neighbors：`指定从近邻样本中随机挑选的样本个数，默认为10个;

* `kind：`用于指定SMOTE算法在生成新样本时所使用的选项，默认为’regular’，表示对少数类别的样本进行随机采样，也可以是’borderline1’、’borderline2’和’svm’;

* `svm_estimator：`用于指定SVM分类器，默认为sklearn.svm.SVC，该参数的目的是利用支持向量机分类器生成支持向量，然后再生成新的少数类别的样本;

* `n_jobs：`用于指定SMOTE算法在过采样时所需的CPU数量，默认为1表示仅使用1个CPU运行算法，即不使用并行运算功能;


### `改进的合成少数类 过采样技术（MSMOTE）`

之后补充


## `可参考 kernel`

* [不平衡数据集的重采样策略](https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets/comments)


* [欠采样（undersampling）和过采样（oversampling）会对模型带来怎样的影响？](https://www.zhihu.com/question/269698662/answer/352279936)

