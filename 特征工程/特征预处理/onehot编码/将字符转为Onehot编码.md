## onehot编码转换

我们在进行建模时，变量中经常会有一些变量为离散型变量，例如性别。这些变量我们一般无法直接放到模型中去训练模型。因此在使用之前，我们往往会对此类变量进行处理。一般是对离散变量进行one-hot编码。下面具体介绍通过python对离散变量进行one-hot的方法。


#### 方法一

__pd.get_dummies(prefix=)__

__参数：__

    prefix : string, list of strings, or dict of strings, default None 
    get_dummies转换后，列名的前缀 

pandas的get_dummies()可以直接对变量进行one-hot编码，其中prefix是为one-hot编码后的变量进行命名。

__数据__

    df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                     'C': [1, 2, 3]})
  
        A	B	C
    0	a	b	1
    1	b	a	2
    2	a	c	3


__例子__

    pd.get_dummies(df)

__out__

        C	A_a	A_b	B_a	B_b	B_c
    0	1	1	0	0	1	0
    1	2	0	1	1	0	0
    2	3	1	0	0	0	1

__例子2__

    pd.get_dummies(df, prefix=['col1', 'col2'])

__out__

        C	col1_a	col1_b	col2_a	col2_b	col2_c
    0	1	1	    0	    0	    1	    0
    1	2	0	    1	    1	    0	    0
    2	3	1	    0	    0	    0	    1



#### 方法二

__LabelEncoder和OneHotEncoder__

我们也可以通过sklearn的模块实现对离散变量的one-hot编码，其中LabelEncoder是将离散变量替换为数字，OneHotEncoder则实现对替换为数字的离散变量进行one-hot编码。

Label Encoder有助于检索和保留序数特征所隐含的信息

__例子__

__1、LabelEncoder()__

    # 简单来说 LabelEncoder 是对不连续的数字或者文本进行编号
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    le.fit([1,5,67,100])
    le.transform([1,1,100,67,5])
    
    array([0,0,3,2,1])

__2、OneHotEncoder()__

    # OneHotEncoder 用于将表示分类的数据扩维：
    from sklearn.preprocessing import OneHotEncoder
    ohe = OneHotEncoder()
    ohe.fit([[1],[2],[3],[4]])
    ohe.transform([2],[3],[1],[4]).toarray()
    
    [[0,1,0,0], [0,0,1,0], [1,0,0,0], [0,0,0,1]]



#### 注意：

get_dummies()可以直接对字符型变量进行one-hot编码，但OneHotEncoder不能直接对字符型变量编码，因此我们需要先将字符型变量转换为数值型变量。这就是为什么在OneHotEncoder之前需要LabelEncoder的原因。

