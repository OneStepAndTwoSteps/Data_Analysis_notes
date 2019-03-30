# 可视化工具Seaborn和Matplotlib

## 4类主要的可视化视图
    
    比较：比较数据间各类别的关系，或者是它们随着时间的变化趋势，比如折线图；
    
    联系：查看两个或两个以上变量之间的关系，比如散点图；
    
    构成：每个部分占整体的百分比，或者是随着时间的百分比变化，比如饼图；
    
    分布：关注单个变量，或者多个变量的分布情况，比如直方图。

单变量可视化视图：
  
    一次值关注一个变量。如我们一次只关注身高变量，来看身高的取值分布，而暂时忽略其他变量。
  
多变量可视化视图：
    
    可以让一张图同时查看两个以上的变量，比如“身高”和“年龄”，你可以理解是同一个人的两个参数，这样在同一张图中可以看到每个人的“身高”和“年龄”的取值，从而分析出这两个变量之前是否存在某种联系。
    
    
离散变量和连续变量：

    离散变量是指其数值只能用自然数或整数单位计算的则为离散变量. 例如,企业个数,职工人数,设备台数等,只能按计量单位数计数,这种变量的数值一般用计数方法取得. 反之,在一定区间内可以任意取值的变量叫连续变量,其数值是连续不断的,相邻两个数值可作无限分割,即可取无限个数值.
  
    针对离散变量我们可以使用常见的条形图和饼图完成数据的可视化工作，那么，针对数值型变量，我们也有很多可视化的方法，例如箱线图、直方图、折线图、面积图、散点图等等。
    
    
    
## 散点图：

  引入工具包，Matplotlib的pyplot包
  
     import matplotlib.pyplot as plt
     
 在工具包引用后，画散点图，需要使用 plt.scatter(x, y, marker=None) 函数。x、y 是坐标，marker 代表了标记的符号。比如“x”、“>”或者“o”。选择不同的 marker，呈现出来的符号样式也会不同(就是以指定的符号当成点画图)，你可以自己试一下。

 或使用工具包seaborn
  
    import seaborn as sns
    
在引用 seaborn 工具包之后，就可以使用 seaborn 工具包的函数了。如果想要做散点图，可以直接使用 sns.jointplot(x, y, data=None, kind=‘scatter’) 函数。其中 x、y 是 data 中的下标。data 就是我们要传入的数据，一般是 DataFrame 类型。kind 这类我们取 scatter，代表散点的意思。当然 kind 还可以取其他值，这个我在后面的视图中会讲到，不同的 kind 代表不同的视图绘制方式。

例子：
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    # 数据准备
    N = 1000
    x = np.random.randn(N)
    y = np.random.randn(N)
    # 用 Matplotlib 画散点图
    plt.scatter(x,y,marker="x")
    plt.show()
    #用seaborn画图
    df=pd.DataFrame({'x':x,'y':y})
    sns.joinplot(x='x',y='y',data=df,kind='scatter',marker='x')
    #sns还是要借助pyplot来打印图的 其自身无show方法
    plt.show    
    
运行结果：
  
  Matplotlib:   
  
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/M%E6%95%A3%E7%82%B9%E5%9B%BE.png)
  
  
  seaborn:    
  
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/S%E6%95%A3%E7%82%B9%E5%9B%BE.png)
  
  
  
## 折线图：
  
  折线图可以用来表示数据随着时间变化的趋势。
  
  在 Matplotlib 中，我们可以直接使用 plt.plot() 函数，当然需要提前把数据按照 x 轴的大小进行排序，要不画出来的折线图就无法按照 x 轴递增的顺序展示。
  
  在 Seaborn 中，我们使用 sns.lineplot (x, y, data=None) 函数。其中 x、y 是 data 中的下标。data 就是我们要传入的数据，一般是 DataFrame 类型。
  
  例子：
  
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    # 数据准备
    x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
    # 使用 Matplotlib 画折线图
    plt.plot(x, y)
    plt.show()
    # 使用 Seaborn 画折线图
    df = pd.DataFrame({'x': x, 'y': y})
    sns.lineplot(x="年", y="月", data=df)
    plt.show()

  运行结果：
  
  M:  
  
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/M%E6%8A%98%E7%BA%BF%E5%9B%BE.png)
  
  
  
  
  
  ## 直方图：
  
  直方图是比较常见的视图，它是把横坐标等分成了一定数量的小区间，这个小区间也叫作“箱子”，然后在每个“箱子”内用矩形条（bars）展示该箱子的箱子数（也就是 y 值），这样就完成了对数据集的直方图分布的可视化。
  
  在 Matplotlib 中，我们使用 plt.hist(x, bins=10) 函数，其中参数 x 是一维数组，bins 代表直方图中的箱子数量，默认是 10。
  
  在 Seaborn 中，我们使用 sns.distplot(x, bins=10, kde=True) 函数。其中参数 x 是一维数组，bins 代表直方图中的箱子数量，kde 代表显示核密度估计，默认是 True，我们也可以把 kde 设置为 False，不进行显示。核密度估计是通过核函数帮我们来估计概率密度的方法。
  
  例子：
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    # 数据准备
    a = np.random.randn(100)
    s = pd.Series(a) 
    # 用 Matplotlib 画直方图
    plt.hist(s)
    plt.show()
    # 用 Seaborn 画直方图
    sns.distplot(s, kde=False)
    plt.show()
    sns.distplot(s, kde=True)
    plt.show()


  运行结果：
  
  M:  
  
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/M%E6%96%B9%E5%BD%A2%E5%9B%BE.png)
  
  
  S:   
  
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/S%E6%96%B9%E5%BD%A2%E5%9B%BE.png)
  
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/S%E6%96%B9%E5%BD%A2%E5%9B%BE2.png)
  
  
  
  ## 条形图
    
    条形图可以帮我们查看类别的特征。在条形图中，长条形的长度表示类别的频数，宽度表示类别。
  
  在 Matplotlib 中，我们使用 plt.bar(x, height) 函数，其中参数 x 代表 x 轴的位置序列，height 是 y 轴的数值序列，也就是柱子的高度。
  
  在 Seaborn 中，我们使用 sns.barplot(x=None, y=None, data=None) 函数。其中参数 data 为 DataFrame 类型，x、y 是 data 中的变量。
  
  
  例子：
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    # 数据准备
    x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
    y = [5, 4, 8, 12, 7]
    # 用 Matplotlib 画条形图
    plt.bar(x, y)
    plt.show()
    # 用 Seaborn 画条形图
    sns.barplot(x, y)
    plt.show()

  
  运行结果：
  
   M：   
   
 ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/M%E6%9D%A1%E5%BD%A2%E5%9B%BE.png)
  
   S:  
   
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/S%E6%9D%A1%E5%BD%A2%E5%9B%BE.png)
  
  
## 箱型图：
    
  箱线图，又称盒式图，由五个数值点组成：最大值 (max)、最小值 (min)、中位数 (median) 和上下四分位数 (Q3, Q1)。它可以帮我们分析出数据的差异性、离散程度和异常值等。
    
  在 Matplotlib 中，我们使用 plt.boxplot(x, labels=None) 函数，其中参数 x 代表要绘制箱线图的数据，labels 是缺省值，可以为箱线图添加标签。
  
  在 Seaborn 中，我们使用 sns.boxplot(x=None, y=None, data=None) 函数。其中参数 data 为 DataFrame 类型，x、y 是 data 中的变量。
  
  
  例子：
  
    # 数据准备
    # 生成 0-1 之间的 10*4 维度数据
    data=np.random.normal(size=(10,4)) 
    lables = ['A','B','C','D']
    # 用 Matplotlib 画箱线图
    plt.boxplot(data,labels=lables)
    plt.show()
    # 用 Seaborn 画箱线图
    df = pd.DataFrame(data, columns=lables)
    sns.boxplot(data=df)
    plt.show()

  运行结果：
  
  M:   
  
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/M%E7%AE%B1%E5%9E%8B%E5%9B%BE.png)
  S:    
  
   ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/S%E7%AE%B1%E5%9E%8B%E5%9B%BE.png)
  
##  饼图

  饼图是常用的统计学模块，可以显示每个部分大小与总和之间的比例。在 Python 数据可视化中，它用的不算多。我们主要采用 Matplotlib 的 pie 函数实现它。
  
  在 Matplotlib 中，我们使用 plt.pie(x, labels=None) 函数，其中参数 x 代表要绘制饼图的数据，labels 是缺省值，可以为饼图添加标签。
  
  这里我设置了 lables 数组，分别代表高中、本科、硕士、博士和其他几种学历的分类标签。nums 代表这些学历对应的人数。
  
  
  例子：
      
      import matplotlib.pyplot as plt
      # 数据准备
      nums = [25, 37, 33, 37, 6]
      labels = ['High-school','Bachelor','Master','Ph.d', 'Others']
      # 用 Matplotlib 画饼图
      plt.pie(x = nums, labels=labels)
      plt.show()

  运行结果：
  
   S:    
   
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/S%E9%A5%BC%E5%9B%BE.png) 
    
    
 ## 热力图：
 
  热力图，英文叫 heat map，是一种矩阵表示方法，其中矩阵中的元素值用颜色来代表，不同的颜色代表不同大小的值。通过颜色就能直观地知道某个位置上数值的大小。另外你也可以将这个位置上的颜色，与数据集中的其他位置颜色进行比较。
 
 热力图是一种非常直观的多元变量分析方法。
 
 
 我们一般使用 Seaborn 中的 sns.heatmap(data) 函数，其中 data 代表需要绘制的热力图数据。
 
 这里我们使用 Seaborn 中自带的数据集 flights，该数据集记录了 1949 年到 1960 年期间，每个月的航班乘客的数量。

 例子
 
    import matplotlib.pyplot as plt
    import seaborn as sns
    # 数据准备
    flights = sns.load_dataset("flights")
    data=flights.pivot('year','month','passengers')
    # 用 Seaborn 画热力图
    sns.heatmap(data)
    plt.show()

 运行结果
    
    通过 seaborn 的 heatmap 函数，我们可以观察到不同年份，不同月份的乘客数量变化情况，其中颜色越浅的代表乘客数量越多，如下图所示：
  
  S:    
  
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/S%E7%83%AD%E5%8A%9B%E5%9B%BE.png)
 
 
 ## 蜘蛛图：
  
  蜘蛛图是一种显示一对多关系的方法。在蜘蛛图中，一个变量相对于另一个变量的显著性是清晰可见的。
  
  假设我们想要给王者荣耀的玩家做一个战力图，指标一共包括推进、KDA、生存、团战、发育和输出。那该如何做呢？
  
  这里我们需要使用 Matplotlib 来进行画图，首先设置两个数组：labels 和 stats。他们分别保存了这些属性的名称和属性值。
  
  因为蜘蛛图是一个圆形，你需要计算每个坐标的角度，然后对这些数值进行设置。当画完最后一个点后，需要与第一个点进行连线。
  
  因为需要计算角度，所以我们要准备 angles 数组；又因为需要设定统计结果的数值，所以我们要设定 stats 数组。并且需要在原有 angles 和 stats 数组上增加一位，也就是添加数组的第一个元素。
  
  
  例子：
    
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from matplotlib.font_manager import FontProperties  
    # 数据准备
    labels=np.array([u" 推进 ","KDA",u" 生存 ",u" 团战 ",u" 发育 ",u" 输出 "])
    stats=[83, 61, 95, 67, 76, 88]
    # 画图数据准备，角度、状态值
    # endpoint是一个bool类型的值，如果为"Ture",“stop"是最后一个值，如果为"False”,生成的数组不会包含"stop"值,白话就是True时右闭，False右开。
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    # numpy.concatenate((a1, a2, ...), axis=0, out=None) 目的就是将两个数组拼接在一起
    stats=np.concatenate((stats,[stats[0]]))
    angles=np.concatenate((angles,[angles[0]]))
    # 用 Matplotlib 画蜘蛛图
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)   
    ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.25)
    # 设置中文字体
    font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)  
    ax.set_thetagrids(angles * 180/np.pi, labels, FontProperties=font)
    plt.show()
    
    
代码中 flt.figure 是创建一个空白的 figure 对象，这样做的目的相当于画画前先准备一个空白的画板。然后 add_subplot(111) 可以把画板划分成 1 行 1 列。再用 ax.plot 和 ax.fill 进行连线以及给图形上色。最后我们在相应的位置上显示出属性名。这里需要用到中文，Matplotlib 对中文的显示不是很友好，因此我设置了中文的字体 font，这个需要在调用前进行定义。最后我们可以得到下面的蜘蛛图，看起来是不是很酷？

运行结果：
     
  M：     
  
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/M%E8%9C%98%E8%9B%9B%E5%9B%BE.png)
      
  
  
## 二元变量分布

如果我们想要看两个变量之间的关系，就需要用到二元变量分布。当然二元变量分布有多种呈现方式，开头给你介绍的散点图就是一种二元变量分布。

在 Seaborn 里，使用二元变量分布是非常方便的，直接使用 sns.jointplot(x, y, data=None, kind) 函数即可。其中用 kind 表示不同的视图类型：“kind=‘scatter’”代表散点图，“kind=‘kde’”代表核密度图，“kind=‘hex’ ”代表 Hexbin 图，它代表的是直方图的二维模拟。

这里我们使用 Seaborn 中自带的数据集 tips，这个数据集记录了不同顾客在餐厅的消费账单及小费情况。代码中 total_bill 保存了客户的账单金额，tip 是该客户给出的小费金额。我们可以用 Seaborn 中的 jointplot 来探索这两个变量之间的关系。

例子：
  
    import matplotlib.pyplot as plt
    import seaborn as sns
    # 数据准备
    tips = sns.load_dataset("tips")
    print(tips.head(10))
    # 用 Seaborn 画二元变量分布图（散点图，核密度图，Hexbin 图）
    sns.jointplot(x="total_bill", y="tip", data=tips, kind='scatter')
    sns.jointplot(x="total_bill", y="tip", data=tips, kind='kde')
    sns.jointplot(x="total_bill", y="tip", data=tips, kind='hex')
    plt.show()

运行结果：

 代码中我用 kind 分别显示了他们的散点图、核密度图和 Hexbin 图，如下图所示。
  
  散点图：  
  
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/%E4%BA%8C%E5%85%83S%E6%95%A3%E7%82%B9%E5%9B%BE.png)
  核图：  
  
  ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/%E4%BA%8C%E5%85%83S%E6%A0%B8%E5%9B%BE.png)
 
 Hexbin图：    
 
 ![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/%E4%BA%8C%E5%85%83hexbin%E5%9B%BE.png)
  
  
  
 ## 可视化导图总结：
    
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/seaborn_and_Matplotlib/python%E5%8F%AF%E8%A7%86%E5%8C%96.png)
  
 
 
 
 
 
 
 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
  
  
  
  
  
    






















