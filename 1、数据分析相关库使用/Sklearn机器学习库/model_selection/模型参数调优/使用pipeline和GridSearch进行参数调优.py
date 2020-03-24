#author py chen

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# 创建随机森林模型
rf=RandomForestClassifier()

# 加载数据
data=load_iris()

# 定义参数调优的范围,randomforestclassifier__n_estimators __前面定义的是名字，后面定义的内容是参数
parameters={"randomforestclassifier__n_estimators":range(1,11),
            "randomforestclassifier__max_depth":range(1,5)}


# 定义pipeline 流水线
pipeline=Pipeline([
    ('scaler',StandardScaler()),
    ('randomforestclassifier',rf)
])

# 使用GridSearchCV 进行参数调优
clf=GridSearchCV(estimator=pipeline,param_grid=parameters,cv=6)

# 进行数据集分类
clf.fit(data.data,data.target)

# 打印最优分数 给出不同参数情况下的评价结果
print("最优分数：%.4lf"%clf.best_score_)
# 打印最优参数 描述了已取得最佳结果的参数的组合
print("最优参数：%s"%clf.best_params_)

# 我们在进行参数调优时，如果计算出来最优参数会发生变化，我们可以查看他的最优分数，如果最优分数相差不大，那表示我们的参数结果也相差不大，那我们选择其中一个即可
