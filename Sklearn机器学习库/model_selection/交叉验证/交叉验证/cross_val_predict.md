## cross_val_predict

__cross_val_predict()__	也使用	K 折交叉验证。

__但它不是返回一个评估分数__ ，而是返回基于每一个测试折做出的一个预测值。

这意味着，对于每一个训练集的样例，你得到一个干净的预测（“干净”是说一个模型在训练过程当中没有用到测试集的数据）。

#### example:

    from sklearn.model_selection import cross_val_predict

    y_train_pred = cross_val_predict(sgd_clf,x_train,y_train_5,cv=3)
    y_train_pred

    array([False, False, False, ..., False, False, False])

### method: decision_function

__cross_val_predict__ 默认的 method=’predict’ ，当 __cross_val_predict__ 的 method为 __'decision_function'__ 时。可以用于计算 __决策分数__ 。而不是 __预测值__。

__注意：__ 不是 cross_val_predict 可以 decision_function 方法，而是需要模型算法支持 decision_function 方法时才能使用！

__decision_function__ 方法返回每个实例的分数，然后就可以根据这些分数，使用任意阈值进行预测, __可以把每个样例返回的分数理解成阈值__。


    y_score = cross_val_predict(sgd_clf,x_train,y_train_5,cv=3,method='decision_function')
    y_score

    array([-22250.67613903, -13896.49860594, -29003.73878143, ...,
            -9836.89786869, -55507.90575443,   -703.42888522])

__适用场景：__ 比如在绘制ROC曲线计算fpr和tpr或者计算AUC面积等情况时，都需要用到这个阈值。



