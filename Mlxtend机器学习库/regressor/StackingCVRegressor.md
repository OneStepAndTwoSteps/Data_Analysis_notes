# StackingCVRegressor

在 Mlxtend中有一個 StackingCVRegressor 方法可以幫助我們進行堆叠

#### 导入包

    from mlxtend.regressor import StackingCVRegressor

## who is StackingCVRegressor?

堆叠是一种集成学习技术，通过元回归器组合多个回归模型。在StackingCVRegressor扩展了标准堆叠算法（如实施StackingRegressor使用失倍预测为2级回归准备输入的数据）。

在标准堆叠程序中，第一级回归器适合于用于准备第二级回归器的输入的相同训练集，这可能导致过度拟合。的StackingCVRegressor，然而，使用失倍预测的概念：数据集被划分成k倍，和在K个连续几轮，k-1个褶皱用于拟合第一级回归。在每一轮中，然后将第一级回归量应用于在每次迭代中未用于模型拟合的剩余1个子集。然后将得到的预测堆叠起来并作为输入数据提供给二级回归量。在训练之后StackingCVRegressor，第一级回归量适合整个数据集以获得最佳预测。



## API

    StackingCVRegressor(regressors, meta_regressor, cv=5, shuffle=True, random_state=None, verbose=0, refit=True, 
    use_features_in_secondary=False, store_train_meta_features=False, n_jobs=None, pre_dispatch='2n_jobs')

### 参数说明


*   regressors : array-like, shape = [n_regressors]

    回归列表。调用fit方法StackingCVRegressor将适合将存储在class属性中的这些原始回归量的克隆self.regr_。

*   meta_regressor : object
元回归器将安装在回归器的整体上

*   cv : int, 交叉验证生成器或可迭代，可选（默认值：5）
确定交叉验证拆分策略。cv的可能输入是： - None，使用默认的5倍交叉验证， - integer，指定a中的折叠数KFold， - 用作交叉验证生成器的对象。 - 可迭代的屈服列车，测试分裂。对于整数/无输入，它将使用KFold交叉验证

*   shuffle : bool (default: True)
如果为True，并且cv参数为整数，则训练数据将在交叉验证之前的拟合阶段进行混洗。如果cv 参数是特定的交叉验证技术，则省略该参数。

*   random_state : int, 随机种子
控制cv分离器的随机性。当cv为整数时使用shuffle=True。v0.16.0中的新功能。

*   verbose : int, optional (default=0)
控制建筑过程的详细程度。v0.16.0中的新功能

*   refit : bool (default: True)
如果为True（默认），则克隆用于堆叠回归的回归量，或者使用原始值，在调用fit方法时将对数据集进行重新设置。如果您正在使用支持scikit-learn fit / predict API接口但与scikit-learn clone函数不兼容的估算器，则建议设置refit = False 。

*   use_features_in_secondary : bool (default: False)
如果为True，则元回归量将在原始回归量和原始数据集的预测上进行训练。如果为假，则元回归量将仅针对原始回归量的预测进行训练。

*   store_train_meta_features : bool (default: False)
如果为True，则从用于拟合存储在self.train_meta_features_数组中的元回归量的训练数据计算的元特征，其可以在调用之后被访问fit。

*   n_jobs : int or None, optional (default=None)
用于执行计算的CPU数。 None除非在：obj：joblib.parallel_backendcontext中，否则表示1 。 -1表示使用所有处理器。请参阅：术语：Glossary <n_jobs> 了解更多详情。 New in v0.16.0.

*   pre_dispatch : int, or string, optional
控制在并行执行期间调度的作业数。减少此数量可有助于避免在分配的作业多于CPU可处理的内容时消耗内存消耗。此参数可以是： - 无，在这种情况下，立即创建和生成所有作业。将此用于轻量级和快速运行的作业，以避免由于按需生成作业而导致的延迟 - 一个int，给出生成的总作业的确切数量 - 一个字符串，给出一个表达式作为n_jobs的函数，如在'2 * n_jobs'v0.16.0中的新功能。


### 属性

*   train_meta_features ：numpy数组，shape = [n_samples，n_regressors]
用于训练数据的元特征，其中n_samples是训练数据中的样本数，len（self.regressors）是回归量的数量。


## 方法


#### fit（X，y，groups = None，sample_weight = None）

适合的集合回归量和元回归量。


### 参数

*   X ：numpy数组，shape = [n_samples，n_features]
训练向量，其中n_samples是样本数，n_​​features是要素数。

*   y ：numpy数组，shape = [n_samples]
目标值。

*   groups ：numpy数组/无，shape = [n_samples]
每个样本所属的组。这由特定折叠策略使用，例如GroupKFold（）

*   sample_weight ：array-like，shape = [n_samples]，可选
样本权重作为sample_weights传递给回归量列表中的每个回归量以及meta_regressor。如果某个回归程序在fit（）方法中不支持sample_weight，则会引发错误。

### 返回

- self ：对象


#### fit_transform（X，y = None，fit_params）

适合数据，然后转换它。

使用可选参数fit_params使变换器适合X和y，并返回X的变换版本。

### 参数

*   X ：numpy数组形状[n_samples，n_features]
训练集。

*   y ：numpy数组形状[n_samples]
目标值。

### 返回

*   X_new ：numpy数组形状[n_samples，n_features_new]
变形阵列。


#### get_params（深=真）

获取此估算工具的参数。

### 参数

*   deep ：布尔值，可选
如果为True，将返回此估计器的参数并包含作为估算器的子对象。

### 返回

*   params ：将字符串映射到任何字符串
映射到其值的参数名称。

#### predict（X）

预测X的目标值。

### 参数

*   X ：{array-like，sparse matrix}，shape = [n_samples，n_features]
训练向量，其中n_samples是样本数，n_​​features是要素数。

### 返回

*   y_target ：array-like，shape = [n_samples]或[n_samples，n_targets]
预测目标值。

#### predict_meta_features（X）

获取测试数据的元功能。

### 参数


*   X ：numpy数组，shape = [n_samples，n_features]
测试向量，其中n_samples是样本数，n_​​features是特征数。

### 返回

*   meta-features ：numpy数组，shape = [n_samples，len（self.regressors）]
测试数据的元特征，其中n_samples是测试数据中的样本数，len（self.regressors）是回归量的数量。


#### score（X，y，sample_weight =无）

返回预测的确定系数R ^ 2。

系数R ^ 2定义为（1-u / v），其中u是残差平方和（（y_true-y_pred）2）.sum（）和v是平方和的总和（（y_true-y_true。 mean（）） 2）.sum（）。

最好的分数是1.0，它可能是负的（因为

模型可以任意恶化）。总是预测y的期望值的常数模型，忽略输入特征，将得到R ^ 2得分为0.0。

### 参数

*   X ：array-like，shape =（n_samples，n_features）
测试样品。对于一些估计器，这可以是预先计算的核矩阵，而是shape =（n_samples，n_samples_fitted），其中n_samples_fitted是在估计器的拟合中使用的样本的数量。

*   y ：array-like，shape =（n_samples）或（n_samples，n_outputs）
X的真值。

*   sample_weight ：array-like，shape = [n_samples]，可选
样品重量。

### 返回

*   score ：漂浮
自我预测（X）的R ^ 2。年。

*   set_params（params）
设置此估算器的参数。
可以使用列出有效的参数键get_params()。

### 返回

self



## 例子 GridSearchCV + StackingCVRegressor


    from mlxtend.regressor import StackingCVRegressor
    from sklearn.datasets import load_boston
    from sklearn.linear_model import Lasso
    from sklearn.linear_model import Ridge
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import GridSearchCV

    X, y = load_boston(return_X_y=True)

    ridge = Ridge(random_state=RANDOM_SEED)
    lasso = Lasso(random_state=RANDOM_SEED)
    rf = RandomForestRegressor(random_state=RANDOM_SEED)

    stack = StackingCVRegressor(regressors=(lasso, ridge),
                                meta_regressor=rf, 
                                random_state=RANDOM_SEED,
                                use_features_in_secondary=True)

    params = {'lasso__alpha': [0.1, 1.0, 10.0],
            'ridge__alpha': [0.1, 1.0, 10.0]}

    grid = GridSearchCV(
        estimator=stack, 
        param_grid={
            'lasso__alpha': [x/5.0 for x in range(1, 10)],
            'ridge__alpha': [x/20.0 for x in range(1, 10)],
            'meta_regressor__n_estimators': [10, 100]
        }, 
        cv=5,
        refit=True
    )

    grid.fit(X, y)

    print("Best: %f using %s" % (grid.best_score_, grid.best_params_))

__out__


    Best: 0.679576 using {'lasso__alpha': 1.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.4}


    /Users/guq/miniconda3/envs/python3/lib/python3.7/site-packages/sklearn/model_selection/_search.py:841: DeprecationWarning: The default of the `iid` parameter will change from True to False in version 0.22 and will be removed in 0.24. This will change numeric results when test-set sizes are unequal.
    DeprecationWarning)


__add code__

    cv_keys = ('mean_test_score', 'std_test_score', 'params')

    for r, _ in enumerate(grid.cv_results_['mean_test_score']):
        print("%0.3f +/- %0.2f %r"
            % (grid.cv_results_[cv_keys[0]][r],
                grid.cv_results_[cv_keys[1]][r] / 2.0,
                grid.cv_results_[cv_keys[2]][r]))
        if r > 10:
            break
    print('...')

    print('Best parameters: %s' % grid.best_params_)
    print('Accuracy: %.2f' % grid.best_score_)


__out__


    0.637 +/- 0.09 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.05}
    0.656 +/- 0.08 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.1}
    0.635 +/- 0.09 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.15}
    0.647 +/- 0.08 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.2}
    0.630 +/- 0.09 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.25}
    0.628 +/- 0.09 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.3}
    0.639 +/- 0.09 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.35}
    0.641 +/- 0.09 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.4}
    0.653 +/- 0.08 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.45}
    0.644 +/- 0.09 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 100, 'ridge__alpha': 0.05}
    0.642 +/- 0.09 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 100, 'ridge__alpha': 0.1}
    0.646 +/- 0.09 {'lasso__alpha': 0.2, 'meta_regressor__n_estimators': 100, 'ridge__alpha': 0.15}
    ...
    Best parameters: {'lasso__alpha': 1.2, 'meta_regressor__n_estimators': 10, 'ridge__alpha': 0.4}
    Accuracy: 0.68






