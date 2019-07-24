#author py chen

from sklearn.ensemble import RandomForestClassifier       
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
# 创建随机森林模型
rf = RandomForestClassifier()

# 设置需要调优的参数和其范围，GridSearchCV会帮助我们在范围中找到最优值
parameters = {"n_estimators": range(1,11)}

# 加载数据集
iris = load_iris()

# 使用 GridSearchCV 进行参数调优
clf = GridSearchCV(estimator=rf, param_grid=parameters)

# 对 iris 数据集进行分类
clf.fit(iris.data, iris.target)

 # 提供优化过程期间观察到的最好的评分
print(" 最优分数： %.4lf" %clf.best_score_)

# best_params_：描述了已取得最佳结果的参数的组合
print(" 最优参数：", clf.best_params_)

运行结果如下：
最优分数： 0.9667
最优参数： {'n_estimators': 6}

# 该链接有相同的案例
https://github.com/OneStepAndTwoSteps/data_mining_analysis/blob/master/%E5%86%B3%E7%AD%96%E6%A0%91/%E5%86%B3%E7%AD%96%E6%A0%91demo.ipynb
