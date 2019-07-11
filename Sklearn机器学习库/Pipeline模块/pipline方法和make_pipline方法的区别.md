### pipline方法和make_pipline方法的区别

__唯一的区别是make_pipeline自动为步骤生成名称。而pipline需要步骤名称.__

__例子__

如果要使用具有模型选择实用程序的管道（例如GridSearchCV）。使用网格搜索，您需要为管道的各个步骤指定参数：(pipline)

    pipe = Pipeline([('vec', CountVectorizer()), ('clf', LogisticRegression()])
    param_grid = [{'clf__C': [1, 10, 100, 1000]}
    gs = GridSearchCV(pipe, param_grid)
    gs.fit(X, y)

将它与make_pipeline进行比较：(make_pipeline)

    pipe = make_pipeline(CountVectorizer(), LogisticRegression())     
    param_grid = [{'logisticregression__C': [1, 10, 100, 1000]}
    gs = GridSearchCV(pipe, param_grid)
    gs.fit(X, y)

### 总结：   

#### Pipeline：

    名称是明确的，如果您需要，您无需弄明白;
    如果更改步骤中使用的估算器/变换器，则
    名称不会更改，例如如果用LinearSVC（）替换LogisticRegression（），你仍然可以使用clf__C。

#### make_pipeline：

    更短且可以说是更具可读性的符号;
    使用简单的规则（估算器的小写名称）自动生成名称。
