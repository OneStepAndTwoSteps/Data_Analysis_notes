# Sklearn 使用pca降维

在scikit-learn中，与PCA相关的类都在sklearn.decomposition包中。最常用的PCA类就是sklearn.decomposition.PCA，我们下面主要也会讲解基于这个类的使用的方法。

*   __KernelPCA__

    除了PCA类以外，最常用的PCA相关类还有KernelPCA类，它 __主要用于非线性数据的降维__，需要用到核技巧。因此在使用的时候需要选择合适的核函数并对核函数的参数进行调参。

*   __IncrementalPCA类__

    另外一个常用的PCA相关类是IncrementalPCA类，它 __主要是为了解决单机内存限制的__。有时候我们的样本量可能是上百万+，维度可能也是上千，直接去拟合数据可能会让内存爆掉， 此时我们可以用IncrementalPCA类来解决这个问题。IncrementalPCA先将数据分成多个batch，然后对每个batch依次递增调用partial_fit函数，这样一步步的得到最终的样本最优降维。

*   __SparsePCA和MiniBatchSparsePCA__

    此外还有SparsePCA和MiniBatchSparsePCA。他们 __和上面讲到的PCA类的区别主要是使用了L1的正则化__ ，这样可以将很多非主要成分的影响度降为0，这样在PCA降维的时候我们仅仅需要对那些相对比较主要的成分进行PCA降维，避免了一些噪声之类的因素对我们PCA降维的影响。
    
    SparsePCA和MiniBatchSparsePCA之间的区别则是MiniBatchSparsePCA通过使用一部分样本特征和给定的迭代次数来进行PCA降维，以解决在大样本时特征分解过慢的问题，当然，代价就是PCA降维的精确度可能会降低。使用SparsePCA和MiniBatchSparsePCA需要对L1正则化参数进行调参。


 ### sklearn.decomposition.PCA参数介绍

下面我们主要基于sklearn.decomposition.PCA来讲解如何使用scikit-learn进行PCA降维。PCA类基本不需要调参，一般来说，我们只需要指定我们需要降维到的维度，或者我们希望降维后的主成分的方差和占原始维度所有特征方差和的比例阈值就可以了。

现在我们对sklearn.decomposition.PCA的主要参数做一个介绍：

*   __1）n_components：__
    
    __这个参数可以帮我们指定希望PCA降维后的特征维度数目。__ 最常用的做法是直接指定降维到的维度数目，此时n_components是一个大于等于1的整数。当然，我们也可以指定主成分的方差和所占的最小比例阈值，让PCA类自己去根据样本特征方差来决定降维到的维度数，此时n_components是一个（0，1]之间的数。当然，我们还可以将参数设置为"mle", 此时PCA类会用MLE算法根据特征的方差分布情况自己去选择一定数量的主成分特征来降维。我们也可以用默认值，即不输入n_components，此时n_components=min(样本数，特征数)。

*   __2）whiten ：__
    
    __判断是否进行白化。__ 所谓白化，就是对降维后的数据的每个特征进行归一化，让方差都为1.对于PCA降维本身来说，一般不需要白化。如果你PCA降维后有后续的数据处理动作，可以考虑白化。默认值是False，即不进行白化。

*   __3）svd_solver：__
    
    __即指定奇异值分解SVD的方法，由于特征分解是奇异值分解SVD的一个特例，一般的PCA库都是基于SVD实现的。__ 有4个可以选择的值：{‘auto’, ‘full’, ‘arpack’, ‘randomized’}。randomized一般适用于数据量大，数据维度多同时主成分数目比例又较低的PCA降维，它使用了一些加快SVD的随机算法。 full则是传统意义上的SVD，使用了scipy库对应的实现。arpack和randomized的适用场景类似，区别是randomized使用的是scikit-learn自己的SVD实现，而arpack直接使用了scipy库的sparse SVD实现。默认是auto，即PCA类会自己去在前面讲到的三种算法里面去权衡，选择一个合适的SVD算法来降维。一般来说，使用默认值就够了。

除了这些输入参数外，有两个PCA类的成员值得关注。第一个是 __(explained_variance_)__ ，它 __代表降维后的各主成分的方差值__ 。方差值越大，则说明越是重要的主成分。第二个是 __(explained_variance_ratio_)__，它 __代表降维后的各主成分的方差值占总方差值的比例__，这个比例越大，则越是重要的主成分。


### PCA实例

[完整代码参见刘建平老师的github：]( https://github.com/ljpzzz/machinelearning/blob/master/classic-machine-learning/pca.ipynb)


### 笔记转载自

-《[刘建平老师博客-用scikit-learn学习主成分分析(PCA)](https://www.cnblogs.com/pinard/p/6243025.html)》
