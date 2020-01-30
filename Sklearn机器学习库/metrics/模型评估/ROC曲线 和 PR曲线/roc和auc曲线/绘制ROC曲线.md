### 绘制ROC曲线

首先需要计算出 __FPR__ 和 __TPR__ ，可以借用 __roc_curve__ 函数。

但是在此之前，我们还需要计算出所有样例的阈值 借用 __cross_val_predict()__ 函数指定 __method = 'dicision_function'__ 。

    from sklearn.metrics import roc_curve

    fpr,tpr,threshold = roc_curve(y_train_5,y_score)


### 绘制图像

    def precision_recall_vs_threshold(precision,recall,threshold):
        plt.plot(threshold,precision[:-1],'b--',label='precision')
        plt.plot(threshold,recall[:-1],'g--',label='recall')
        plt.legend(loc='upper left')
        plt.xlabel('Threshold')
        plt.ylim(0,1)

    precision_recall_vs_threshold(precision,recall,threshold)
    plt.show()

