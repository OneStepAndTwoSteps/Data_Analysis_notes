
### pipeline的流程案例-代码解释：

    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline

    pipe_lr = Pipeline([('sc', StandardScaler()),
                        ('pca', PCA(n_components=2)),
                        ('clf', LogisticRegression(random_state=1))
                        ])
    pipe_lr.fit(X_train, y_train)
    print('Test accuracy: %.3f' % pipe_lr.score(X_test, y_test))  

### Pipeline执行流程的分析

pipeline 的中间过程由scikit-learn相适配的转换器（transformer）构成，最后一步是一个estimator。比如上述的代码，StandardScaler和PCA transformer 构成intermediate steps，LogisticRegression 作为最终的estimator。

当我们执行 pipe_lr.fit(X_train, y_train)时，首先由StandardScaler在训练集上执行 fit和transform方法，transformed后的数据又被传递给Pipeline对象的下一步，也即PCA()。和StandardScaler一样，PCA也是执行fit和transform方法，最终将转换后的数据传递给 LosigsticRegression。



