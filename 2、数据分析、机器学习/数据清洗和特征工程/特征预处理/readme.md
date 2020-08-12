# 特征预处理

机器学习的模式之一：`特征工程` 比模型构建和超参数调整有更大的投资回报。正如 `Andrew Ng` 喜欢说的：“应用机器学习基本上是特征工程。”

虽然选择正确的模型和最佳设置很重要，但是模型只能从给定的数据中学习。确保这些数据尽可能与任务相关是数据科学家的工作（也许还有一些自动化工具可以帮助我们）。

`特征工程` 指的是一个遗传过程，可以包括特征构造：从现有数据中添加新的特征，以及特征选择：只选择最重要的特征或其他降维方法。我们可以使用许多技术来创建特性和选择特性。

当我们开始使用其他数据源时，我们将进行大量的特征工程，比如我们可以尝试以下两种简单的特征构造方法：

* `Polynomial Features 多项式特征`

* `Domain knowledge features 领域知识特征`


## Polynomial Features

一种简单的特征构造方法称为 `多项式特征`。在该方法中，我们生成的特征是现有特征的幂函数以及现有特征之间的交互项。

例如，我们可以创建变量 `EXT_SOURCE_1的二次方` 和 `EXT_SOURCE_2的二次方`，也可以创建变量 `EXT_SOURCE_1 x EXT_SOURCE_2^2`，`EXT_SOURCE_1^2 x EXT_SOURCE_2^2`，依此类推。这些由多个独立变量组合而成的特征称为 [交互项](https://en.wikipedia.org/wiki/Interaction（统计学）) 因为它们捕捉变量之间的相互作用。换言之，虽然两个变量本身可能不会对目标产生强烈的影响，但将它们组合成一个单独的交互变量可能会显示出与目标的关系。交互项在统计模型中常用来捕捉多个变量的影响，但我不认为它们在机器学习中经常使用。尽管如此，我们可以尝试一些，看看它们是否有助于我们的模型来预测是否会有帮助。


在下面的代码中，我们使用 `EXT_SOURCE` 和 `DAYS_BIRTH` 变量创建多项式特征。`Scikit Learn` 有一个很有用的类，叫做 `PolynomialFeatures` ，它创建多项式和交互项，达到指定的程度。我们可以使用3度来查看结果（当我们创建多项式特征时，我们希望避免使用太高的次数，这既因为 `特征的数量与次数成指数关系` ，也因为我们可能会遇到 `过拟合` 的问题）。


    # 为多项式特征生成一个新的数据帧
    poly_features = app_train[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH', 'TARGET']]
    poly_features_test = app_test[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH']]

    # 用于处理缺失值的填充器
    from sklearn.preprocessing import Imputer
    imputer = Imputer(strategy = 'median')

    poly_target = poly_features['TARGET']

    poly_features = poly_features.drop(columns = ['TARGET'])

    #需要插补缺失值
    poly_features = imputer.fit_transform(poly_features)
    poly_features_test = imputer.transform(poly_features_test)

    from sklearn.preprocessing import PolynomialFeatures
                                    
    # 创建具有指定次数的多项式对象
    poly_transformer = PolynomialFeatures(degree = 3)
