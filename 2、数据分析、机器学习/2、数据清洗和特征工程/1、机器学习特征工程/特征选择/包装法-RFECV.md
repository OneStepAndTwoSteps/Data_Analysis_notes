## 包装法-RFECV


最常用的包装法是递归消除特征法(recursive feature elimination,以下简称RFE)。递归消除特征法使用一个机器学习模型来进行多轮训练，每轮训练后，消除若干权值系数的对应的特征，再基于新的特征集进行下一轮训练。在sklearn中，可以使用RFE函数来选择特征。

### recursive feature elimination ( RFE )

recursive feature elimination ( RFE )通过学习器返回的 coef_ 属性 或者 feature_importances_ 属性来获得每个特征的重要程度。 然后，从当前的特征集合中移除最不重要的特征。在特征集合上不断的重复递归这个步骤，直到最终达到所需要的特征数量为止。

### RFECV
RFECV通过交叉验证来找到最优的特征数量。如果减少特征会造成性能损失，那么将不会去除任何特征。这个方法用以选取单模型特征相当不错，但是有两个缺陷，一，计算量大。二，随着学习器（评估器）的改变，最佳特征组合也会改变，有些时候会造成不利影响。

#### 导入方法：

    from sklearn.feature_selection import RFE, RFECV

#### 例子
    
    dtree_rfe=feature_selection.RFECV(dtree,step=1,scoring='accuracy',cv=cv_split)
    dtree_rfe.fit(x_train,y_train)

    # get_support 方法可以得到最后我们选择出来的特征(重要的特征会在这个特征的所在位置标志为True，不重要的标志False)
    x_rfe=x_train.columns.values[dtree_rfe.get_support()]

-《[更多使用方法](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html)》
    
  
