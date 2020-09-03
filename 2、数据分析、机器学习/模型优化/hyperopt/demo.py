
# https://www.jianshu.com/p/35eed1567463
# https://www.kaggle.com/kabure/extensive-eda-and-modeling-xgb-hyperopt/notebook

from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
import matplotlib.pyplot as plt

################# fmin #################

# best = fmin(
#     fn=lambda x: x,
#     space=hp.uniform('x', 0, 1),
#     algo=tpe.suggest,
#     max_evals=100)
# print(best)

# best = fmin(
#     fn=lambda x: (x)**2,
#     space=hp.uniform('x', -2, 2),
#     algo=tpe.suggest,
#     max_evals=100)
# print(best)

################# 搜索空间 #################

# import hyperopt.pyll.stochastic

# space = {
#     'x': hp.uniform('x', 0, 1),                    # hp.uniform(label, low, high) 其中low和high是范围的下限和上限。          
#     'y': hp.normal('y', 0, 1),                     # hp.normal(label, mu, sigma) 其中mu和sigma分别是均值和标准差。
#     'name': hp.choice('name', ['alice', 'bob']),   # hp.choice(label, options) 其中options应是 python 列表或元组。
# }

# print(hyperopt.pyll.stochastic.sample(space))

################# 通过 Trials 捕获信息 #################

# from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

# fspace = {
#     'x': hp.uniform('x', -5, 5)
# }

# def f(params):
#     x = params['x']
#     val = x**2
#     return {'loss': val, 'status': STATUS_OK}

# trials = Trials()
# best = fmin(fn=f, space=fspace, algo=tpe.suggest, max_evals=50, trials=trials)

# print('best:', best)

# print('trials:')
# for trial in trials.trials[:2]:
#     print(trial)

################# 可视化 #################

# 查看 时间t和x之间的关系
# f, ax = plt.subplots(1)
# xs = [t['tid'] for t in trials.trials]
# ys = [t['misc']['vals']['x'] for t in trials.trials]
# ax.set_xlim(xs[0]-10, xs[-1]+10)
# ax.scatter(xs, ys, s=20, linewidth=0.01, alpha=0.75)
# ax.set_title('$x$ $vs$ $t$ ', fontsize=18)
# ax.set_xlabel('$t$', fontsize=16)
# ax.set_ylabel('$x$', fontsize=16)
# plt.show()

# 查看 loss和x之间的关系

# f, ax = plt.subplots(1)
# xs = [t['misc']['vals']['x'] for t in trials.trials]
# ys = [t['result']['loss'] for t in trials.trials]
# ax.scatter(xs, ys, s=20, linewidth=0.01, alpha=0.75)
# ax.set_title('$val$ $vs$ $x$ ', fontsize=18)
# ax.set_xlabel('$x$', fontsize=16)
# ax.set_ylabel('$val$', fontsize=16)
# plt.show()






# now with scaling as an option
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score 
from sklearn.preprocessing import normalize
from sklearn.preprocessing import scale

iris = datasets.load_iris()
X = iris.data
y = iris.target

def hyperopt_train_test(params):
    X_ = X[:]

    if 'normalize' in params:
        if params['normalize'] == 1:
            X_ = normalize(X_)
            del params['normalize']

    if 'scale' in params:
        if params['scale'] == 1:
            X_ = scale(X_)
            del params['scale']

    clf = KNeighborsClassifier(**params)
    return cross_val_score(clf, X_, y).mean()

space4knn = {
    'n_neighbors': hp.choice('n_neighbors', range(1,50)),
    'scale': hp.choice('scale', [0, 1]),
    'normalize': hp.choice('normalize', [0, 1])
}

def f(params):
    acc = hyperopt_train_test(params)
    return {'loss': -acc, 'status': STATUS_OK}

trials = Trials()
best = fmin(f, space4knn, algo=tpe.suggest, max_evals=100, trials=trials)
print('best:')
print(best)