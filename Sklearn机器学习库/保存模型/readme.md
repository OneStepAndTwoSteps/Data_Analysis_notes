### 保存模型

你要保存每个试验过的模型，以便后续可以再用。要确保有超参数和训练参数，以及交叉验证评分，和实际的预测值。这可以让你比较不同类型模型的评分，还可以比较误差种类。

你可以用 Python 的模块 pickle ，非常方便地保存 Scikit-Learn 模型，或使用 sklearn.externals.joblib ，后者序列化大 NumPy 数组更有效率。

__新版的 sklearn 可能会移除 joblib，可以通过直接 pip install joblib 来进行安装。__


    import joblib

    # 保存模型
    joblib.dump(forest_reg,'forest_reg.pk1')
    ['forest_reg.pk1']

    # 重新加载模型
    my_model_loaded = joblib.load('forest_reg.pk1')
    my_model_loaded

    RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
                        max_features='auto', max_leaf_nodes=None,
                        min_impurity_decrease=0.0, min_impurity_split=None,
                        min_samples_leaf=1, min_samples_split=2,
                        min_weight_fraction_leaf=0.0, n_estimators=10,
                        n_jobs=None, oob_score=False, random_state=None,
                        verbose=0, warm_start=False)