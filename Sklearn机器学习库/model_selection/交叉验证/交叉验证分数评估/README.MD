## cross_validate和cross_val_score

最简单的使用交叉验证的方法是cross_val_score函数

    >>> import numpy as np
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn import datasets
    >>> from sklearn import svm
    >>> from sklearn.model_selection import cross_val_score

    >>> iris = datasets.load_iris()
    >>> clf = svm.SVC(kernel='linear', C=1)
    >>> scores = cross_val_score(clf, iris.data, iris.target, cv=5)
    >>> scores                                              
    array([0.96..., 1.  ..., 0.96..., 0.96..., 1.        ])

    >>> print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    Accuracy: 0.98 (+/- 0.03)

__cross_validate和cross_val_score的不同之处在于：__

    1、评估的时候可以选择多个指标
    2、返回一个包含测试分数、拟合时间、打分时间（以及可选择的训练分数和拟合的模型）的字典。

__cross_validate案例：__

    MLA_columns=['MLA Name', 'MLA Parameters','MLA Train Accuracy Mean', 'MLA Test Accuracy Mean', 'MLA Test Accuracy 3*STD' ,'MLA Time']
    MLA_compare=pd.DataFrame(columns=MLA_columns)

    # 1、之前这里没有加deepcopy，在 MLA_predict[MLA_name]=alg.predict(x_train) 
    # 这步中直接修改了 y_train的数据，因为之前我们的y_train也是等于train_data['Survived']
    
    # 2、train_data[['Survived']] 和 train_data['Survived'] 输出的结果是不同的，
    # type(train_data[['Survived']].head())是df，type(train_data['Survived'].head())是serise

    MLA_predict=train_data[['Survived']].copy(deep=True)


    for row_index,alg in enumerate(MLA):
    #     print('row_index: ',row_index)
        MLA_name=alg.__class__.__name__
        MLA_compare.loc[row_index,'MLA Name']=MLA_name
        ''' alg.get_params() type 是一個字典 我们将其转化为str，df行中中不能直接存储dict，字典中的每一个k,v会存储一行'''
        MLA_compare.loc[row_index,'MLA Parameters']=str(alg.get_params())
        cv_result=model_selection.cross_validate(alg,x_train,y_train,cv=cv_split)
        MLA_compare.loc[row_index,'MLA Train Accuracy Mean']=cv_result['train_score'].mean()
    #     print(cv_result['test_score'])
        MLA_compare.loc[row_index,'MLA Test Accuracy Mean']=cv_result['test_score'].mean()    
        MLA_compare.loc[row_index,'MLA Test Accuracy 3*STD']=cv_result['test_score'].std()*3   
        MLA_compare.loc[row_index,'MLA Time']=cv_result['fit_time'].mean()
        
        alg.fit(x_train,y_train)
        # 因为这样我们要新建一列模型预测的数据，所以我们必须要在上面的train_data[['Survived']] 中记得这是一个双括号，
        # 否则那么我们就是在series中拼接,其实是拼不进去的
        MLA_predict[MLA_name]=alg.predict(x_train)

    MLA_compare.sort_values(by='MLA Test Accuracy Mean',ascending=False,inplace=True)
    MLA_compare
