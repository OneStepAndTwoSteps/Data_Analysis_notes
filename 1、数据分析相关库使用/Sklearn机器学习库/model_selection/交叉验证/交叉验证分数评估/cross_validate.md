# cross_validate

## 方法

cross_validate(estimator, X, y=None, groups=None, scoring=None, cv=’warn’, n_jobs=None, verbose=0, fit_params=None, pre_dispatch=‘2*n_jobs’, return_train_score=False, return_estimator=False, error_score=’raise-deprecating’)



__如：__ base_results=model_selection.cross_validate(dtree,x_train,y_train,cv=cv_split)

__cross_validate 通过交叉验证评估指标，并记录适合度/得分时间。比如我们可以得到在交叉训练中训练集的模型测试分数，验证集的模型册数分数等__


-《[sklearn - cross_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html)》

### 例子 

`分类：`

    dtree=tree.DecisionTreeClassifier(random_state=0)
    base_results=model_selection.cross_validate(dtree,x_train,y_train,cv=cv_split)
    dtree.fit(x_train,y_train)

    print('BEFORE DT Parameters: ',dtree.get_params())
    print('BEFORE DT Training w/bin score mean: {:.2f}'.format(base_results['train_score'].mean()*100))             # 交叉验证之后的训练集训练分数
    print('BEFORE DT Test w/bin score mean: {:.2f}'.format(base_results['test_score'].mean()*100))                  # 交叉验证之后的验证集验证分数
    print('BEFORE DT Test w/bin score 3*std: +/- {:.2f}'.format(base_results['test_score'].std()*3))
    print('\n')

    param_grid={'criterion':['gini','entropy'],
                'max_depth':[2,4,6,8,10,None],
                'random_state':[0]}

    tune_model=model_selection.GridSearchCV(estimator=dtree,param_grid=param_grid,scoring='roc_auc',cv=cv_split)
    tune_model.fit(x_train,y_train)

    print('AFTER DT Parameters: ',tune_model.best_params_)
    '''[mean_train_score,mean_test_score,std_test_score] 这些键都是在 cv_results_ 中的key，
    通过后面跟[tune_model.best_index_]索引我们可以得到相应key的values'''

    print('AFTER DT Training w/bin score mean: {:.2f}'.format(tune_model.cv_results_['mean_train_score'][tune_model.best_index_]*100))
    print('AFTER DT Test w/bin score mean: {:.2f}'.format(tune_model.cv_results_['mean_test_score'][tune_model.best_index_]*100))
    print('AFTER DT Test w/bin score 3*std: +/- {:.2f}'.format(tune_model.cv_results_['std_test_score'][tune_model.best_index_]*100*3))



