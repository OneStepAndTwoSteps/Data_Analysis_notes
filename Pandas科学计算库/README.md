
# 📖pandas用法梳理

## pandas介绍：
  在数据分析工作中，Pandas 的使用频率是很高的，一方面是因为 Pandas 提供的基础数据结构 DataFrame 与 json 的契合度很高，转换起来就很方便。
  另一方面，如果我们日常的数据清理工作不是很复杂的话，你通常用几句 Pandas 代码就可以对数据进行规整。

  Pandas 可以说是基于 NumPy 构建的含有更高级数据结构和分析能力的工具包。在 NumPy 中数据结构是围绕 ndarray 展开的，那么在 Pandas 中的核心数据结构是什么呢？

  下面主要给你讲下Series 和 DataFrame 这两个核心数据结构，他们分别代表着一维的序列和二维的表结构。基于这两种数据结构，Pandas 可以对数据进行导入、清洗、处理、统计和输出。

## pandas.set_option 选项设置
  __可以设置pandas的属性，比如打印出来数据时显示多少列，显示多宽等等，可以一次性设置多个格式如下__
   
  设置pandas保留小数位数为三位
  
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
  
  默认显示列数，行数,当设置为None时，表示显示所有内容
    
    pd.set_option('display.max_columns',5, 'display.max_rows', 100)
  
  设置pandas显示所有数据内容(不隐藏数据)：

  显示所有列 (列中有省略的不省略)

    pd.set_option('display.max_columns', None)
    
  __解决如下问题：__

      11 12 13 ... 19 20
      21 22 23 ... 29 30
      31 32 33 ... 39 40
      41 42 43 ... 49 50

  显示所有行 (行中有省略的不省略)
  
    pd.set_option('display.max_rows', None)

  __解决如下问题：__

      1 2 3
      4 5 6
      7 8 9
      ...
      100 101 102    
      
## 数据结构Series 和 Dataframe

### Series
  __Series 是个定长的字典序列__ 。说是定长是因为在存储的时候，相当于两个 ndarray，这也是和字典结构最大的不同。因为在字典的结构里，元素的个数是不固定的。
  
  __Series 的两个基本属性__ 有两个基本属性：index 和 values。在 Series 结构中，index 默认是 0,1,2,……递增的整数序列，当然我们也可以自己来指定索引，比如 index=[‘a’, ‘b’, ‘c’, ‘d’]。
  
  __例子：__
  
    import pandas as pd
    from pandas import Series, DataFrame
    x1 = Series([1,2,3,4])
    x2 = Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
    print x1
    print x2

  
  __运行结果：__
  
    0    1
    1    2
    2    3
    3    4
    dtype: int64
    a    1
    b    2
    c    3
    d    4
    dtype: int64
    
这个例子中，x1 中的 index 采用的是默认值，x2 中 index 进行了指定。我们也可以采用字典的方式来创建 Series，比如：

__例子：__

    d = {'a':1, 'b':2, 'c':3, 'd':4}
    x3 = Series(d)
    print x3 

__运行结果：__
  
    a    1
    b    2
    c    3
    d    4
    dtype: int64

### DataFrame 类型数据结构类似数据库表。

  它包括了行索引和列索引，我们可以将 DataFrame 看成是由相同索引的 Series 组成的字典类型。
  
  我们虚构一个考试的场景，想要输出几位英雄的考试成绩：
    
    import pandas as pd
    from pandas import Series, DataFrame
    data = {'Chinese': [66, 95, 93, 90,80],'English': [65, 85, 92, 88, 90],'Math': [30, 98, 96, 77, 90]}
    df1= DataFrame(data)
    df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
    print df1
    print df2

  在后面的案例中，我一般会用 df, df1, df2 这些作为 DataFrame 数据类型的变量名，我们以例子中的 df2 为例，
  列索引是 [‘English’, ‘Math’, ‘Chinese’]，行索引是 [‘ZhangFei’, ‘GuanYu’, ‘ZhaoYun’, ‘HuangZhong’, ‘DianWei’]，所以 df2 的输出是：
  
  
                  English  Math  Chinese
    ZhangFei         65    30       66
    GuanYu           85    98       95
    ZhaoYun          92    96       93
    HuangZhong       88    77       90
    DianWei          90    90       80

在了解了 Series 和 DataFrame 这两个数据结构后，我们就从数据处理的流程角度，来看下他们的使用方法。

Pandas 允许直接从 xlsx，csv 等文件中导入数据，也可以输出到 xlsx, csv 等文件，非常方便。
  
    import pandas as pd
    from pandas import Series, DataFrame
    score = DataFrame(pd.read_excel('data.xlsx'))
    score.to_excel('data1.xlsx')
    print score
  
需要说明的是，在运行的过程可能会存在缺少 xlrd 和 openpyxl 包的情况，到时候如果缺少了，可以在命令行模式下使用“pip install”命令来进行安装。


### Dataframe 和 Series 的坑

___场景：在一段df数据中我们进行取值__

__数据：__
  
    train_data.head()

__out：__

      Survived	Pclass	Sex	Age	Fare	Embarked	Title	Isalone
    0 	0	      3	      1	  1	  0   	2	        2	    0
    1	  1	      1	      0	  2	  0	    0	        3	    0
    2	  1	      3	      0	  1	  0   	2	        1	    1
    3	  1	      1	      0	  2	  0	    2	        3	    0
    4	  0	      3	      1	  2	  0	    2	        2	    1


__双括号和单括号之间的区别：__

__双括号取出的 Survived 是 DataFrame 格式__

    type(train_data[['Survived']].head())

    pandas.core.frame.DataFrame

__单括号取出的 Survived 是 Series 格式__

    type(train_data['Survived'].head())
    pandas.core.series.Series

取出来为 Series 格式，但是你没有发觉，此后如果想赋值一个新的列，那么无法成功，因为Series中只能有一列。



### pandas 数据类型

Pandas __dtype__ 映射：

<div align=center><img width="700" height="430" src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/pandas/3.png"/></div>


### 将 object 类型转为 category 分类类型





### 数据清洗
  数据清洗是数据准备过程中必不可少的环节，Pandas 也为我们提供了数据清洗的工具，在后面数据清洗的章节中会给你做详细的介绍，这里简单介绍下 Pandas 在数据清洗中的使用方法。
  
  还是以上面这些英雄人物的数据为例。
  
    data = {'Chinese': [66, 95, 93, 90,80],'English': [65, 85, 92, 88, 90],'Math': [30, 98, 96, 77, 90]}
    df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])

  在数据清洗过程中，一般都会遇到以下这几种情况，下面我来简单介绍一下。
  
  __1. 删除 DataFrame 中的不必要的列或行：__
  
  Pandas 提供了一个便捷的方法 drop() 函数来删除我们不想要的列或行。比如我们想把“语文”这列删掉。
    
    df2 = df2.drop(columns=['Chinese'])

  想把“张飞”这行删掉。
  
    df2 = df2.drop(index=['ZhangFei'])
  
  刪除不需要的列名也可以用delete()，删除train_data.columns的第一列，注意delete不能对df数据类型使用。

    coeff_df = pd.DataFrame(train_data.columns.delete(0))


  __2. 重命名列名 columns，让列表名更容易识别：__
  
  如果你想对 DataFrame 中的 columns 进行重命名，可以直接使用 rename(columns=new_names, inplace=True) 函数，比如我把列名 Chinese 改成 YuWen，English 改成 YingYu。
  
    # inplace：刷选过缺失值得新数据是存为副本还是直接在原数据上进行修改。
    df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace = True)

  __3. 去重复的值：__
    数据采集可能存在重复的行，这时只要使用 drop_duplicates() 就会自动把重复的行去掉。
  
      df = df.drop_duplicates() # 去除重复行

  __4. 格式问题：__
    这是个比较常用的操作，因为很多时候数据格式不规范，我们可以使用 astype 函数来规范数据格式，比如我们把 Chinese 字段的值改成 str 类型，或者 int64 可以这么写：
  
      df2['Chinese'].astype('str') 
      df2['Chinese'].astype(np.int64) 

  
### 数据间的空格

  有时候我们先把格式转成了 str 类型，是为了方便对数据进行操作，这时想要删除数据间的空格，我们就可以使用 strip 函数：
  
    # 删除左右两边空格
    df2['Chinese']=df2['Chinese'].map(str.strip)
    # 删除左边空格
    df2['Chinese']=df2['Chinese'].map(str.lstrip)
    # 删除右边空格
    df2['Chinese']=df2['Chinese'].map(str.rstrip)

  如果数据里有某个特殊的符号，我们想要删除怎么办？同样可以使用 strip 函数，比如 Chinese 字段里有美元符号，我们想把这个删掉，可以这么写：

    df2['Chinese']=df2['Chinese'].str.strip('$')


__大小写转换：__
  
  大小写是个比较常见的操作，比如人名、城市名等的统一都可能用到大小写的转换，在 Python 里直接使用 upper(), lower(), title() 函数，方法如下：
  
    # 全部大写
    df2.columns = df2.columns.str.upper()
    # 全部小写
    df2.columns = df2.columns.str.lower()
    # 首字母大写
    df2.columns = df2.columns.str.title()

  
__查找空值：__

  数据量大的情况下，有些字段存在空值 NaN 的可能，这时就需要使用 Pandas 中的 __isnull__ 函数进行查找。比如，我们输入一个数据表如下：
    
    姓名     语文     英语     数学
    
    张飞     66       65        
    
    关羽     95       85       98   
  
    赵云     95       92       96   
    
    黄忠     90       88       77   
  
    典韦     80       90       90   
  
  
  
  如果我们想看下哪个地方存在空值 NaN，可以针对数据表 df进行 __df.isnull()__ :结果如下

        姓名      语文     英语     数学
     0  False    False    False    True   
     1  False    False    False    False   
     2  False    False    False    False   
     3  False    False    False    False   
     4  False    False    False    False   

  
  如果我想知道哪列存在空值，可以使用 __df.isnull().any()__ ，结果如下：
  
    姓名     False
    语文     False
    英语     False
    数学     True
  
  __直接查看那个列存在空值：__

    train.isnull().any()[train.isnull().any().values==True]

  out：

    overview    True
    runtime     True
    tagline     True
    dtype: bool

  
  __使用 apply 函数对数据进行清洗：__
  
    apply 函数是 Pandas 中自由度非常高的函数，使用频率也非常高。
    比如我们想对 name 列的数值都进行大写转化可以用：
  
      df['name'] = df['name'].apply(str.upper)
      
    我们也可以定义个函数，在 apply 中进行使用。比如定义 double_df 函数是将原来的数值 *2 进行返回。然后对 df1 中的“语文”列的数值进行 *2 处理，可以写成：
  
      def double_df(x):
           return 2*x
      df1[u'语文'] = df1[u'语文'].apply(double_df)

    我们也可以定义更复杂的函数，比如对于 DataFrame，我们新增两列，其中’new1’列是“语文”和“英语”成绩之和的 m 倍，'new2’列是“语文”和“英语”成绩之和的 n 倍，我们可以这样写：
      
        def plus(df,n,m):
          df['new1'] = (df[u'语文']+df[u'英语']) * m
          df['new2'] = (df[u'语文']+df[u'英语']) * n
          return df
        df1 = df1.apply(plus,axis=1,args=(2,3,))

    其中 axis=1 代表按照列为轴进行操作，axis=0 代表按照行为轴进行操作，args 是传递的两个参数，即 n=2, m=3，在 plus 函数中使用到了 n 和 m，从而生成新的 df。
  
  __使用 apply 函数对数据进行清洗 (进阶) ：__
    
    # 将 train['production_companies'] 中的数据作为 x 传给apply函数，在apply中做处理
    # (取得的 production_companies 特征中的所有数据 [该数据是一个字典] 然后做if else判断)
    
    train['production_companies'].apply(lambda x: [i['name'] for i in x] if x != {} else []).values


__自定义函数apply__
 
      def search_hundredth(train_content):
          hundredth=train_content.loc[99]
          return hundredth

      search_func=train_content.apply(search_hundredth)
      print(search_func)

      1. 不同于 transform 只允许在 Series 上进行一次转换， apply对整个DataFrame 作用

      2.apply隐式地将group 上所有的列作为自定义函数

__自定义函数 transfrom__

  apply()里面可以跟自定义的函数，包括简单的求和函数以及复杂的特征间的差值函数等（注：apply不能直接使用agg()方法 / transform()中的python内置函数，例如sum、max、min、'count‘等方法）

  transform() 里面不能跟自定义的特征交互函数，因为transform是真针对每一元素（即每一列特征操作）进行计算，也就是说在使用 transform() 方法时，需要记得三点：

  1、__它只能对每一列进行计算__，所以在groupby()之后，.transform()之前是要指定要操作的列，这点也与apply有很大的不同。

  2、由于是只能对每一列计算，所以方法的通用性相比apply()就局限了很多，例如只能求列的最大/最小/均值/方差/分箱等操作

  3、transform还有什么用呢?最简单的情况是试图将函数的结果分配回原始的dataframe。也就是说返回的shape是 (len(df)，1)。注：如果与groupby()方法联合使用，需要对值进行去重。


__transform 和 apply的相同之处：__

  都能针对dataframe完成特征的计算，并且常常与groupby()方法一起使用。



  ### 数据统计
  
    在数据清洗后，我们就要对数据进行统计了。Pandas 和 NumPy 一样，都有常用的统计函数，如果遇到空值 NaN，会自动排除。
    常用的统计函数包括：
    以下函数可以指定计算的axis为行还是列，默认为行(就是某一列中的每一行特征) axis=0。注意如果计算所在某一列/行中存在字符，则该列/行将不进行计算
 
      count()     统计个数，空值NaN不计算
      describe()  一次性输出多个统计指标，包括：count,mean,std,min,max 等
      min()       最小值
      max()       最大值
      sum()       总和
      mean()      平均值
      median()    中位数
      var()       方差
      std()       标准差
      argmin()    统计最小值的索引位置
      argmax()    统计最大值的索引位置
      idxmin()    统计最小值的索引值
      idxmax()    统计最大值的索引值
      
      
   表格中有一个 describe() 函数，统计函数千千万，describe() 函数最简便。它是个统计大礼包，可以快速让我们对数据有个全面的了解。下面我直接使用 df1.describe() 输出结果为：
      
   分析泰坦尼克数据为例：

      train_df.describe() # 默认只计算数值类型

      out:

            PassengerId	  Survived	 Pclass	       Age	       SibSp	     Parch	    Fare
      count	891.000000	 891.000000	891.000000	714.000000	891.000000	891.000000	891.000000
      mean	446.000000	 0.383838	  2.308642	  29.699118	  0.523008  	0.381594	  32.204208
      std	  257.353842	  0.486592	0.836071  	14.526497	  1.102743	  0.806057	  49.693429
      min	  1.000000	    0.000000	1.000000  	0.420000	  0.000000	  0.000000	  0.000000
      25%	  223.500000	  0.000000	2.000000	  20.125000	  0.000000	  0.000000	  7.910400
      50%	  446.000000	  0.000000	3.000000	  28.000000	  0.000000	  0.000000	  14.454200
      75%	  668.500000	  1.000000	3.000000	  38.000000	  1.000000	  0.000000	  31.000000
      max	  891.000000	  1.000000	3.000000	  80.000000	  8.000000	  6.000000	  512.329200

      train_df.describe(include=['O']) # 只计算类型为str的数据
      
      out:
      
            Name	                           Sex	Ticket	Cabin	       Embarked
      count	  891         	                 891	891	     204	          889
      unique	891	                           2	  681	     147	          3
      top	Panula, Master. Juha Niilo	       male	1601	C23 C25 C27	      S
      freq    1                              577	7	         4	          644


   __运行结果:__  
   
  ![Image text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/describe.png)
        
   __数据表合并__
    
   有时候我们需要将多个渠道源的多个数据表进行合并，一个 DataFrame 相当于一个数据库的数据表，那么多个 DataFrame 数据表的合并就相当于多个数据库的表合并。
    
   比如我要创建两个 DataFrame：
    
      df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
      df2 = DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2':range(5)})

   __1. 基于指定列进行连接__
      
   比如我们可以基于 name 这列进行连接。
    
        df3 = pd.merge(df1, df2, on='name')

   __运行结果:__ 
   
   ![Image text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/1.png)
    
    
   __2. inner 内连接__
        
   inner 内链接是 merge 合并的默认情况，inner 内连接其实也就是键的交集，在这里 df1, df2 相同的键是 name，所以是基于 name 字段做的连接：
     
        df3 = pd.merge(df1, df2, how='inner')
   __运行结果:__ 
   
   ![Image text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/2-1.png)
    
   __3. left 左连接__
    
   左连接是以第一个 DataFrame 为主进行的连接，第二个 DataFrame 作为补充。
        
          df3 = pd.merge(df1, df2, how='left')
   __运行结果:__
   
  ![Image text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/3.png)

   __4. right 右连接__
        
   右连接是以第二个 DataFrame 为主进行的连接，第一个 DataFrame 作为补充。
      
        df3 = pd.merge(df1, df2, how='right')
   __运行结果:__
   
  ![Image text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/4.png)

   __5. outer 外连接__

   外连接相当于求两个 DataFrame 的并集。
        
        df3 = pd.merge(df1, df2, how='outer')
   __运行结果:__
   
  ![Image text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/5.png)
  
 ### 如何用 SQL 方式打开 Pandas
    
 Pandas 的 DataFrame 数据类型可以让我们像处理数据表一样进行操作，比如数据表的增删改查，都可以用 Pandas 工具来完成。
 不过也会有很多人记不住这些 Pandas 的命令，相比之下还是用 SQL 语句更熟练，用 SQL 对数据表进行操作是最方便的，它的语句描述形式更接近我们的自然语言。
    
 事实上，在 Python 里可以直接使用 SQL 语句来操作 Pandas。
    
 __这里给你介绍个工具：pandasql。__
    
 pandasql 中的主要函数是 sqldf，它接收两个参数：一个 SQL 查询语句，还有一组环境变量 globals() 或 locals()。这样我们就可以在 Python 里，直接用 SQL 语句中对 DataFrame 进行操作，举个例子：import pandas as pd
     
  __例子：__
    
      from pandas import DataFrame
      from pandasql import sqldf, load_meat, load_births
      df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
      pysqldf = lambda sql: sqldf(sql, globals())
      sql = "select * from df1 where name ='ZhangFei'"
      print pysqldf(sql)

    
  __运行结果：__
  
      data1      name
      0      0  ZhangFei

  上面这个例子中，我们是对“name='ZhangFei”“的行进行了输出。当然你会看到我们用到了 lambda，lambda 在 python 中算是使用频率很高的，那 lambda 是用来做什么的呢？
  它实际上是用来定义一个匿名函数的，具体的使用形式为：
  
      lambda argument_list: expression

  
  
  这里 argument_list 是参数列表，expression 是关于参数的表达式，会根据 expression 表达式计算结果进行输出返回。
  
  在上面的代码中，我们定义了：
  
    pysqldf = lambda sql: sqldf(sql, globals())

  在这个例子里，输入的参数是 sql，返回的结果是 sqldf 对 sql 的运行结果，当然 sqldf 中也输入了 globals 全局参数，因为在 sql 中有对全局参数 df1 的使用。
  
  ### 读取文件里的内容
  以csv的格式读取文件里的内容
    
    train_content=pd.read_csv("train.csv")
  
  以xls的格式读取文件里的内容 (excel文件读取方式)
    
    train_content=pd.read_excel("train.xls")
    
  显示pd_content的前面三行(不包括列名字)  
     
     print(train_content.head(3)
  
  pivot_table函数
    
  pivot_table有四个最重要的参数index、values、columns、aggfunc

  index     index代表索引，每个pivot_table必须拥有一个index。
  Values    Values可以对需要的计算数据进行筛选
  Aggfunc   aggfunc参数可以设置我们对数据聚合时进行的函数操作。当我们未设置aggfunc时，它默认aggfunc='mean'计算均值，可以设置多个 如：
            [aggfunc=[np.sum,np.mean]] 此时会显示np.sum和np.mean统计出来的数据。
            
  Columns   Columns类似Index可以设置列层次字段，它不是一个必要参数，作为一种分割数据的可选方式。

      #以 Pclass(船舱)为索引 查看不同船舱人员的平均存活率Survived。
      train_survived=train_content.pivot_table(index="Pclass",values="Survived")
      
      # 查看不同船舱的收费均值是多少
      train_age_fare=train_content.pivot_table(index="Pclass",values=["Age","Fare"])
      
      # 查看不同船舱人员的的人均年龄
      train_survived=train_content.pivot_table(index="Pclass",values="Age")
  
### icol和col 取范围
    
  iloc和loc的区别是 iloc只能跟整数，而loc可以跟数字
   
     print(train_content.iloc[83,3])     #找的是除title以外的第84行，因为数组默认是从0开始向上增长的
     print(train_content.iloc[82:83,3:5]) #去尾的83不包括 5不包括
     print(train_content.iloc[82:84,3:6]) #去尾的83不包括 5不包括

     print(train_content.loc[83,"Age"])
     print(train_content.loc[82:83,"Name":"Age"])   #还可以跟范围


### 查找 df 数据列中 列数据等于 x 长度的值

    # 找到在 genres 列中列长度等于7的数据
    train[train['genres'].str.len() == 7]


### 将Pandas中的DataFrame类型转换成Numpy中array类型的三种方法
  dataframe 转列表  
      
      
1、使用DataFrame中的values方法

    df.values
  
2、使用DataFrame中的as_matrix()方法

    df.as_matrix()

3、使用Numpy中的array方法

    np.array(df)

### pandas.mode() 

__返回出现频率最高的值 默认 axis=0，即每一特征中出现最高的值 默认忽略NA值，如果想将NA值计算进去可以使用 dropna=False__

__注意：如果存在频率相同的值会返回两个值__

__数据:__

    >>> df = pd.DataFrame([('bird', 2, 2),
    ...                    ('mammal', 4, np.nan),
    ...                    ('arthropod', 8, 0),
    ...                    ('bird', 2, np.nan)],
    ...                   index=('falcon', 'horse', 'spider', 'ostrich'),
    ...                   columns=('species', 'legs', 'wings'))
    >>> df
              species  legs  wings
    falcon        bird     2    2.0
    horse       mammal     4    NaN
    spider   arthropod     8    0.0
    ostrich       bird     2    NaN  

__例子1__

    >>> df.mode()
      species  legs  wings
    0    bird   2.0    0.0
    1     NaN   NaN    2.0

__例子2__

    >>> df.mode(dropna=False)
      species  legs  wings
    0    bird     2    NaN


### 删除缺失值：df.dropna()

    df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                      "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                      "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                               pd.NaT]})

    >>> df

          name        toy       born
    0    Alfred        NaN        NaT
    1    Batman  Batmobile 1940-04-25
    2  Catwoman   Bullwhip        NaT

__删除至少缺少一个元素的行__

    df.dropna()

       name        toy       born
    1  Batman  Batmobile 1940-04-25


__删除至少缺少一个元素的列。__

    df.dropna(axis='columns')

          name
    0    Alfred
    1    Batman
    2  Catwoman

__删除缺少所有元素的行。__

    >>> df.dropna(how='all')

          name        toy       born
    0    Alfred        NaN        NaT
    1    Batman  Batmobile 1940-04-25
    2  Catwoman   Bullwhip        NaT

__仅保留至少包含2个非NA值的行。__

    >>> df.dropna(thresh=2)

          name        toy       born
    1    Batman  Batmobile 1940-04-25
    2  Catwoman   Bullwhip        NaT

__删除某列中缺失值：__

    df['toy'].dropna()

    1    Batmobile
    2     Bullwhip
    Name: toy, dtype: object



### pandas.DataFrame.fillna 用指定的方法填充NA/NaN

__DataFrame.fillna（value = None，method = None，axis = None，inplace = False，limit = None，downcast = None，** kwargs ）__
        
  value ： 标量，字典，系列或DataFrame用于填充孔的值（例如0），或者用于指定每个索引（对于Series）或列（对于DataFrame）使用哪个值的Dict /Series / DataFrame。（不会填写dict / Series / DataFrame中的值）。该值不能是列表。
                 
  method :  {'backfill'，'bfill'，'pad'，'ffill'，None}，默认无   用于填充重新索引的填充孔的方法系列填充/填充
              
  axis : {0或'索引'，1或'列'}
  
  例子：
  
      >>> df = pd.DataFrame([[np.nan, 2, np.nan, 0],
      ...                    [3, 4, np.nan, 1],
      ...                    [np.nan, np.nan, np.nan, 5],
      ...                    [np.nan, 3, np.nan, 4]],
      ...                    columns=list('ABCD'))
      >>> df
           A    B   C  D
      0  NaN  2.0 NaN  0
      1  3.0  4.0 NaN  1
      2  NaN  NaN NaN  5
      3  NaN  3.0 NaN  4

   __用0替换所有NaN元素__
   
      >>> df.fillna(0)
          A   B   C   D
      0   0.0 2.0 0.0 0
      2   0.0 0.0 0.0 5
      3   0.0 3.0 0.0 4
      1   3.0 4.0 0.0 1

   __我们还可以向前或向后传播非空值。__

    >>> df.fillna(method='ffill')
        A   B   C   D
    0   NaN 2.0 NaN 0
    1   3.0 4.0 NaN 1
    2   3.0 4.0 NaN 5
    3   3.0 3.0 NaN 4

   __将“A”，“B”，“C”和“D”列中的所有NaN元素分别替换为0,1,2和3。__

    >>> values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    >>> df.fillna(value=values)
        A   B   C   D
    0   0.0 2.0 2.0 0
    1   3.0 4.0 2.0 1
    2   0.0 1.0 2.0 5
    3   0.0 3.0 2.0 4
    
  __只替换第一个NaN元素。__

    >>> df.fillna(value=values, limit=1)
        A   B   C   D
    0   0.0 2.0 2.0 0
    1   3.0 4.0 NaN 1
    2   NaN 1.0 NaN 5
    3   NaN 3.0 NaN 4
    
    
### pandas.DataFrame.groupby   
  
  DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False, **kwargs)[source]

*   __参数介绍：__
    
      as_index:为True时会将第一列数据设置为index，为False时则会新建一个数字索引。默认为True

        import pandas as pd

        df = pd.DataFrame(data={'books':['bk1','bk1','bk1','bk2','bk2','bk3'], 'price': [12,12,12,15,15,17]})

        df

        out：
            books	price
          0  bk1	  12
          1	 bk1	  12
          2	 bk1	  12
          3	 bk2	  15
          4	 bk2	  15
          5	 bk3	  17

        a=df.groupby('books', as_index=True).sum()
        print(a.index)
        a

        out：

          Index(['bk1', 'bk2', 'bk3'], dtype='object', name='books')

                price
          books	
          bk1	    36
          bk2	    30
          bk3	    17

        df.groupby('books', as_index=False).sum() 
        
        out： 

            books	price
          0	bk1	  36
          1	bk2	  30
          2	bk3	  17

    __groupby操作涉及拆分对象，应用函数和组合结果的某种组合。这可用于对这些组上的大量数据和计算操作进行分组。__
    
    __使用groupby进行切片之后，我们如果进行操作其实是在那个切片(split)中进行的操作，计算完成之后返回合并结果(Combine) 如图：__


<div align=center><img width="650" height="300" src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/pandas/2.png"/></div>

*   __groupby函数 例子1__

        import pandas as pd
        import numpy as np

        dict_obj = {'key1' : ['a', 'b', 'a', 'b', 
                              'a', 'b', 'a', 'a'],
                    'key2' : ['one', 'one', 'two', 'three',
                              'two', 'two', 'one', 'three'],
                    'data1': np.random.randn(8),
                    'data2': np.random.randn(8)}
        df_obj = pd.DataFrame(dict_obj)
        print(df_obj)

    __out：__

        key1   key2     data1     data2
        0    a    one -0.109110  0.528666
        1    b    one -0.746051  1.994562
        2    a    two  2.685447  1.672294
        3    b  three  0.546663 -0.970285
        4    a    two -0.859890 -0.964093
        5    b    two -0.347244  0.146132
        6    a    one  0.254899  0.830872
        7    a  three -0.958547 -2.016811


*   __dataframe根据key1进行分组__                          
                                                                                     
       grouped1=df_obj.groupby('key1')

        [x for x in grouped1]


        [('a',   key1   key2     data1     data2
          0       a    one -0.109110  0.528666
          2       a    two  2.685447  1.672294
          4       a    two -0.859890 -0.964093
          6       a    one  0.254899  0.830872
          7       a  three -0.958547 -2.016811), ('b',   key1   key2     data1     data2
          1       b    one -0.746051  1.994562
          3       b  three  0.546663 -0.970285
          5       b    two -0.347244  0.146132)]

*   __使用groupby指定字段内容进行运算__

    __如：__

        # 按照 key1 进行分组从上面的数据中我们可以发现分为a,b两组
        grouped = df.groupby(df['key1'])
        grouped.mean()

    __out：__

        # 这里使用 df['key1'] 做了分组键，即按 a 和 b 进行分组。下例中没有显示 key2 列，是因为其值不是数字类型，被 mean() 方法自动忽视了
            data1	data2
        key1		
        a	0.202560	0.010185
        b	-0.182211	0.390136
        
    __如：__ 

        # 以key1进行分组，将data2字段中的内容进行求和
        grouped1=df_obj.groupby(['key1'])['data2'].sum()
        grouped1

    __out：__

        key1
        a    0.050927
        b    1.170409
        Name: data2, dtype: float64

    __如：__ 注意使用groupby进行多列的组合时，顺序会影响我们的分组效果 如groupby(['key1','key2']) 和groupby(['key2','key1'])展示出来的效果就会不同

        # 以key1，和key2 进行分组，将data2字段中的内容进行求和
        grouped1=df_obj.groupby(['key1','key2'])['data2'].sum()
        grouped1

    __out：__

        key1  key2 
        a     one      1.359537
              three   -2.016811
              two      0.708200
        b     one      1.994562
              three   -0.970285
              two      0.146132


    __如：__

        # 以Pclass进行分组，将字段中'Pclass','Survived'的内容进行求和
        print(train_data.groupby(['Pclass'])['Pclass','Survived'].mean())
        
                  Pclass    Survived
        Pclass                  
        1          1.0      0.629630
        2          2.0      0.472826
        3          3.0      0.242363
      
        print(train_data.groupby(['Pclass'])['Pclass'，'Survived','Age'].mean())

                  Pclass    Survived        Age
        Pclass                             
        1          1.0      0.629630      37.048118
        2          2.0      0.472826      29.866958
        3          3.0      0.242363      26.403259


*   __分层索引__

        我们可以使用level参数对不同级别的层次索引进行分组：

        >>> arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
        ...           ['Capitve', 'Wild', 'Capitve', 'Wild']]
        >>> index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
        >>> df = pd.DataFrame({'Max Speed' : [390., 350., 30., 20.]},
        ...                    index=index)
        >>> df
                        Max Speed
        Animal Type
        Falcon Capitve      390.0
              Wild         350.0
        Parrot Capitve       30.0
              Wild          20.0

        >>> df.groupby(level=0).mean()
                Max Speed
        Animal
        Falcon      370.0
        Parrot       25.0

        >>> df.groupby(level=1).mean()
                Max Speed
        Type
        Capitve      210.0
        Wild         185.0

*   __groupby 函数的两个方法 .size() .count()__

    可以使用 GroupBy 对象（不论是 DataFrameGroupBy 还是 SeriesGroupBy）的 .size() 方法查看分组大小：

    __.size 如:__

        grouped.size()

    __out：__

        key1
        a       3
        b       2

    __.count 如：__

        grouped.count()

    __out：__

            key2	data1	data2
        key1			
        a	  5	    5	    5
        b	  3	    3	    3

    __.size 和 .count的区别： size计数时包含NaN值，而count不包含NaN值__


*   __groupby.first()__

    首先计算每组中的值

    __例子：__

        train.groupby('matchId')['matchType'].value_counts()

    __out__

        matchId         matchType       
        0000a43bce5eec  squad-fpp            95
        0000eb01ea6cdd  squad-fpp            98
        0002912fe5ed71  solo                 95
        0003b92987589e  duo                 100
        0006eb8c17708d  duo-fpp              93
        00077604e50a63  squad-fpp            98


    __例子：__

    首先使用 groupby('matchId') ,将 matchId 作为索引，后面接 matchType , first的作用在于，因为 某一个 matchId 下面可能有多个 matchType ，而first()只取第一个 matchType的值 。

        train.groupby('matchId')['matchType'].first().value_counts()

    __out__

        squad-fpp           18576
        duo-fpp             10620
        squad                6658
        solo-fpp             5679
        duo                  3356
        solo                 2297
        normal-squad-fpp      358
        normal-duo-fpp        158
        normal-solo-fpp        96
        crashfpp               73
        flaretpp               29
        normal-solo            23
        normal-squad           16
        normal-duo             12
        flarefpp                9
        crashtpp                5
        Name: matchType, dtype: int64

### pd.to_frame

pd.to_frame 将 Series 转化为 dataframe

*   __例子__

        train.groupby(['matchType','matchId']).count().groupby(['matchType','matchId']).size().shape
      
        group = train.groupby(['matchType','matchId','groupId']).count().groupby(['matchType','matchId']).size().to_frame('groups in match')
        print(group)

        group.shape
    __out__

        (47965,)

                              groups in match
        matchType	  matchId	
        duo	        0003b92987589e	  47
                    0006eb8c17708d	  44
                    00086c74bb4efc	  48
        (47965,1)

    我们可以通过 shape 查看他到底是不是 series，只有 series 才可以进行 to_farme.




### pd.cut 为数据分段：

  需要将数据值分段并排序到箱中时使用cut。此函数对于从连续变量转换为分类变量也很有用。例如，cut可以将年龄转换为年龄范围组。支持分箱到相同数量的箱柜或预先指定的箱柜阵列。

  pandas.cut（x，bins，right = True，labels = None，retbins = False，precision = 3，include_lowest = False，duplicates ='raise' ）

__参数介绍：__
    
    x: 数据
    
    bins：进行划分的一维数组
      
      当 bins 为 整数时,将x划分为多少个等间距的区间

      当 bins 为 序列时,将x划分在指定的序列中，若不在该序列中，则是NaN

    right：是否包含右端点

    labels : 是否用标记来代替返回的bins

    precision: 精度

    include_lowest:是否包含左端点

__例子：__

*   当bins为整数时：将数据分为三份等间距的区间

      pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3)

          [(0.994, 3.0], (5.0, 7.0], (3.0, 5.0], (3.0, 5.0], (5.0, 7.0], (0.994, 3.0]]  # 输出的数据区间划分
          Categories (3, interval[float64]): [(0.994, 3.0] < (3.0, 5.0] < (5.0, 7.0]]   # 3份等间距区间

*   当bins为以序列时，可以看到1不属于我们2-4区间，也不属于4-6区间，也不属于6-8区间，所以输出的内容为NAN

        pd.cut(np.array([1, 7, 5, 4, 6, 3]), [2,4,6,8]) 

          [NaN, (6.0, 8.0], (4.0, 6.0], (2.0, 4.0], (4.0, 6.0], (2.0, 4.0]]
          Categories (3, interval[int64]): [(2, 4] < (4, 6] < (6, 8]]

*   给不同区间赋值

        pd.cut(np.array([1, 7, 5, 4, 6, 3]), [2,4,6,8],labels=['2到4区间','4到6区间','6到8区间']) 
        
          [NaN, 6到8区间, 4到6区间, 2到4区间, 4到6区间, 2到4区间]
          Categories (3, object): [2到4区间 < 4到6区间 < 6到8区间]

  ### pandas按若干个列的组合条件筛选数据
    #取年龄等于26，并且存活的数据的数量
    print(train_data[(train_data['Age']==29) & (train_data['Survived']==1)].count())

  ### pandas一次显示指定的多个标签 
    #使用 [[ ]] 两层嵌套括号 比如 
    print(train_data[['Survived','Age']])
    print("%s "%(new_user_data[new_user_data['节']==section][['名字','知识点']].values))


  ### 筛选出特定字符串的列

    [col for col in train.columns if 'str' in col]

  ### 过滤出包含某个字符串的列信息 df.filter()

    #过滤出包含 matchType 字符串的所有列
    matchType_encoding = train.filter(regex='matchType')

  ### pandas.Series.map
    
    根据输入的对应关系映射系列的值。

    用于将系列中的每个值替换为另一个值，该值可以从函数，a dict或a 派生Series。
  
  __例子：__
  
      >>> s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])
      >>> s
      0      cat
      1      dog
      2      NaN
      3   rabbit
      dtype: object
  
  map接受a dict或a Series。除非dict具有默认值（例如），否则将dict转换为未找到的NaN值defaultdict：
  
      >>> s.map({'cat': 'kitten', 'dog': 'puppy'})
      0   kitten
      1    puppy
      2      NaN
      3      NaN
      dtype: object
      
  __它还接受一个功能：__

    >>> s.map('I am a {}'.format)
    0       I am a cat
    1       I am a dog
    2       I am a nan
    3    I am a rabbit
    dtype: object
  
  为避免将函数应用于缺失值（并将其保留为 NaN），na_action='ignore'可以使用：

    >>> s.map('I am a {}'.format, na_action='ignore')
    0     I am a cat
    1     I am a dog
    2            NaN
    3  I am a rabbit
    dtype: object

  ### pandas to_dict

  __例子：__
    
    train_feature=vec.fit_transform(data.to_dict(orient='record'))

    orient参数不同会有不一样的效果 

    https://blog.csdn.net/m0_37804518/article/details/78444110


    
  ### python dataframe 获得 列名columns 和行名称 index
   
    dfname._stat_axis.values.tolist()   ==  dfname.index.values.tolist()      # 行名称
     
    
    dfname.columns.values.tolist()    # 列名称

  ### python dataframe 当读取csv文件，但csv数据中无列名时进行赋值列名

  __错误示范：__

    data=pd.read_csv('filepath')
    # 为数据增加一行列名
    column=['user_id','名字','知识点','节','课程','course_id']
    data.columns=column

  __正确示范：__

    data=pd.read_csv('filepath'，header=None)
    # 为数据增加一行列名
    column=['user_id','名字','知识点','节','课程','course_id']
    data.columns=column

  不加 header=None ，在进行read_csv之后，默认会将第一行数据设置为列名，此时如果直接进行 data.columns=column 那么第一行数据被替换成我们指定的列名，这样我们的数据就变少了，如果加上了header=None,那么读取之后的数据是没有列名的(第一行数据还是数据，不会成为列名)，此时我们进行命名列名就不会替换掉我们的数据。


  ### 构造DataFrame

   __例子：__ 如果想要构造这样的dataframe：

   <div align=center><img src="https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/pandas/1.jpg"/></div> 

      import pandas as pd

      list1=[[1,2,3],[4,5,6],[7,8,9]]

      dict={'id':[1,2,3],'item':[[5,6,7,8],[1,2,3],[4,5,6]]}

      data=pd.DataFrame(data=dict,columns=['id','item'])

      print(data)


  ### pandas 错误警告：

    在使用pd.read_csv()时 出现了如下的错误

      data=pd.read_csv(file_path)

      pandas.errors.ParserError: Error tokenizing data. C error: Expected 20 fields in line 4, saw 21

  __解决方案1：__ 加上分隔符 sep 

      data=pd.read_csv(file_path,sep='\t')

  __解决方案2：__ 忽略错误的行

      data=pd.read_csv(file_path,error_bad_lines=False)

  


  ### 数据的偏度和峰度

  __df.skew()  偏度__

    Definition:是描述数据分布形态的统计量，其描述的是某总体取值分布的对称性，简单来说就是数据的不对称程度。
    偏度是三阶中心距计算出来的。
    （1）Skewness = 0 ，分布形态与正态分布偏度相同。
    （2）Skewness > 0 ，正偏差数值较大，为正偏或右偏。长尾巴拖在右边，数据右端有较多的极端值。
    （3）Skewness < 0 ，负偏差数值较大，为负偏或左偏。长尾巴拖在左边，数据左端有较多的极端值。
    （4）数值的绝对值越大，表明数据分布越不对称，偏斜程度大。


  __df.kurt()  峰度__

    Definition:偏度是描述某变量所有取值分布形态陡缓程度的统计量，简单来说就是数据分布顶的尖锐程度。
    峰度是四阶标准矩计算出来的。
    （1）Kurtosis=0 与正态分布的陡缓程度相同。
    （2）Kurtosis>0 比正态分布的高峰更加陡峭——尖顶峰
    （3）Kurtosis<0 比正态分布的高峰来得平缓——平顶峰

  ### pandas 计算矩阵关系系数

  使用.corr() 可以用于计算矩阵关系系数，可以使用得到的关系系数绘制热力图
    
  __举例：__

    现在我们有一些数据，我们要计算这些特征之间的关系
    
    corrmat = train_data.drop('Id',axis=1).corr()   # train_data 是read_cav()读取进来的数据
    corrmat

  __out__

    	            MSSubClass	LotFrontage	  LotArea	 OverallQual  OverallCond

    MSSubClass	  1.000000	  -0.386347	  -0.139781	  0.032628	  -0.059316	
    LotFrontage	  -0.386347 	1.000000	  0.426095	  0.251646	  -0.059213	
    LotArea	      -0.139781	  0.426095	  1.000000	  0.105806	  -0.005636	
    OverallQual	  0.032628	  0.251646  	0.105806	  1.000000	  -0.091932	
    OverallCond   -0.059316	  -0.059213	  -0.005636 	-0.091932	  1.000000	

  __绘制热力图__

    fig,ax=plt.subplots(figsize=(20,16))
    sns.heatmap(corrmat,annot=True,fmt ='.1')
    plt.show()


### df.to_sql df写到数据库：

  将df数据写入数据库

__案例：__

    import MySQLdb
    import pandas as pd
    from sqlalchemy import create_engine

    host = '127.0.0.1'
    port = 3306
    db = 'db_name'
    user = 'db_user'
    password = 'db_user_password'
    
    # ?charset=utf8 表示使用utf8字符集
    engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8") % (user, password, host, db))

    try:
        # 将数据写入test1表，如果表存在就进行替换，如果数据库的编码格式为latin，并且数据中存在中文，会报乱码。
        Associate_dknowledge.to_sql('test1',con=engine,if_exists='replace',index=False)
    except Exception as e:
        print(e)

__df.to_sql暂时还不支持我们设置主键__

    如果想要设置主键：加上 标记为 <---- 的两句

    import MySQLdb
    import pandas as pd
    from sqlalchemy import create_engine

    host = '127.0.0.1'
    port = 3306
    db = 'db_name'
    user = 'db_user'
    password = 'db_user_password'
    
    # ?charset=utf8 表示使用utf8字符集
    engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8") % (user, password, host, db))
    conn = engine.connect()     <-------

    try:
        # 将数据写入test1表，如果表存在就进行替换，如果数据库的编码格式为latin，并且数据中存在中文，会报乱码。
        Associate_dknowledge.to_sql('test1',con=engine,if_exists='replace',index=True)
        conn.execute('alter table `{}` add primary key(`index`)'.format(file_name))       <-------

    except Exception as e:
        print(e)


__df.to_sql if_exists='append' 时防止主键冲突__
  
  为了防止主键重复，于是我们修改原先的数据中的index，让其接着数据库中最大index往下排序

    import MySQLdb
    import pandas as pd
    from sqlalchemy import create_engine

    host = '127.0.0.1'
    port = 3306
    db = 'db_name'
    user = 'db_user'
    password = 'db_user_password'

    engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8") % (user, password, host, db))
    conn = engine.connect()
    Session = sessionmaker(bind=engine)

    def df_to_sql(test1,data,flag): 
        session = Session(bind=conn)
        # 通过flag表示是否更新表，如果更新就替换之前的表，否则追加
        print('flag: ',flag)
        # 如果是更新表，则覆盖原有表
        if flag==True:
            method='replace'
            data.to_sql(test1,con=engine,if_exists=method,index=True)
        # 如果是追加数据，则追加
        else:
            method='append'
            try:
                result=session.execute('SELECT COUNT(*) FROM `test1`') 
                """ 为了防止主键重复，于是我们修改原先的数据中的index，让其接着数据库中最大index往下排序"""
                data_len=len(data)
                sql_data_len=result.fetchall()[0][0]
                data.index=np.arange(sql_data_len, sql_data_len+data_len)
                print(data)
                data.to_sql(test1,con=engine,if_exists=method,index=True)
                session.commit()
                session.close()
            except Exception as e:
                print(e)


    def set_primary_key(course_name):
      try:
          conn.execute('alter table test1 add primary key(`index`)') 
      except Exception as e:
          print(e)

#### 注意：

这里我们最好使用session会话，这样我们进行一次修改之后就会提交一次事务，否则可能造成事务未提交的情况，这个时候如果我们还留有事务，但是此时如果我们要进行表的替换replace，那么因为之前存在事务，但是我们要尝试去删表，就会造成metadata lock，就会阻塞，所以我们采用session，及时进行事务的提交。



### 数据库数据转为df：

    import pandas as pd
    import pymysql
    import sqlalchemy
    from sqlalchemy import create_engine

    host = '127.0.0.1'
    port = 3306
    db = 'db_name'
    user = 'db_user'
    password = 'db_user_password'

    # 1. 用sqlalchemy构建数据库链接engine
    engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8") % (user, password, host, db))
    # sql 命令
    sql_cmd = "SELECT * FROM table"
    df = pd.read_sql(sql=sql_cmd, con=engine)

    # 2. 用DBAPI构建数据库链接engine
    con = pymysql.connect(host=localhost, user=username, password=password, database=dbname, charset='utf8', use_unicode=True)
    df = pd.read_sql(sql_cmd, con)

  


  ### pandas的拼接循环：

  举个例子：

    现在有两个df数据 train_df 和 test_df 

    现在 combine=[train_df,test_df]

    for dataset in combine:
        dataset['Title']=dataset.Name.str.extract('([A-Za-z]+)\.',expand=False)

  这里的 for dataset in combine 其实只是循环了两次，第一次是train_data 第二次是test_data数据，其实上就是操作修改我们train_data和test_data，之后输出train_df 我们会发现其多了一个特征 ‘Title’ 。

### df.copy()

  __复制此对象的索引和数据。__

  当deep=True（默认）时，将使用调用对象的数据和索引的副本创建新对象。对副本的数据或索引的修改不会反映在原始对象中（请参阅下面的注释）。

  何时deep=False，将创建一个新对象而不复制调用对象的数据或索引（仅复制对数据和索引的引用）。对原始数据的任何更改都将反映在浅层副本中（反之亦然）。

  __例子：__

    a=train_data['Survived']
    b=train_data['Survived']
    print(a.tail())
    print(b.tail())
    
    a:                             b:

    886    0                      886    0
    887    1                      887    1
    888    0                      888    0
    889    1                      889    1
    890    0                      890    0
    Name: Survived, dtype: int64  Name: Survived, dtype: int64
    
__现在我们没有进行deepcopy，我们修改b的数据，a的数据也会发生修改，所以我们如果要保持a和b数据独立，我们必须deepcopy__

    b['haha']=1           
    b.tail(1)

    haha    1
    Name: Survived, dtype: int64
    
    a.tail(1)

    haha    1
    Name: Survived, dtype: int64
      
__如果要使用deepcopy，使用df.copy(deep=True)即可__


### df 追加数据

__例子：__

    df = df.append(df2)
    


### df.quantile
####  分位数解释

__四分位数__

__概念：__ 把给定的乱序数值由小到大排列并分成四等份，处于三个分割点位置的数值就是四分位数。

__第1四分位数 (Q1)__， 又称“较小四分位数”，等于该样本中所有数值由小到大排列后第25%的数字。

__第2四分位数 (Q2)__，又称“中位数”，等于该样本中所有数值由小到大排列后第50%的数字。

__第3四分位数 (Q3)__，又称“较大四分位数”，等于该样本中所有数值由小到大排列后第75%的数字。

__四分位距__（InterQuartile Range, IQR）= 第3四分位数与第1四分位数的差距

*   __确定p分位数位置的两种方法__

    position = (n+1)*p    - 箱型图采用的计算方法

    position = 1 + (n-1)*p  - python中计算分位数位置的方案

    其中 n 表示序列中包含的项数。也就是有多少个数。

在python中计算分位数位置的方案采用 __position=1+(n-1)*p__

__案例1__

    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.array([[1, 1], [2, 10], [3, 100], [4, 100]]), columns=['a', 'b'])
    print("数据原始格式：")
    print(df)
    print("计算p=0.1时，a列和b列的分位数")
    print(df.quantile(.1))

__data:__

    序号	a	   b
    0	    1	  2
    1	    2	  10
    2	    3	  100
    3	    4	  100

__程序计算结果：__

    计算p=0.1时，a列和b列的分位数
    a 1.3
    b 3.7
    Name: 0.1, dtype: float64

__手算计算结果：__

    计算a列
    pos = 1 + (4 - 1)*0.1 = 1.3
    fraction = 0.3
    ret = 1 + (2 - 1) * 0.3 = 1.3
    计算b列
    pos = 1.3
    ret = 2 + (10 - 2)* 0.3 = 4.4

__解释：__

1、首先根据公式 <position=1+(n-1)*p> ，因为a列有 4个项数，所以我们可以得到 pos = 1 + (4 - 1)*0.1 = 1.3 。

2、然后 fraction 是pos的分数位，即0.3。

3、接着 我们将数据进行排序，因为我们这里就是已经排序完成的数据了，就忽略这一步。

4、因为 pos为 1.3，项数位置在 第一项 和 第二项 之间 ( 1< 1.3 <2 )

5、所以那 i 就是 2 ，j 就是10，也就是b列表中的第一项 2 和第二个项 10 。

6、然后我们就可以返回 .1分位数的值，也就是 i + (j-i) * fraction = ret = 2 + (10 - 2)* 0.3 = 4.4 ，也就是前 10% 的数据。

__案例2__

    import pandas as pd
    import numpy as np
    dt = pd.Series(np.array([6, 47, 49, 15, 42, 41, 7, 39, 43, 40, 36])
    print("数据格式：")
    print(dt)
    print('Q1:', df.quantile(.25))
    print('Q2:', df.quantile(.5))
    print('Q3:', df.quantile(.75))

__计算结果__

    Q1: 25.5
    Q2: 40.0
    Q3: 42.5

  ## 总结：
  
   和 NumPy 一样，Pandas 有两个非常重要的数据结构：Series 和 DataFrame。使用 Pandas 可以直接从 csv 或 xlsx 等文件中导入数据，以及最终输出到 excel 表中。
   
   Pandas 包与 NumPy 工具库配合使用可以发挥巨大的威力，正是有了 Pandas 工具，Python 做数据挖掘才具有优势。
  
  
  
