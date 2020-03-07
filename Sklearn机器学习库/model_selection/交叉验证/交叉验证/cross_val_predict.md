# cross_val_predict

__cross_val_predict()__	也使用	K 折交叉验证。

__但它不是返回一个评估分数__ ，而是返回基于每一个测试折做出的一个预测值。

这意味着，对于每一个训练集的样例，你得到一个干净的预测（“干净”是说一个模型在训练过程当中没有用到测试集的数据）。

## 一、简单示例:

    from sklearn.model_selection import cross_val_predict

    y_train_pred = cross_val_predict(sgd_clf,x_train,y_train_5,cv=3)
    y_train_pred

    array([False, False, False, ..., False, False, False])

## 二、使用不同的method:

### 1、decision_function:__ (计算决策分数)

*   __cross_val_predict__ 默认的 method=’predict’ ，当 __cross_val_predict__ 的 method为 __'decision_function'__ 时。可以用于计算 __决策分数__ 。而不是 __预测值__。

*   __注意：__ 
    
    不是 cross_val_predict 可以 decision_function 方法，而是需要模型算法支持 decision_function 方法时才能使用。
        
    比如SGD支持使用 decision_function 这个方法，所以可以 cross_val_predict(sgd_clf,x_train,y_train_5,cv=3) ！

*   __decision_function__ 方法返回每个实例的分数，然后就可以根据这些分数，使用任意阈值进行预测, 可以把每个样例返回的 __分数__ 理解成 __阈值__。

        y_score = cross_val_predict(sgd_clf,x_train,y_train_5,cv=3,method='decision_function')
        y_score

        array([-22250.67613903, -13896.49860594, -29003.73878143, ...,
                -9836.89786869, -55507.90575443,   -703.42888522])

    __适用场景：__ 比如在绘制 [ROC曲线](https://github.com/OneStepAndTwoSteps/Data_Analysis_notes/blob/master/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/ROC%E6%9B%B2%E7%BA%BF%20%E5%92%8C%20PR%E6%9B%B2%E7%BA%BF/roc%E5%92%8Cauc%E6%9B%B2%E7%BA%BF/%E7%BB%98%E5%88%B6ROC%E6%9B%B2%E7%BA%BF.md) 计算fpr和tpr或者计算AUC面积等情况时，都需要用到这个阈值。



### 2、__predict_proba:__ (计算概率)

*   __predict_proba()__	方法返回 一个数组，数组的每一行代表一个样例，每一列代表一个类。数组当中的值的意思是：给定一个样例属于给定类的概率。
    
    __例如：__ 返回的是一个n行k列的数组，第i行第j列上的数值是模型预测第i个预测样本的标签为j的概率。所以每一行的和应该等于1.

*   __案例：__

        from sklearn.ensemble import RandomForestClassifier 

        forest_clf = RandomForestClassifier(random_state=42) 
        y_probas_forest	= cross_val_predict(forest_clf, X_train, y_train_5,	cv=3,method="predict_proba")


*   __注意：__ 如果某个算法不支持计算决策分数 (阈值)，。一个简单的解决方法是使用 __正例__ 的 __概率__ 当作 __样例的分数__。

        # score	= proba	of positive class (二分类，第二列就是预测为正类的概率)
        # 因为是二分类，所以第一列表示 0 负类，第二列表示 1 为正类。
        y_scores_forest	= y_probas_forest[:, 1]	

        array([[1. , 0. ],
               [1. , 0. ],
               [0.8, 0.2],
               ...,
               [1. , 0. ],
               [1. , 0. ],
               [0.9, 0.1]])

        fpr_forest,	tpr_forest,	thresholds_forest = roc_curve(y_train_5,y_scores_forest)

