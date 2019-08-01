## Sklearn 中 SVM SVC SVR包的区别

### SVM 

    from sklearn import svm

SVM中包含了 SVC 和 SVR

### SVC

    from sklearn.svm import SVC

当做 __分类器__ 的时候，我们使用的是 SVC 或者 LinearSVC。SVC 的英文是 Support Vector Classification。

###SVR

    from sklearn.svm import SVR

当用 SVM 做 __回归__ 的时候，我们可以使用 SVR 或 LinearSVR。SVR 的英文是 Support Vector Regression。


### 总结

__SVM模型的几种__

    svm.LinearSVC Linear Support Vector Classification.

    svm.LinearSVR Linear Support Vector Regression.

    svm.NuSVC Nu-Support Vector Classification.

    svm.NuSVR Nu Support Vector Regression.

    svm.OneClassSVM Unsupervised Outlier Detection.

    svm.SVC C-Support Vector Classification.

    svm.SVR Epsilon-Support Vector Regression.