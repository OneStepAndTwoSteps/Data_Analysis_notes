## Pipeline

Pipeline 构造器需要一个定义步骤顺序的名字/估计器对的列表。__除了最后一个估计器，其余都要是转换器（即，它们都要有 fit_transform() 方法）。__ 名字可以随意起。

当你 __调用流水线的 fit() 方法__ ，就会对所有转换器 __顺序调用 fit_transform() 方法__，将每次调用的输出作为参数传递给下一个调用，__一直到最后一个估计器，它只执行 fit() 方法。__



### pipeline的流程案例-代码解释1：

    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    num_pipeline = Pipeline(
        [
            ('imputer',impute.SimpleImputer(strategy='median')),
            ('attribs_adder',CombinedAttributesAdder()),
            ('std_scaler',StandardScaler()),
        ]
    )
    housing_num_tr=num_pipeline.fit_transform(housing[attribute])


流水线暴露相同的方法作为最终的估计器。在这个例子中，最后的估计器是一个StandardScaler，它是一个转换器，因此这个流水线有一个 transform() 方法，可以顺序对数据做所有转换（它还有一个	fit_transform 方法可以使用，就不必先调用 fit()再进行transform()）。

#### 注意：

pipeline最后一步(__估计器__)如果有transform方法，我们才可以进行fit_transform，也就是前面的几步(__转换器__)，都是进行fit_transform方法。


*   此时我们现在做的操作是对于数值类型的数据进行的转换，那么如果我们 __同时还要进行对分类值的转换__ 呢？

    Scikit-Learn提供了一个类 __FeatureUnion__ 实现这个功能。

        from sklearn_features.transformers import DataFrameSelector
        from sklearn.pipeline import FeatureUnion

        num_attribs = ['longitude', 'latitude','housing_median_age','total_rooms','total_bedrooms'
        ,'population','households', 'median_income','median_house_value']

        cat_attribs = ['ocean_proximity']

        num_pipeline = Pipeline([
        ('selector',DataFrameSelector(num_attribs)),        # 会选出num的数据
        ('imputer',impute.SimpleImputer(strategy='median')),
        ('attribs_adder',CombinedAttributesAdder()),
        ('std_scaler',StandardScaler()),
        ])

        cat_pipeline = Pipeline([
            ('selector',DataFrameSelector(cat_attribs)),    # 会选出cat的数据
            # 两个返回的结果一致
        #   ('cat_encoder',CategoricalEncoder(encoding="onehot-dense")),
            ('ohe',OneHotEncoder(sparse=False)),
        ])

        full_pipeline = FeatureUnion(transformer_list=[
            ('num_pipeline',num_pipeline),
            ('cat_pipeline',cat_pipeline),

        ])

        housing_prepared = full_pipeline.fit_transform(housing)
        housing_prepared

        array([[-1.32783522,  1.05254828,  0.98214266, ...,  0.        ,
                1.        ,  0.        ],
            [-1.32284391,  1.04318455, -0.60701891, ...,  0.        ,
                1.        ,  0.        ],
            [-1.33282653,  1.03850269,  1.85618152, ...,  0.        ,
                1.        ,  0.        ],
            ...,
            [-0.8237132 ,  1.77823747, -0.92485123, ...,  0.        ,
                0.        ,  0.        ],
            [-0.87362627,  1.77823747, -0.84539315, ...,  0.        ,
                0.        ,  0.        ],
            [-0.83369581,  1.75014627, -1.00430931, ...,  0.        ,
                0.        ,  0.        ]])


对于 FeatureUnion 你给它一列转换器（可以是所有的转换器），当调用它的transform()方法，__每个转换器的transform()会被并行执行__，等待输出，然后 __将输出合并起来，并返回结果__（当然，调用它的fit()方法就会调用每个转换器的fit()）。



### pipeline的流程案例-代码解释2：

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



