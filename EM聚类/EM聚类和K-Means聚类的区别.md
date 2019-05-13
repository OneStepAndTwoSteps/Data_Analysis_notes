## EM聚类和K-Means聚类的区别

相比于 K-Means 算法，EM 聚类更加灵活，比如下面这两种情况，K-Means 会得到下面的聚类结果。

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/EM%E8%81%9A%E7%B1%BB/5.png)

因为 K-Means 是通过 __距离来区分样本之间的差别__ 的，且每个样本在计算的时候只能属于一个分类，称之为是 __硬聚类算法。__而 EM 聚类在求解的过程中，实际上 __每个样本都有一定的概率和每个聚类相关__ ，叫做 __软聚类算法。__





