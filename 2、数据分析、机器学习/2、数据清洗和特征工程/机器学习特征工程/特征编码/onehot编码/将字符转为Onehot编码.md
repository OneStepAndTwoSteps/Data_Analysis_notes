# onehot编码转换

我们在进行建模时，变量中经常会有一些变量为离散型变量，例如性别。这些变量我们一般无法直接放到模型中去训练模型。因此在使用之前，我们往往会对此类变量进行处理。一般是对离散变量进行one-hot编码。下面具体介绍通过python对离散变量进行one-hot的方法。

## `方法一`

### `初級`：


__pd.get_dummies(prefix=)__

__`参数：`__

    prefix : string, list of strings, or dict of strings, default None 
    get_dummies转换后，列名的前缀 

pandas的get_dummies()可以直接对变量进行one-hot编码，其中prefix是为one-hot编码后的变量进行命名。

__`数据`__

    df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                     'C': [1, 2, 3]})
  
        A	B	C
    0	a	b	1
    1	b	a	2
    2	a	c	3


__`例子`__

    pd.get_dummies(df)

__`out`__

        C	A_a	A_b	B_a	B_b	B_c
    0	1	1	0	0	1	0
    1	2	0	1	1	0	0
    2	3	1	0	0	0	1

__`例子2`__

    pd.get_dummies(df, prefix=['col1', 'col2'])

__`out`__

        C	col1_a	col1_b	col2_a	col2_b	col2_c
    0	1	1	    0	    0	    1	    0
    1	2	0	    1	    1	    0	    0
    2	3	1	    0	    0	    0	    1

### `进阶`：


__`例子3`__

筛选出数据类型为 `object` 的数据进行 `onehot` 编码。

    bureau = pd.read_csv('xxxxx')

    categorical = pd.get_dummies(bureau.select_dtypes('object'))
    
    # SK_ID_CURR 是唯一标识 id，这里对新生成的 df 进行赋值
    categorical['SK_ID_CURR'] = bureau['SK_ID_CURR']
    categorical.head()

__`效果图：`__

<div align="center"><img width="800" height="150" src="./static/get_dummies.jpg"/></div>



## `方法二`

### `初级`

__`LabelEncoder 和 OneHotEncoder`__

我们也可以通过sklearn的模块实现对离散变量的one-hot编码，其中LabelEncoder是将离散变量替换为数字，OneHotEncoder则实现对替换为数字的离散变量进行one-hot编码。

Label Encoder有助于检索和保留序数特征所隐含的信息

__`例子`__

__`1、LabelEncoder()`__

    # 简单来说 LabelEncoder 是对不连续的数字或者文本进行编号
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    le.fit([1,5,67,100])
    le.transform([1,1,100,67,5])
    
    array([0,0,3,2,1])

__`2、OneHotEncoder()`__

    # OneHotEncoder 用于将表示分类的数据扩维：
    from sklearn.preprocessing import OneHotEncoder
    ohe = OneHotEncoder()
    ohe.fit([[1],[2],[3],[4]])
    ohe.transform([2],[3],[1],[4]).toarray()
    
    [[0,1,0,0], [0,0,1,0], [1,0,0,0], [0,0,0,1]]


## `进阶`

### `保留有序特征的label，将无序特征进行onehot编码`

#### `例子：`

    import pandas as pd
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import OneHotEncoder
    
    df = pd.DataFrame([
        ['green', 'Chevrolet', 2017],
        ['blue', 'BMW', 2015],
        ['yellow', 'Lexus', 2018],
    ])
    df.columns = ['color', 'make', 'year']
    
    le_color = LabelEncoder()
    le_make = LabelEncoder()
    df['color_encoded'] = le_color.fit_transform(df.color)
    df['make_encoded'] = le_make.fit_transform(df.make)
    
    color_ohe = OneHotEncoder()
    make_ohe = OneHotEncoder()
    X = color_ohe.fit_transform(df.color_encoded.values.reshape(-1, 1)).toarray()
    Xm = make_ohe.fit_transform(df.make_encoded.values.reshape(-1, 1)).toarray()
    
    dfOneHot = pd.DataFrame(X, columns=["Color_" + str(int(i)) for i in range(X.shape[1])])
    df = pd.concat([df, dfOneHot], axis=1)
    
    dfOneHot = pd.DataFrame(Xm, columns=["Make" + str(int(i)) for i in range(X.shape[1])])
    df = pd.concat([df, dfOneHot], axis=1)

#### `实战：`

已经过处理之后的特征及其对应值

    train_data.head()

        Survived	Pclass	Sex	Age	Fare	Embarked	Title	Isalone
    0	    0	    3	    1	1	0	    2	          2	    0
    1	    1	    1	    0	2	0	    0	          3	    0
    2	    1	    3	    0	1	0	    2	          1	    1
    3	    1	    1	    0	2	0	    2	          3	    0
    4	    0	    3	    1	2	0	    2	          2	    1


    from sklearn.preprocessing import OneHotEncoder
    ohe=OneHotEncoder()

    # 将无序特征进行onehot编码
    Sex_ohe=ohe.fit_transform(train_data[['Sex']].values.reshape(-1, 1)).toarray()
    Isalone_ohe=ohe.fit_transform(train_data[['Isalone']].values.reshape(-1, 1)).toarray()
    Embarked_ohe=ohe.fit_transform(train_data[['Embarked']].values.reshape(-1, 1)).toarray()
    Title_ohe=ohe.fit_transform(train_data[['Title']].values.reshape(-1, 1)).toarray()

    # 为各个onehot编码之后的特征值取名
    Sex_ohe = pd.DataFrame(Sex_ohe, columns=["Sex" + str(int(i)) for i in range(Sex_ohe.shape[1])])
    Isalone_ohe = pd.DataFrame(Isalone_ohe, columns=["Isalone" + str(int(i)) for i in range(Isalone_ohe.shape[1])])
    Embarked_ohe = pd.DataFrame(Embarked_ohe, columns=["Embarked" + str(int(i)) for i in range(Embarked_ohe.shape[1])])
    Title_ohe = pd.DataFrame(Title_ohe, columns=["Title" + str(int(i)) for i in range(Title_ohe.shape[1])])

    # 将编为onehot向量的特征和原来的特征进行拼接
    df = pd.concat([train_data[['Pclass','Age','Fare']], Sex_ohe,Isalone_ohe,Embarked_ohe,Title_ohe], axis=1)
    df.head()

#### `展示结果：`

        Pclass	Age	Fare	Sex0	Sex1	Isalone0	Isalone1	Embarked0	Embarked1	Embarked2	Title0	Title1	Title2	Title3	Title4
    0	3	    1	0	    0.0	    1.0	    1.0	        0.0	        0.0	        0.0	        1.0	        0.0	    0.0	    1.0	    0.0 	0.0
    1	1	    2	0	    1.0	    0.0	    1.0	        0.0	        1.0	        0.0	        0.0	        0.0	    0.0	    0.0	    1.0	    0.0
    2	3	    1	0	    1.0	    0.0	    0.0	        1.0	        0.0	        0.0	        1.0	        0.0	    1.0	    0.0	    0.0	    0.0
    3	1	    2	0	    1.0	    0.0	    1.0	        0.0	        0.0	        0.0	        1.0	        0.0	    0.0	    0.0	    1.0	    0.0
    4	3	    2	0	    0.0	    1.0	    0.0	        1.0	        0.0	        0.0	        1.0	        0.0	    0.0	    1.0	    0.0	    0.0



#### `注意：`

`get_dummies()` 可以直接对字符型变量进行 `one-hot` 编码，但 `OneHotEncoder` 不能直接对字符型变量编码，因此我们需要先将字符型变量转换为数值型变量。这就是为什么在 `OneHotEncoder` 之前需要 `LabelEncoder` 的原因。

