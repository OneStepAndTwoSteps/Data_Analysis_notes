'''
scikit-learn基于AdaBoosts算法提供了两个模型：
1.AdaBoostClassifier用于解决分类问题
2.AdaBoostRegressor用于解决回归问题
'''
from sklearn.ensemble import AdaBoostClassifier
 
AdaBoostClassifier(base_estimator=None,
                 n_estimators=50,
                 learning_rate=1.,
                 algorithm='SAMME.R',
                 random_state=None)
'''
参数含义:
1.Base_estimator:object, optional (default=DecisionTreeClassifier)
                基分类器。默认为DecisionTreeClassifier。
                基分类器需要支持带样本权重的学习以及具备classes_和n_classes_属性。
2.n_estimator:integer, optional (default=50)
                整数，默认是50.指定基分类器的数量。
                提升学习过程被终止时基分类器的最大数量。当完美的拟合训练数据了，
                提升算法会提前停止。这时的基本分类器数量小于给定的值
3.learn_rate:float, optional (default=1.).
                学习率。默认是1.
                通过learning_rate缩减每个分类器的贡献。在learning_rate和n_estimators之间需要权衡。
                通常学习率越小，需要的基本分类器就越多，因此在learning_rate和n_estimators之间要有所折中。
                学习率就是下面公式中的v：
                                    F_m(x)=F_m-1(x)+v*alpha_m*G_m(x)
                其中G_m(x)就是第m个基本分类器。aplha_m是第m个基本分类器的系数。
4.algorithm:{'SAMME', 'SAMME.R'}, optional (default='SAMME.R')
            指定所采用的算法。默认为'SAMME.R'。
            标准的AdaBoost算法只适用于二分类问题。SAMME适用于AdaBoost多分类问题
            (1).algorithm='SAMME',采用SAMME离散提升算法。
            (2).algorith='SAMME.R',采用SAMME.R真正的提升算法。如果选择SAMME.R算法，
            基本分类器必须必须支持类别概率的计算。
            (3).SAMME.R算法通常比SAMME收敛得更快，通过较少的提升迭代实现较低的测试误差。
5.random_state:int, RandomState instance or None, optional (default=None)
            (1).如果为整数，则它指定了随机数生成器的种子。
            (2).如果为RandomState实例，则指定了随机数生成器。
            (3).如果为None，则使用默认的随机数生成器。
            
属性：
1.estimators_:list of classifiers.分类器列表。所有训练过的基本分类器。
2.classes_ : array of shape = [n_classes]。类别标签。
3.n_classes_ : int。类别数量。
4.estimator_weights_ : array of floats。数组，存放每个基本分类器的权重。
5.estimator_errors_ : array of floats。数组，存放每个基本分类器的分类误差。
6.feature_importances_ : array of shape = [n_features]
                        每个特征的重要性。
方法：
1.fit():模型训练。
2.predict():模型预测。
3.predict_log_proba():预测的每个样本属于各个类别的概率对数值。
4.predict_proba():预测的每个样本属于各个类别的概率值。
5.staged_predict():预测每一轮迭代后输入样本的预测值。
6.staged_predict_proba():预测每一轮迭代后输入样本属于各个类别的概率值。
'''
 
from sklearn.ensemble import AdaBoostRegressor
 
AdaBoostRegressor(base_estimator=None,
                 n_estimators=50,
                 learning_rate=1.,
                 loss='linear',
                 random_state=None)
 
'''
参数含义:
1.base_estimator：object, optional (default=DecisionTreeRegressor)
                基本分类器。默认是DecisionTreeRegressor
                基分类器需要支持带样本权重的学习。
2.n_estimators:integer, optional (default=50)
                整数，默认是50.指定基分类器的数量。
                提升学习过程被终止时基分类器的最大数量。当完美的拟合训练数据了，
                提升算法会提前停止。这时的基本分类器数量小于给定的值.
3.learning_rate：float, optional (default=1.)
                学习率。默认是1.
                通过learning_rate缩减每个分类器的贡献。在learning_rate和n_estimators之间需要权衡。
                通常学习率越小，需要的基本分类器就越多，因此在learning_rate和n_estimators之间要有所折中。
                学习率就是下面公式中的v：
                                    F_m(x)=F_m-1(x)+v*alpha_m*G_m(x)
                其中G_m(x)就是第m个基本分类器。aplha_m是第m个基本分类器的系数。
4.loss：{'linear', 'square', 'exponential'}, optional (default='linear')
        指定损失函数。
        (1).loss='linear',线性损失函数。
        (2).loss='square',平方损失函数。
        (3).loss='exponential'，指数损失函数。
        (4).在每一轮提升迭代之后，都需要通过损失函数更新权重。
5.random_state：int, RandomState instance or None, optional (default=None)
        (1).如果为整数，则它指定了随机数生成器的种子。
        (2).如果为RandomState实例，则指定了随机数生成器。
        (3).如果为None，则使用默认的随机数生成器。
属性:
1.estimators_:list of classifiers.分类器列表。存放所有训练过的基本回归器。
2.estimator_weights_ : array of floats。数组，存放每个基本回归器的权重。
5.estimator_errors_ : array of floats。数组，存放每个基本回归器的误差。
6.feature_importances_ : array of shape = [n_features]
                        每个特征的重要性。
方法:
1.fit():模型训练。
2.predict():模型预测。
3.staged_predict():预测每一轮迭代后输入样本的预测值。
'''
 
 
 
'''
scikit-learn基于梯度提升树算法提供了两个模型：
GradientBoostingClassifier即GBDT，用于分类问题
GradientBoostingRegressor即GBRT，用于回归问题
'''
 
from sklearn.ensemble import GradientBoostingClassifier
 
GradientBoostingClassifier(loss='deviance', learning_rate=0.1, n_estimators=100,
                 subsample=1.0, criterion='friedman_mse', min_samples_split=2,
                 min_samples_leaf=1, min_weight_fraction_leaf=0.,
                 max_depth=3, min_impurity_decrease=0.,
                 min_impurity_split=None, init=None,
                 random_state=None, max_features=None, verbose=0,
                 max_leaf_nodes=None, warm_start=False,
                 presort='auto')
'''
参数含义:
1.loss:{'deviance', 'exponential'}, optional (default='deviance')
(1).loss='deviance',此时的损失函数与逻辑回归的损失函数相同，为对数损失：L(Y，P(Y|X))=-logP(Y|X).
(2).loss='exponential',损失函数为指数损失函数。
2.learning_rate:float, optional (default=0.1)。默认0.1。
通过learning_rate缩减每个分类器的贡献。在learning_rate和n_estimators之间需要权衡。
通常学习率越小，需要的基本分类器就越多，因此在learning_rate和n_estimators之间要有所折中。
学习率就是下面公式中的v：
                    F_m(x)=F_m-1(x)+v*alpha_m*G_m(x)
其中G_m(x)就是第m个基本分类器。aplha_m是第m个基本分类器的系数。
3.n_estimators:int (default=100)
指定基本决策树的数量。梯度提升对过拟合有很好的鲁棒性，因此该值越大，性能越好。
4.subsample:float, optional (default=1.0).
用于拟合个体基本学习器的样本数量。如果小于1.0，模型将会变成随机梯度提升决策树。
如果subsample<1.0，此时会减少方差，提高偏差
5.criterion；string, optional (default="friedman_mse")
评估节点分裂的质量指标。
6.min_samplses_split：int, float, optional (default=2)
表示分裂一个内部节点需要的最少样本数。
(1).如果为整数，则min_samples_split就是最少样本数。
(2).如果为浮点数(0到1之间)，则每次分裂最少样本数为ceil(min_samples_split * n_samples)
7.min_samples_leaf：int, float, optional (default=1)
叶子节点最少样本数
(1).如果为整数，则min_samples_split就是最少样本数。
(2).如果为浮点数(0到1之间)，则每个叶子节点最少样本数为ceil(min_samples_leaf * n_samples)
8.min_weight_fraction_leaf：float, optional (default=0.)
指定叶子节点中样本的最小权重。
9.max_depth：integer, optional (default=3)
指定每个基本决策树的最大深度。最大深度限制了决策树中的节点数量。
调整这个参数可以获得更好的性能。
10.min_impurity_decrease：float, optional (default=0.)
 如果节点的分裂导致不纯度的减少(分裂后样本比分裂前更加纯净)大于或等于min_impurity_decrease，则分裂该节点。
 个人理解这个参数应该是针对分类问题时才有意义。这里的不纯度应该是指基尼指数。
 回归生成树采用的是平方误差最小化策略。分类生成树采用的是基尼指数最小化策略。
 加权不纯度的减少量计算公式为：
  N_t / N * (impurity - N_t_R / N_t * right_impurity
                    - N_t_L / N_t * left_impurity)
 其中N是样本的总数，N_t是当前节点的样本数，N_t_L是分裂后左子节点的样本数，
 N_t_R是分裂后右子节点的样本数。impurity指当前节点的基尼指数，right_impurity指
 分裂后右子节点的基尼指数。left_impurity指分裂后左子节点的基尼指数。
11.min_impurity_split：树生长过程中早停止的阈值。如果当前节点的不纯度高于阈值，节点将分裂，否则它是叶子节点。
这个参数已经被弃用。用min_impurity_decrease代替了min_impurity_split。
12.init:BaseEstimator, None, optional (default=None)
一个基本分类器对象或者None,该分类器对象用于执行初始的预测。
如果为None，则使用loss.init_estimator.
13.random_state：int, RandomState instance or None, optional (default=None)
(1).如果为整数，则它指定了随机数生成器的种子。
(2).如果为RandomState实例，则指定了随机数生成器。
(3).如果为None，则使用默认的随机数生成器。
14.max_features：int, float, string or None, optional (default=None)
 搜寻最佳划分的时候考虑的特征数量。
(1).如果为整数，每次分裂只考虑max_features个特征。
(2).如果为浮点数(0到1之间)，每次切分只考虑int(max_features * n_features)个特征。
(3).如果为'auto'或者'sqrt',则每次切分只考虑sqrt(n_features)个特征
(4).如果为'log2',则每次切分只考虑log2(n_features)个特征。
(5).如果为None,则每次切分考虑n_features个特征。
(6).如果已经考虑了max_features个特征，但还是没有找到一个有效的切分，那么还会继续寻找
下一个特征，直到找到一个有效的切分为止。
(7).如果max_features < n_features，则会减少方差，增加偏差。
15. verbose:int, default: 0
如果为0则不输出日志信息，如果为1则每隔一段时间打印一次日志信息
16.max_leaf_nodes：int or None, optional (default=None)
指定每颗决策树的叶子节点的最大数量。
(1).如果为None，则叶子节点数量不限。
(2).如果不为None，则max_depth被忽略。
17.warm_start：bool, default: False
当为True时，则继续使用上一次训练的结果，增加更多的estimators来集成。
18.presort：bool or 'auto', optional (default='auto')
在训练过程中，是否预排序数据加速寻找最佳划分。
属性:
1.feature_importances_：数组，给出每个特征的重要性。
2.oob_improvement_ : array, shape = [n_estimators]
数组，给出了每增加一颗基本决策树，在包外估计(即测试集上)的损失函数的改善情况(相对于上一轮迭代)
即损失函数的减少值。
3.train_score_:数组，给出每增加一颗基本决策树，在训练集上的损失函数的值。
4.init:初始预测使用的分类器。
5.estimators_：数组，给出每棵基础决策树。
方法：
1.fit():训练模型
2.predict():模型预测
3.predict_log_proba():数组，预测各个类别的概率对数值。
4.predict_proba()：数组，预测各个类别的概率值。
'''
 
from sklearn.ensemble import GradientBoostingRegressor
GradientBoostingRegressor(loss='ls', learning_rate=0.1, n_estimators=100,
                 subsample=1.0, criterion='friedman_mse', min_samples_split=2,
                 min_samples_leaf=1, min_weight_fraction_leaf=0.,
                 max_depth=3, min_impurity_decrease=0.,
                 min_impurity_split=None, init=None, random_state=None,
                 max_features=None, alpha=0.9, verbose=0, max_leaf_nodes=None,
                 warm_start=False, presort='auto')
 
'''
参数含义:
1.loss：{'ls', 'lad', 'huber', 'quantile'}, optional (default='ls')
指定优化的损失函数。
(1).loss='ls':损失函数是平方损失函数
(2).loss='lad':损失函数为绝对值损失函数
(3).loss='huber'：损失函数是上边两种损失函数的结合。
2.learning_rate : float, optional (default=0.1)
通过learning_rate缩减每个分类器的贡献。在learning_rate和n_estimators之间需要权衡。
通常学习率越小，需要的基本分类器就越多，因此在learning_rate和n_estimators之间要有所折中。
学习率就是下面公式中的v：
                    F_m(x)=F_m-1(x)+v*alpha_m*G_m(x)
其中G_m(x)就是第m个基本分类器。aplha_m是第m个基本分类器的系数。
3.n_estimators : int (default=100)
指定基本决策树的数量。梯度提升对过拟合有很好的鲁棒性，因此该值越大，性能越好。
4.max_depth : integer, optional (default=3)
指定每个基本决策树的最大深度。最大深度限制了决策树中的节点数量。
调整这个参数可以获得更好的性能。
5.criterion : string, optional (default="friedman_mse")
评估节点分裂的质量指标。
6.min_samples_split : int, float, optional (default=2)
表示分裂一个内部节点需要的最少样本数。
(1).如果为整数，则min_samples_split就是最少样本数。
(2).如果为浮点数(0到1之间)，则每次分裂最少样本数为ceil(min_samples_split * n_samples)
7.min_impurity_decrease：float, optional (default=0.)
 如果节点的分裂导致不纯度的减少(分裂后样本比分裂前更加纯净)大于或等于min_impurity_decrease，则分裂该节点。
 个人理解这个参数应该是针对分类问题时才有意义。这里的不纯度应该是指基尼指数。
 回归生成树采用的是平方误差最小化策略。分类生成树采用的是基尼指数最小化策略。
 加权不纯度的减少量计算公式为：
  N_t / N * (impurity - N_t_R / N_t * right_impurity
                    - N_t_L / N_t * left_impurity)
 其中N是样本的总数，N_t是当前节点的样本数，N_t_L是分裂后左子节点的样本数，
 N_t_R是分裂后右子节点的样本数。impurity指当前节点的基尼指数，right_impurity指
 分裂后右子节点的基尼指数。left_impurity指分裂后左子节点的基尼指数。
8.min_impurity_split：树生长过程中早停止的阈值。如果当前节点的不纯度高于阈值，节点将分裂，否则它是叶子节点。
这个参数已经被弃用。用min_impurity_decrease代替了min_impurity_split。
9.init:BaseEstimator, None, optional (default=None)
一个基本分类器对象或者None,该分类器对象用于执行初始的预测。
如果为None，则使用loss.init_estimator.
10.random_state：int, RandomState instance or None, optional (default=None)
(1).如果为整数，则它指定了随机数生成器的种子。
(2).如果为RandomState实例，则指定了随机数生成器。
(3).如果为None，则使用默认的随机数生成器。
11.max_features：int, float, string or None, optional (default=None)
 搜寻最佳划分的时候考虑的特征数量。
(1).如果为整数，每次分裂只考虑max_features个特征。
(2).如果为浮点数(0到1之间)，每次切分只考虑int(max_features * n_features)个特征。
(3).如果为'auto'或者'sqrt',则每次切分只考虑sqrt(n_features)个特征
(4).如果为'log2',则每次切分只考虑log2(n_features)个特征。
(5).如果为None,则每次切分考虑n_features个特征。
(6).如果已经考虑了max_features个特征，但还是没有找到一个有效的切分，那么还会继续寻找
下一个特征，直到找到一个有效的切分为止。
(7).如果max_features < n_features，则会减少方差，增加偏差。
12. verbose:int, default: 0
如果为0则不输出日志信息，如果为1则每隔一段时间打印一次日志信息
13.max_leaf_nodes：int or None, optional (default=None)
指定每颗决策树的叶子节点的最大数量。
(1).如果为None，则叶子节点数量不限。
(2).如果不为None，则max_depth被忽略。
14.warm_start：bool, default: False
当为True时，则继续使用上一次训练的结果，增加更多的estimators来集成。
15.presort：bool or 'auto', optional (default='auto')
在训练过程中，是否预排序数据加速寻找最佳划分。
属性:
1.feature_importances_：数组，给出每个特征的重要性。
2.oob_improvement_ : array, shape = [n_estimators]
数组，给出了每增加一颗基本决策树，在包外估计(即测试集上)的损失函数的改善情况(相对于上一轮迭代)
即损失函数的减少值。
3.train_score_:数组，给出每增加一颗基本决策树，在训练集上的损失函数的值。
4.init:初始预测使用的分类器。
5.estimators_：数组，给出每棵基础决策树。
'''
 
'''
scikit-learn基于随机森林算法提供了两个模型：
1.RandomForestClassifier用于分类问题
2.RandomForestRegressor用于回归问题
'''
from sklearn.ensemble import RandomForestClassifier
 
RandomForestClassifier(n_estimators=10,
                 criterion="gini",
                 max_depth=None,
                 min_samples_split=2,
                 min_samples_leaf=1,
                 min_weight_fraction_leaf=0.,
                 max_features="auto",
                 max_leaf_nodes=None,
                 min_impurity_decrease=0.,
                 min_impurity_split=None,
                 bootstrap=True,
                 oob_score=False,
                 n_jobs=1,
                 random_state=None,
                 verbose=0,
                 warm_start=False,
                 class_weight=None)
'''
随机森林是一种元估计器，它在数据集的各个子样本上拟合多个决策树分类器，
并使用平均法来提高预测精度和控制过拟合。
参数含义：
1.n_estimators:integer, optional (default=10)
随机森林中决策树的数量
2.criterion：string, optional (default="gini")
评估节点分裂的质量指标。支持的标准有基尼指数和信息增益。
3.max_depth:integer or None, optional (default=None)
指定树的最大深度。如果为None，表示树的深度不限。直到所有的叶子节点都是纯净的，即叶子节点
中所有的样本点都属于同一个类别。或者每个叶子节点包含的样本数小于min_samples_split。
4.min_samples_split:int, float, optional (default=2)
表示分裂一个内部节点需要的最少样本数。
(1).如果为整数，则min_samples_split就是最少样本数。
(2).如果为浮点数(0到1之间)，则每次分裂最少样本数为ceil(min_samples_split * n_samples)
5.min_samples_leaf:int, float, optional (default=1)
整数或者浮点数，默认为1。它指定了每个叶子节点包含的最少样本数。
如果为浮点数(0到1之间)，每个叶子节点包含的最少样本数为ceil(min_samples_leaf * n_samples)
6.max_features：int, float, string or None, optional (default="auto")
搜寻最佳划分的时候考虑的特征数量。
(1).如果为整数，每次分裂只考虑max_features个特征。
(2).如果为浮点数(0到1之间)，每次切分只考虑int(max_features * n_features)个特征。
(3).如果为'auto'或者'sqrt',则每次切分只考虑sqrt(n_features)个特征
(4).如果为'log2',则每次切分只考虑log2(n_features)个特征。
(5).如果为None,则每次切分考虑n_features个特征。
(6).如果已经考虑了max_features个特征，但还是没有找到一个有效的切分，那么还会继续寻找
下一个特征，直到找到一个有效的切分为止。
7.max_leaf_nodes:int or None, optional (default=None)
指定每颗决策树的叶子节点的最大数量。
(1).如果为None，则叶子节点数量不限。
(2).如果不为None，则max_depth被忽略。
8.min_impurity_decrease:float, optional (default=0.)
如果节点的分裂导致不纯度的减少(分裂后样本比分裂前更加纯净)大于或等于min_impurity_decrease，则分裂该节点。
加权不纯度的减少量计算公式为：
  N_t / N * (impurity - N_t_R / N_t * right_impurity
                    - N_t_L / N_t * left_impurity)
其中N是样本的总数，N_t是当前节点的样本数，N_t_L是分裂后左子节点的样本数，
N_t_R是分裂后右子节点的样本数。impurity指当前节点的基尼指数，right_impurity指
分裂后右子节点的基尼指数。left_impurity指分裂后左子节点的基尼指数。
9.min_impurity_split:树生长过程中早停止的阈值。如果当前节点的不纯度高于阈值，节点将分裂，否则它是叶子节点。
这个参数已经被弃用。用min_impurity_decrease代替了min_impurity_split。
10.bootstrap：boolean, optional (default=True)
建立决策树时是否采用自助采样
11.oob_score:bool (default=False)
是否使用包外样本来估计泛化精度.
12.n_jobs:integer, optional (default=1)
指定并行运行的任务数。如果为-1，任务数与CPU核数相同。
13.verbose：int, optional (default=0)
控制决策树构建过程的详细程度。
如果为0则不输出日志信息，如果为1则每隔一段时间打印一次日志信息
14.class_weight: dict, list of dicts, "balanced"
(1).如果是一个字典，则字典给出了每个分类的权重，{class_label: weight}
(2).如果为‘balanced’,则每个分类的权重与该分类在样本集中出现的频率成反比。
(3).如果为‘balanced_subsample’,则样本集为自助采样法产生的决策树的训练数据集，
每个分类的权重与该分类在采用生成的样本集中出现的频率成反比。
(4).如果为None，则每个分类的权重都为1.
属性:
1.estimators_ : list of DecisionTreeClassifier
 决策树分类器列表，存放所有训练过的决策树。
2.classes_ : array of shape = [n_classes] or a list of such arrays
类别标签
3.n_classes_ : int or list
类别数量
4.n_features_ : int
训练时使用的特征数量
5.n_outputs_ : int
训练时输出的数量
6.feature_importances_ : array of shape = [n_features]
特征重要性
7.oob_score_ : float
训练数据使用包外估计时的得分
方法：
1.fit():训练模型
2.predict():预测
3.predict_log_proba()：预测属于各个类别的概率对数值
4.predict_proba():预测属于各个类别的概率值。
'''
 
from sklearn.ensemble import RandomForestRegressor
 
RandomForestRegressor(n_estimators=10,
                 criterion="mse",
                 max_depth=None,
                 min_samples_split=2,
                 min_samples_leaf=1,
                 min_weight_fraction_leaf=0.,
                 max_features="auto",
                 max_leaf_nodes=None,
                 min_impurity_decrease=0.,
                 min_impurity_split=None,
                 bootstrap=True,
                 oob_score=False,
                 n_jobs=1,
                 random_state=None,
                 verbose=0,
                 warm_start=False)
'''
参数含义：
1.n_estimators:integer, optional (default=10)
随机森林中决策树的数量
2.criterion : string, optional (default="mse")
评估节点分裂的质量指标。支持的标准有MSE和MAE。
3.max_depth:integer or None, optional (default=None)
指定树的最大深度。如果为None，表示树的深度不限。直到所有的叶子节点都是纯净的，即叶子节点
中所有的样本点都属于同一个类别。或者每个叶子节点包含的样本数小于min_samples_split。
4.min_samples_split:int, float, optional (default=2)
表示分裂一个内部节点需要的最少样本数。
(1).如果为整数，则min_samples_split就是最少样本数。
(2).如果为浮点数(0到1之间)，则每次分裂最少样本数为ceil(min_samples_split * n_samples)
5.min_samples_leaf:int, float, optional (default=1)
整数或者浮点数，默认为1。它指定了每个叶子节点包含的最少样本数。
如果为浮点数(0到1之间)，每个叶子节点包含的最少样本数为ceil(min_samples_leaf * n_samples)
6.max_features：int, float, string or None, optional (default="auto")
搜寻最佳划分的时候考虑的特征数量。
(1).如果为整数，每次分裂只考虑max_features个特征。
(2).如果为浮点数(0到1之间)，每次切分只考虑int(max_features * n_features)个特征。
(3).如果为'auto'或者'sqrt',则每次切分只考虑sqrt(n_features)个特征
(4).如果为'log2',则每次切分只考虑log2(n_features)个特征。
(5).如果为None,则每次切分考虑n_features个特征。
(6).如果已经考虑了max_features个特征，但还是没有找到一个有效的切分，那么还会继续寻找
下一个特征，直到找到一个有效的切分为止。
7.max_leaf_nodes:int or None, optional (default=None)
指定每颗决策树的叶子节点的最大数量。
(1).如果为None，则叶子节点数量不限。
(2).如果不为None，则max_depth被忽略。
8.min_impurity_decrease:float, optional (default=0.)
如果节点的分裂导致不纯度的减少(分裂后样本比分裂前更加纯净)大于或等于min_impurity_decrease，则分裂该节点。
加权不纯度的减少量计算公式为：
  N_t / N * (impurity - N_t_R / N_t * right_impurity
                    - N_t_L / N_t * left_impurity)
其中N是样本的总数，N_t是当前节点的样本数，N_t_L是分裂后左子节点的样本数，
N_t_R是分裂后右子节点的样本数。impurity指当前节点的基尼指数，right_impurity指
分裂后右子节点的基尼指数。left_impurity指分裂后左子节点的基尼指数。
9.min_impurity_split:树生长过程中早停止的阈值。如果当前节点的不纯度高于阈值，节点将分裂，否则它是叶子节点。
这个参数已经被弃用。用min_impurity_decrease代替了min_impurity_split。
10.bootstrap：boolean, optional (default=True)
建立决策树时是否采用自助采样
11.oob_score:bool (default=False)
是否使用包外样本来估计泛化精度.
12.n_jobs:integer, optional (default=1)
指定并行运行的任务数。如果为-1，任务数与CPU核数相同。
13.verbose：int, optional (default=0)
控制决策树构建过程的详细程度。
如果为0则不输出日志信息，如果为1则每隔一段时间打印一次日志信息
属性:
1.estimators_ : list of DecisionTreeRegressor
 回归决策树列表，存放所有训练过的决策树。
2.n_features_ : int
训练时使用的特征数量
3.n_outputs_ : int
训练时输出的数量
4.feature_importances_ : array of shape = [n_features]
特征重要性
5.oob_score_ : float
训练数据使用包外估计时的得分
6.ob_prediction_ : array of shape = [n_samples]
在训练集上使用包外估计时的预测值。
方法：
1.fit():训练模型
2.predict():预测
Notes：
控制树大小的参数的默认值（例如``max_depth``，``min_samples_leaf``等）导致完全成长和未剪枝的树，
这些树在某些数据集上可能表现很好。为减少内存消耗，应通过设置这些参数值来控制树的复杂度和大小。
'''

