## SGDRegressor

随机梯度下降回归

__例子：__

    sgd_reg2 = SGDRegressor(penalty=None,warm_start=True,learning_rate='constant',eta0=0.005)

__参数：__

    penalty：
        
        指明惩罚项，比如 l2 正则化

    warm_start:	

        warm_start=True	时，调用	fit()	方法后，训练会从停下来的地方继续，而不是从头 重新开始。

    learning_rate：
        
        指明学习率的状态 constant 表示学习率固定不变为 eta0 指定的大小。

    eta0: 
        
        学习率大小

