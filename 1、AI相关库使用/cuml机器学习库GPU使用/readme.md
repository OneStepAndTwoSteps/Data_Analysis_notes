# `cuML - GPU Machine Learning Algorithms`

`介绍：`[cuML](https://github.com/rapidsai/cuml) `is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that share compatible APIs with other RAPIDS projects.`



## `一、分类场景：`

### `1、导入模块：`

    import cuml
    import cudf
    import cupy


### `2、绘制混淆矩阵：`

    import itertools

    '''
    cm：混淆矩阵
    classes：标签的unique列表
    '''


    def plot_confusion_matrix(cm, classes,
                                normalize=False,
                                title='Confusion matrix',
                                cmap=plt.cm.Blues):
        """
            此函数打印并绘制混淆矩阵。
            可以通过设置“ normalize = True”来应用归一化。
        """
        plt.figure(figsize=(10,8))

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=90)
        plt.yticks(tick_marks, classes)

        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                        horizontalalignment="center",
                        color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()


### `3、func 定义：`

    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
    import time
    from sklearn.preprocessing import normalize

    def func(models,classes):
        model = models
        start = time.clock()

        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        acc = accuracy_score(y_test, pred)

        print('Test Accuracy : \033[32m \033[01m {:.5f}% \033[30m \033[0m'.format(acc*100))
        
        ## 下述代码为绘制混淆矩阵
        cnf_matrix = confusion_matrix(y_test, pred)
        np.set_printoptions(precision=2)

        norm_cnf_matrix = normalize(cnf_matrix,norm='l1')
        norm_cnf_matrix = np.around(norm_cnf_matrix,decimals=2)
        plot_confusion_matrix(norm_cnf_matrix, classes=classes, title='Normalized confusion matrix')

        plt.show()

        end = time.clock()
        print (str(end-start))
        
        return model,acc


### `4、数据处理：`

* `类别标签转换：`


        label_mapping = {"BENIGN": 0, "DoS Hulk": 1,'PortScan':2,'DDoS':3,'DoS GoldenEye':4,
                        'FTP-Patator':5,'SSH-Patator':6,'DoS slowloris':7,'Bot':8,'Web Attack � Brute Force':9,
                        'Web Attack � XSS':10,'Infiltration':11,'Web Attack � Sql Injection':12,'Heartbleed':13}
        Thursday['Label'] = Thursday['Label'].map(label_mapping)



* `数据标准化和切分：`

        from sklearn.preprocessing import StandardScaler

        Thursday = Thursday.dropna()
        X = Thursday.drop(["Label"],axis=1)


        ## 使用 cuml 可能会报无法识别分类的错误，所以使用下述代码解决
        enc = cuml.preprocessing.LabelEncoder()
        y = enc.fit_transform( Thursday['Label'])

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X,y.values,test_size=0.3, random_state=3)


        ## func 中的 y_pred 是 np array，所以这里将y_test 转为 np array，否则报错 .get方法
        y_test = np.array(y_test.get())



### `5、执行func`

    from cuml.ensemble import RandomForestClassifier

    class_names = ["BENIGN", 'Web Attack � Brute Force','Web Attack � XSS','Infiltration','Web Attack � Sql Injection']

    Thu_rfc,acc_RFC =func(RandomForestClassifier(),class_names)





