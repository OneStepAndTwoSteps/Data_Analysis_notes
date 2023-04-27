### 绘制PR曲线

需要知道 Precision 和 recall 。

*   __获取决策分数。__

    通过 __cross_val_predict__ 的 __method='decision_function'__ ，可以得到所有样例的 __决策分数__。

        y_score = cross_val_predict(sgd_clf,x_train,y_train_5,cv=3,method='decision_function')
        y_score

*   __获取 准确率 和 召回率。__


    通过这些分数值。对于任何可能的阈值，使用 __precision_recall_curve()__ ,你都可以计算 __准确率__ 和 __召回率__。

        precision,recall,threshold = precision_recall_curve(y_train_5,y_score)

#### 绘制PR曲线

    def plot_pr(precision,recall):
        plt.plot(recall,precision,'b')
        plt.axis([0,1,0,1])
        plt.xlabel('precision')
        plt.ylabel('recall')    

    plot_pr(precision,recall)
