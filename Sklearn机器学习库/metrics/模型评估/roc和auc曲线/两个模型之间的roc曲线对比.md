## 两个模型之间的roc曲线对比

接下来展示如何在一张图中绘制两个模型的roc曲线

### 例子

接下来我们使用 逻辑回归模型 和 支持向量机 这两个模型进行roc曲线的绘制，对比模型之间的优劣

__定义 LogisticRegression__

    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import mean_absolute_error, accuracy_score

    ## call on the model object
    logreg = LogisticRegression(solver='liblinear')

    ## fit the model with "train_x" and "train_y"
    logreg.fit(X_train,y_train)

    ## Once the model is trained we want to find out how well the model is performing, so we test the model. 
    ## we use "test_x" portion of the data(this data was not used to fit the model) to predict model outcome. 
    y_pred = logreg.predict(X_test)

    ## Once predicted we save that outcome in "y_pred" variable.
    ## Then we compare the predicted value( "y_pred") and actual value("test_y") to see how well our model is performing. 

    print ("So, Our accuracy Score is: {}".format(round(accuracy_score(y_pred, y_test),4)))


__定义 SVC__

    from sklearn.svm import SVC

    svm=SVC(C=2, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
    max_iter=-1, probability=True, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

    svm.fit(X_train,y_train)


__在 logisticregression 和 SVC 中有有一个方法 .decision_function 可以帮助我们查看各个样本的预测分数。__


#### 现在我们已经知道了如何获得分数，那么我们开始绘制 ROC 曲线

    from sklearn.metrics import roc_curve, auc
    #plt.style.use('seaborn-pastel')
    y_score = logreg.decision_function(X_test)
    svm_y_score=svm.decision_function(X_test)

    FPR, TPR, _ = roc_curve(y_test, y_score)
    FPR2, TPR2, _ = roc_curve(y_test, svm_y_score)

    # 打印AUC的面积
    ROC_AUC = auc(FPR, TPR)
    print ('Logistic AUC: ',ROC_AUC)

    # 打印AUC的面积
    ROC_AUC2 = auc(FPR2, TPR2)
    print ('SVM AUC : ',ROC_AUC2)

    plt.figure(figsize =[11,9])
    plt.plot(FPR, TPR, label= 'ROC curve(area = %0.2f)'%ROC_AUC, linewidth= 4)
    plt.plot(FPR2, TPR2, label= 'ROC curve(area = %0.2f)'%ROC_AUC, linewidth= 4)

    plt.plot([0,1],[0,1], 'k--', linewidth = 4)
    plt.xlim([0.0,1.0])
    plt.ylim([0.0,1.05])
    plt.xlabel('False Positive Rate', fontsize = 18)
    plt.ylabel('True Positive Rate', fontsize = 18)
    plt.title('ROC for Titanic survivors', fontsize= 18)

    # 加上legend方法才会显示图例
    plt.legend(loc="lower right",fontsize=16)

    plt.show()


#### 展示图


<div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/Sklearn%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%BA%93/static/metrics/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0/roc%E6%9B%B2%E7%BA%BF/roc5-1.png"/></div>




从展示图中我们可以看到 SVM 的 AUC面积比 logisticregression 的 AUC面积更大，看起来svm模型更好一些。