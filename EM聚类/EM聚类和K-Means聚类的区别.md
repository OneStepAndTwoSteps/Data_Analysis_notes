## EM聚类和K-Means聚类的区别

相比于 K-Means 算法，EM 聚类更加灵活，比如下面这两种情况，K-Means 会得到下面的聚类结果。

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/EM%E8%81%9A%E7%B1%BB/5.png)

因为 K-Means 是通过 __距离来区分样本之间的差别__ 的，且每个样本在计算的时候只能属于一个分类，称之为是 __硬聚类算法。__ 而 EM 聚类在求解的过程中，实际上 __每个样本都有一定的概率和每个聚类相关__ ，叫做 __软聚类算法。__

和 K-Means 一样，我们事先知道聚类的个数，但是不知道每个样本分别属于哪一类。通常，我们可以假设样本是符合高斯分布的（也就是正态分布）。每个高斯分布都属于这个模型的组成部分（component），要分成 K 类就相当于是 K 个组成部分。这样我们可以先初始化每个组成部分的高斯分布的参数，然后再看来每个样本是属于哪个组成部分。这也就是 E 步骤。

再通过得到的这些隐含变量结果，反过来求每个组成部分高斯分布的参数，即 M 步骤。反复 EM 步骤，直到每个组成部分的高斯分布参数不变为止。

这样也就相当于将样本按照 GMM 模型进行了 EM 聚类。

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/EM%E8%81%9A%E7%B1%BB/6.png)

### 总结：
__相似处：__

    1.EM，KMEANS，都是随机生成预期值，然后经过反复调整，获得最佳结果

    2.聚类个数清晰

__不同处：__

    1.EM是计算概率，KMeans是计算距离。

    计算概率，概率只要不为0，都有可能即样本是每一个类别都有可能

    计算距离，只有近的的票高，才有可能，即样本只能属于一个类别
