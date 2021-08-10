# 决策树

## Titanic 乘客生存预测流程

    数据获取 --> 数据探索 --> 数据清理 --> 特征选择 --> 决策树模型 --> 模型预测和评估 --> 决策树可视化
  
  ### 模块 1:数据探索：
  
    一、使用 info() 了解数据表的基本情况：行数、列数、每列的数据类型、数据完整度；
           
    二、使用 describe() 了解数据表的统计情况：总数、平均值、标准差、最小值、最大值等；
               
    三、使用 describe(include=[‘O’]) 查看字符串类型（非数字）的整体情况；
            
    四、使用 head 查看前几行数据（默认是前 5 行）；
            
    五、使用 tail 查看后几行数据（默认是最后 5 行）。

  ### 模块 2：数据清洗
   通过数据探索，我们发现 Age和 Cabin 这三个字段的数据有所缺失。其中 Age 为年龄字段，是数值型，我们可以通过平均值进行补齐；。
    
      # 使用平均年龄来填充年龄中的 nan 值
      train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
      test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)

   Cabin 为船舱，有大量的缺失值。在训练集和测试集中的缺失率分别为 77% 和 78%，无法补齐；Embarked 为登陆港口，有少量的缺失值，我们可以把缺失值补齐。
    
    print(train_data['Embarked'].value_counts())
    
 __输出结果：__
   
    S    644
    C    168
    Q     77

我们发现一共就 3 个登陆港口，其中 S 港口人数最多，占到了 72%，因此我们将其余缺失的 Embarked 数值均设置为 S：
 
    # 使用登录最多的港口来填充登录港口的 nan 值
    train_data['Embarked'].fillna('S', inplace=True)
    test_data['Embarked'].fillna('S',inplace=True)

### 模块 3：特征选择
  通过数据探索，PassengerId 为乘客编号，对分类没有作用，可以放弃；Name 为乘客姓名，对分类没有作用，可以放弃；Cabin 字段缺失值太多，可以放弃；Ticket 字段为船票号码，杂乱无章且无规律，可以放弃。其余的字段包括：Pclass、Sex、Age、SibSp、Parch 和 Fare，这些属性分别表示了乘客的船票等级、性别、年龄、亲戚数量以及船票价格，可能会和乘客的生存预测分类有关系。具体是什么关系，我们可以交给分类器来处理。

    # 特征选择
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    train_features = train_data[features]
    train_labels = train_data['Survived']
    test_features = test_data[features]
    
__特征值里有一些是字符串，这样不方便后续的运算，需要转成数值类型，比如 Sex 字段，有 male 和 female 两种取值。我们可以把它变成 Sex=male 和 Sex=female 两个字段，数值用 0 或 1 来表示。__

__我们可以使用 sklearn 特征选择中的 DictVectorizer 类，用它将可以处理符号化的对象，将符号转成数字 0/1 进行表示。具体方法如下：__
   
    from sklearn.feature_extraction import DictVectorizer
    dvec=DictVectorizer(sparse=False)
    train_features=dvec.fit_transform(train_features.to_dict(orient='record'))

fit_transform 这个函数，它可以将特征向量转化为特征值矩阵。打印 dvec 在转化后的特征属性是怎样的，即查看 dvec 的 feature_names_ 属性值，方法如下：
  
    print(dvec.feature_names_)
    
__输出结果：__

    ['Age', 'Embarked=C', 'Embarked=Q', 'Embarked=S', 'Fare', 'Parch', 'Pclass', 'Sex=female', 'Sex=male', 'SibSp']


### 模块 4：决策树模型
  使用 ID3 算法，即在创建 DecisionTreeClassifier 时，设置 criterion=‘entropy’，然后使用 fit 进行训练，将特征值矩阵和分类标识结果作为参数传入，得到决策树分类器。
    
    from sklearn.tree import DecisionTreeClassifier
    # 构造 ID3 决策树
    clf = DecisionTreeClassifier(criterion='entropy')
    # 决策树训练
    clf.fit(train_features, train_labels)

__另一种方法：训练的时候我们也可以使用train_test_split分割我们的数据集如下：__
          
    data_train,data_test,label_train,label_test=train_test_split(train_features,train_label,test_size=0.1,random_state=42)
   
    clf=DecisionTreeClassifier(criterion='entropy',random_state=42)
    clf.fit(data_train,label_train)
    print(clf.score(data_test, label_test))
    # 用 CART 分类树做预测
    test_predict = clf.predict(data_test)
    score = accuracy_score(label_test, test_predict)
    print("CART 分类树准确率 %.4lf" % score)
    
    训练就结束了
    输出结果：    CART 分类树准确率 0.7778


### 模块 5：模型预测 & 评估
  在预测中，我们首先需要得到测试集的特征值矩阵，然后使用训练好的决策树 clf 进行预测，得到预测结果 pred_labels：
  
    test_features=dvec.transform(test_features.to_dict(orient='record'))
    # 决策树预测   
    pred_labels = clf.predict(test_features)
    
在模型评估中，决策树提供了 score 函数可以直接得到准确率，但是我们并不知道真实的预测结果，所以无法用预测值和真实的预测结果做比较 __因为我们现在的代码中没有设置测试集的标签__ 。我们只能使用训练集中的数据进行模型评估，可以使用决策树自带的 score 函数计算下得到的结果：
    
    # 得到决策树准确率
    acc_decision_tree = round(clf.score(train_features, train_labels), 6)
    print(u'score 准确率为 %.4lf' % acc_decision_tree)

__输出结果：__
  
    score 准确率为 0.9820
    
我们发现刚用训练集做训练，再用训练集自身做准确率评估自然会很高。但这样得出的准确率并不能代表决策树分类器的准确率。
因为我们没有测试集的实际结果，因此无法用测试集的预测结果与实际结果做对比。如果我们使用 score 函数对训练集的准确率进行统计，正确率会接近于 100%（如上结果为 98.2%），无法对分类器的在实际环境下做准确率的评估。

这里可以使用 __K 折交叉验证的方式__ ，交叉验证是一种常用的验证分类准确率的方法，原理是拿出大部分样本进行训练，少量的用于分类器的验证。K 折交叉验证，就是做 K 次交叉验证，每次选取 K 分之一的数据作为验证，其余作为训练。轮流 K 次，取平均值。

交叉熵这里又讲
https://github.com/OneStepAndTwoSteps/data_mining_analysis/blob/master/sklearn%E5%BA%93/11_sklearn%E5%86%85%E7%BD%AE%E6%96%B9%E6%B3%95.md
 
在 sklearn 的 model_selection 模型选择中提供了 cross_val_score 函数。cross_val_score 函数中的参数 cv 代表对原始数据划分成多少份，也就是我们的 K 值，一般建议 K 值取 10，因此我们可以设置 CV=10，我们可以对比下 score 和 cross_val_score 两种函数的正确率的评估结果：

    import numpy as np
    from sklearn.model_selection import cross_val_score
    # 使用 K 折交叉验证 统计决策树准确率
    print(u'cross_val_score 准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))

输出结果：

    cross_val_score 准确率为 0.7835

### 模块 6：决策树可视化
  
  

## 决策树模型使用技巧总结

  __1.特征选择是分类模型好坏的关键。__ 选择什么样的特征，以及对应的特征值矩阵，决定了分类模型的好坏。 __通常情况下，特征值不都是数值类型，可以使用 DictVectorizer 类进行转化；__
  
  __2.模型准确率需要考虑是否有测试集的实际结果可以做对比，__ 当测试集没有真实结果可以对比时，需要使用 __K 折交叉验证 cross_val_score，就是交叉熵；__
  
  __3.Graphviz 可视化工具可以很方便地将决策模型呈现出来，帮助你更好理解决策树的构建。__






