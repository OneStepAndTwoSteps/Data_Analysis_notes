
### Adaboost类的核心参数：

    # 引入Adaboost分类器
    from sklearn.ensemble import AdaBoostClassifier


    # 引入Adaboost回归器
    from sklearn.ensemble import AdaBoostRegressor

### Adaboost分类器：
__AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm=’SAMME.R’, random_state=None) __

__base_estimator：__ 代表的是弱分类器。在 AdaBoost 的分类器和回归器中都有这个参数，在 AdaBoost 中默认使用的是决策树，一般我们不需要修改这个参数，当然你也可以指定具体的分类器。

__n_estimators：__ 算法的最大迭代次数，也是分类器的个数，每一次迭代都会引入一个新的弱分类器来增加原有的分类器的组合能力。默认是 50。

__learning_rate：__ 代表学习率，取值在 0-1 之间，默认是 1.0。如果学习率较小，就需要比较多的迭代次数才能收敛，也就是说学习率和迭代次数是有相关性的。当你调整 learning_rate 的时候，往往也需要调整 n_estimators 这个参数。

__algorithm：__ 代表我们要采用哪种 boosting 算法，一共有两种选择：SAMME 和 SAMME.R。默认是 SAMME.R。这两者之间的区别在于对弱分类权重的计算方式不同。

__random_state：__ 代表随机数种子的设置，默认是 None。随机种子是用来控制随机模式的，当随机种子取了一个值，也就确定了一种随机规则，其他人取这个值可以得到同样的结果。如果不设置随机种子，每次得到的随机数也就不同。

### Adaboost回归：

__AdaBoostRegressor(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm=’linear’, random_state=None) __

回归和分类的参数基本是一致的， __不同点在于回归算法里没有 algorithm 这个参数，但多了一个 loss 参数。__

loss 代表损失函数的设置，一共有 3 种选择，分别为 linear、square 和 exponential，它们的含义分别是线性、平方和指数。 __默认是线性__ 。一般采用线性就可以得到不错的效果。

创建好 AdaBoost 分类器或回归器之后，我们就可以输入训练集对它进行训练。我们使用 fit 函数，传入训练集中的样本特征值 train_X 和结果 train_y，模型会自动拟合。使用 predict 函数进行预测，传入测试集中的样本特征值 test_X，然后就可以得到预测结果。

