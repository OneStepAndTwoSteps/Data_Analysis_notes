# sklearn.model_selection模块常用函数和类


    1. train_test_split()	        # 训练集和测试集划分

    2. KFold()	                    # k折交叉验证

    3. GridSearchCV()	            # 网格搜索，寻找模型最优参数

    4. cross_val_score()	cross_validate()    # 通过交叉验证评估指标，并记录适合度/得分时间。

    5. StratifiedKFold()	        # 分层K-Folds交叉验证器

    6. ShuffleSplit()	            # 随机置换交叉验证器 注意：与其他交叉验证策略相反，随机拆分并不能保证所有折叠都不同，尽管这对于相当大的数据集来说仍然很可能。

    7. StratifiedShuffleSplit()	

    8. RandomizedSearchCV()	

    9. cross_val_predict()	

    10. ParameterGrid()	

    11. learning_curve()	

    12. ParameterSampler()	

    13. validation_curve()	

    14. LeaveOneOut()	            # 留一交叉验证

    15. check_cv()	

    16. GroupKFold()	          

