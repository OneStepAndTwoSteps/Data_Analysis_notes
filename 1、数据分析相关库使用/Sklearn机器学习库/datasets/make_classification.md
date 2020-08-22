## make_classification

* `make_classification` 可以用于生成数据：

        from sklearn.datasets import make_classification


案例：


    X, y = make_classification(
    n_classes=2, class_sep=1.5, weights=[0.9, 0.1],
    n_informative=3, n_redundant=1, flip_y=0,
    n_features=20, n_clusters_per_class=1,
    n_samples=100, random_state=10)
                

参数介绍：

* `n_samples`=100,                      生成样本数量

* `class_sep=1.0`,                      难易度：超立方体大小乘以的因子。较大的值分散了群集/类，并使分类任务更加容易。

* `weights=None`,                       列表类型，权重比             

* `n_informative`,                      有价值的重要特征

* `n_features`,                         特征个数= n_informative（） + n_redundant + n_repeated


* `n_redundant`,                        就是把n_informative进行线性组合的特征

* `n_repeated`,                         随机挑选的n_informative和n_redundant的特征数

* `n_classes`,                          分类类别

* `n_clusters_per_class`=2,             每个类的簇数


* `flip_y=0.01`,                        随机分配类别的样本的比例。


* `hypercube=True,shift=0.0, scale=1.0`,                      

* `shuffle=True`,                       随机排列示例和功能。

* `random_state=None `              随机种子




