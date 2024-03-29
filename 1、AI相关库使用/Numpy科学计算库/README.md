# 📖 numpy库使用方法梳理

## 为什么要使用numpy库呢
  在Python数据结构中的列表list，它其实上相当于一个数组结构。而numpy中的一个关键数据类型就是关于数组的，那为什么还存在这样的一个第三方数据结构呢？
  
  实际上，标准的Python中，用列表保存数组的值。由于列表中的元素是任意的对象，所以列表中list保存的是对象的指针。虽然在Python编程中隐去了指针的概念，
  但是数组有指针，Python的列表list其实就是数组。这样如果我们要保存一个简单的数组 [0,1,2],就需要有3个指针和3个整数对象，这样对于Python来说是非常不经济
  的，浪费了内存和计算时间。
  
## 使用 NumPy 让你的 Python 科学计算更高效

  为什么要用 NumPy 数组结构而不是 Python 本身的列表 list？这是因为列表 list 的元素在系统内存中是分散存储的，而 NumPy 数组存储在一个均匀连续的内存块中。
  这样数组计算遍历所有的元素，不像列表 list 还需要对内存地址进行查找，从而节省了计算资源。
  
  另外在内存访问模式中，缓存会直接把字节块从 RAM 加载到 CPU 寄存器中。因为数据连续的存储在内存中，NumPy 直接利用现代 CPU 的矢量化指令计算，加载寄存器中的多个连续浮点数。
  另外 NumPy 中的矩阵计算可以采用多线程的方式，充分利用多核 CPU 计算资源，大大提升了计算效率。


  当然除了使用 NumPy 外，你还需要一些技巧来提升内存和提高计算资源的利用率。一个重要的规则就是：避免采用隐式拷贝，而是采用就地操作的方式 。
  举个例子，如果我想让一个数值 x 是原来的两倍，可以直接写成 x*=2，而不要写成 y=x*2。
 
  这样速度能快到 2 倍甚至更多。
  
  既然 NumPy 这么厉害，你该从哪儿入手学习呢？在 NumPy 里有两个重要的对象：ndarray（N-dimensional array object）解决了多维数组问题，而 ufunc（universal function object）则是解决对数组进行处理的函数。

  下面，我就带你一一来看。

## np.random.permutation 随机打乱

对于训练数据时如果想要训练集随机打乱，可以使用 np.random.permutation 对索引进行打乱，然后重组训练数据集。

#### 1、对0-5之间的序列进行随机排序

    import numpy as np

    random_index = np.random.permutation(5)

    print(random_index)         # [3,1,2,5,4]

#### 2、对一个list进行随机排序

    import numpy as np

    random_list = np.random.permutation([1,2,3,4,5,6,7,8,9])

    print(random_index)         # [3,1,2,5,4,6,7,9,8]


## 设置小数位数

*   `设置有效的小数位数`

        np.around([0.37, 1.64])
        array([ 0.,  2.])

        np.around([0.37, 1.64], decimals=1)
        array([ 0.4,  1.6])
        
*   `设置输出的精度`
          
          np.set_printoptions(precision=3)
          print(x)
          # [ 0.078  0.48   0.413  0.83 ]
          
## ndarray 对象
  ndarray 实际上是多维数组的含义。在 NumPy 数组中，维数称为秩（rank），一维数组的秩为 1，二维数组的秩为 2，以此类推。
  在 NumPy 中，每一个线性的数组称为一个轴（axes），其实秩就是描述轴的数量。  
  
  `创建数组`
  
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b[1,1]=10
    print a.shape
    print b.shape
    print a.dtype
    print b
    
 `运行结果：`
 
    (3L,)
    (3L, 3L)
    int32
    [[ 1  2  3]
     [ 4 10  6]
     [ 7  8  9]]

  创建数组前，你需要引用 NumPy 库，可以直接通过 array 函数创建数组，如果是多重数组，比如示例里的 b，那么该怎么做呢？
  你可以先把一个数组作为一个元素，然后嵌套起来，比如示例 b 中的 [1,2,3] 就是一个元素，然后 [4,5,6][7,8,9] 也是作为元素，然后把三个元素再放到 [] 数组里，赋值给变量 b。

  当然数组也是有属性的，比如你可以通过函数 shape 属性获得数组的大小，通过 dtype 获得元素的属性。如果你想对数组里的数值进行修改的话，直接赋值即可，注意下标是从 0 开始计的，所以如果你想对 b 数组，九宫格里的中间元素进行修改的话，下标应该是 [1,1],1]。
  
## np.c_和np.r_

np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等。

np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等。


[np.c_和np.r_ 案例展示](https://blog.csdn.net/weixin_41797117/article/details/80048688)

## 结构数组

  如果你想统计一个班级里面学生的姓名、年龄，以及语文、英语、数学成绩该怎么办？
  当然你可以用数组的下标来代表不同的字段，比如下标为 0 的是姓名、小标为 1 的是年龄等，但是这样不显性。
  
  实际上在 C 语言里，可以定义结构数组，也就是通过 struct 定义结构类型，结构中的字段占据连续的内存空间，每个结构体占用的内存大小都相同，那在 NumPy 中是怎样操作的呢？
    
  `定义结构数组:`
    
    import numpy as np
    persontype = np.dtype({
        'names':['name', 'age', 'chinese', 'math', 'english'],
        'formats':['S32','i', 'i', 'i', 'f']})
    peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
           ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
        dtype=persontype)
    ages = peoples[:]['age']
    chineses = peoples[:]['chinese']
    maths = peoples[:]['math']
    englishs = peoples[:]['english']
    print np.mean(ages)
    print np.mean(chineses)
    print np.mean(maths)
    print np.mean(englishs)

  `运行结果：`
    
    28.25
    77.5
    93.25
    93.75

  你看下这个例子，首先在 NumPy 中是用 dtype 定义的结构类型，然后在定义数组的时候，用 array 中指定了结构数组的类型 dtype=persontype，这样你就可以自由地使用自定义的 persontype 了。
  比如想知道每个人的语文成绩，就可以用 chineses = peoples[:][‘chinese’]，当然 NumPy 中还有一些自带的数学运算，比如计算平均值使用 np.mean。

##  ufunc 运算
  ufunc 是 universal function 的缩写，是不是听起来就感觉功能非常强大？确如其名，它能对数组中每个元素进行函数操作。NumPy 中很多 ufunc 函数计算速度非常快，因为都是采用 C 语言实现的。
  
##  `连续数组的创建`
  NumPy 可以很方便地创建连续数组，比如我使用 arange 或 linspace 函数进行创建：
  
 `example:`
 
    import numpy 
    x1 = np.arange(1,11,2)
    display(x1)

    # numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
      
      endpoint是一个bool类型的值，如果为"Ture",“stop"是最后一个值，如果为"False”,生成的数组不会包含"stop"值
      retstep是一个bool类型的值，如果为"Ture"，会返回样本之间的间隙。
    
    x2 = np.linspace(1,9,5)
    display(x2)
    
 `out:`
    
    array([1, 3, 5, 7, 9])
    array([1., 3., 5., 7., 9.])

*   `np.arange() 和 np.linspace() 的异同：`

    np.arange 和 np.linspace 起到的作用是一样的，都是创建等差数组。这两个数组的结果 x1,x2 都是 [1 3 5 7 9]。结果相同，但是你能看出来创建的方式是不同的。   

*   `np.arange()：`
    
    arange() 类似内置函数 range()，通过指定 `初始值、终值、步长` 来创建等差数列的一维数组，默认是不包括终值的。

*   `np.linspace()：`

    linspace 是 linear space 的缩写，代表线性等分向量的含义。linspace() 通过指定 `初始值、终值、元素个数` 来创建等差数列的一维数组，默认是包括终值的。

## 算数运算
  通过 NumPy 可以自由地创建等差数组，同时也可以进行加、减、乘、除、求 n 次方和取余数。
  
  `例子：`
  
    x1 = np.arange(1,11,2)
    x2 = np.linspace(1,9,5)
    print np.add(x1, x2)
    print np.subtract(x1, x2)
    print np.multiply(x1, x2)
    print np.divide(x1, x2)
    print np.power(x1, x2)
    print np.remainder(x1, x2)

  `运行结果：`
  
    [ 2.  6. 10. 14. 18.]
    [0. 0. 0. 0. 0.]
    [ 1.  9. 25. 49. 81.]
    [1. 1. 1. 1. 1.]
    [1.00000000e+00 2.70000000e+01 3.12500000e+03 8.23543000e+05
     3.87420489e+08]
    [0. 0. 0. 0. 0.]

   我还以 x1, x2 数组为例，求这两个数组之间的加、减、乘、除、求 n 次方和取余数。在 n 次方中，x2 数组中的元素实际上是次方的次数，x1 数组的元素为基数。
  在取余函数里，你既可以用 np.remainder(x1, x2)，也可以用 np.mod(x1, x2)，结果是一样的。
  
#### 算数运算中的 axis 的作用

axis = 0 时，代表对横轴操作，也就是第0轴，在运算的过程中其运算的方向表现为纵向运算。

axis = 1 时，代表对纵轴操作，也就是第1轴，在运算的过程中其运算的方向表现为横向运算。


`例子：` 

现在有一个混淆矩阵，我们想要其按列进行相加，保持原来的行数

  conf_mx 

  array([[5688,    1,   16,   20,   20,   36,   33,    5,   99,    5],
        [   2, 6470,   39,   21,   22,   40,   12,    9,  117,   10],
        [  77,   80, 5029,  122,  106,   58,  115,  110,  243,   18],
        [  45,   32,  227, 4903,   26,  364,   26,  103,  319,   86],
        [  19,   35,   23,   10, 5406,   29,   49,   35,   59,  177],
        [  59,   26,   29,  279,  125, 4513,  119,   19,  200,   52],
        [  57,   20,   26,    3,   43,  113, 5562,    8,   85,    1],
        [  35,   24,   53,   22,  115,   31,    3, 5784,   30,  168],
        [  39,  168,  102,  146,   73,  466,   60,   38, 4675,   84],
        [  48,   48,   19,  130,  583,  171,    3,  455,  100, 4392]],
        dtype=int64)

  row_sums = conf_mx.sum(axis=1,keepdims=True) # keepdims=True 表示保持2维形状。
  row_sums.shape

  (10, 1)

可以看到行数保持不变，但是列数变成了1列。

## 统计函数
  
  如果你想要对一堆数据有更清晰的认识，就需要对这些数据进行描述性的统计分析，比如了解这些数据中的最大值、最小值、平均值，是否符合正态分布，方差、标准差多少等等。它们可以让你更清楚地对这组数据有认知。
  
  下面我来介绍下在 NumPy 中如何使用这些统计函数。
  
  `计数组 / 矩阵中的最大值函数 amax()，最小值函数 amin()`
  
    import numpy as np
    a = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print np.amin(a)
    print np.amin(a,0)
    print np.amin(a,1)
    print np.amax(a)
    print np.amax(a,0)
    print np.amax(a,1)

`运行结果：`

    1
    [1 2 3]
    [1 4 7]
    9
    [7 8 9]
    [3 6 9]

amin() 用于计算数组中的元素沿指定轴的最小值。对于一个二维数组 a，amin(a) 指的是数组中全部元素的最小值，amin(a,0) 是延着 axis=0 轴的最小值，axis=0 轴是把元素看成了 [1,4,7], [2,5,8], [3,6,9] 三个元素，所以最小值为 [1,2,3]，amin(a,1) 是延着 axis=1 轴的最小值，axis=1 轴是把元素看成了 [1,2,3], [4,5,6], [7,8,9] 三个元素，所以最小值为 [1,4,7]。同理 amax() 是计算数组中元素沿指定轴的最大值。
  
## 统计最大值与最小值之差 ptp()
  `例子：`
  
    a = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print np.ptp(a)
    print np.ptp(a,0)
    print np.ptp(a,1)

`运行结果：`

      8
    [6 6 6]
    [2 2 2]

  对于相同的数组 a，np.ptp(a) 可以统计数组中最大值与最小值的差，即 9-1=8。同样 ptp(a,0) 统计的是沿着 axis=0 轴的最大值与最小值之差，即 7-1=6（当然 8-2=6,9-3=6，第三行减去第一行的 ptp 差均为 6），ptp(a,1) 统计的是沿着 axis=1 轴的最大值与最小值之差，即 3-1=2（当然 6-4=2, 9-7=2，即第三列与第一列的 ptp 差均为 2）。
  
## `统计数组的百分位数 percentile()`
  
  `例子:`
    
    a = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print np.percentile(a, 50)
    print np.percentile(a, 50, axis=0)
    print np.percentile(a, 50, axis=1)
    
 `运行结果：`
 
      5.0
    [4. 5. 6.]
    [2. 5. 8.]

 同样，percentile() 代表着第 p 个百分位数，这里 p 的取值范围是 0-100，如果 p=0，那么就是求最小值，如果 p=50 就是求平均值，如果 p=100 就是求最大值。同样你也可以求得在 axis=0 和 axis=1 两个轴上的 p% 的百分位数。
 
 ## 统计数组中的中位数 median()、平均数 mean()
  
  `例子：`
  
    a = np.array([[1,2,3], [4,5,6], [7,8,9]])
    # 求中位数
    print np.median(a)
    print np.median(a, axis=0)
    print np.median(a, axis=1)
    # 求平均数
    print np.mean(a)
    print np.mean(a, axis=0)
    print np.mean(a, axis=1)


  `运行结果：`
    
    5.0
    [4. 5. 6.]
    [2. 5. 8.]
    5.0
    [4. 5. 6.]
    [2. 5. 8.]


你可以用 median() 和 mean() 求数组的中位数、平均值，同样也可以求得在 axis=0 和 1 两个轴上的中位数、平均值。你可以自己练习下看看运行结果。

## 统计数组中的加权平均值 average()

  `例子：`
    
    a = np.array([1,2,3,4])
    wts = np.array([1,2,3,4])
    print np.average(a)
    print np.average(a,weights=wts)

`运行结果：`

    2.5
    3.0

average() 函数可以求加权平均，加权平均的意思就是每个元素可以设置个权重，默认情况下每个元素的权重是相同的，所以 np.average(a)=(1+2+3+4)/4=2.5，你也可以指定权重数组 wts=[1,2,3,4]，这样加权平均 np.average(a,weights=wts)=(1*1+2*2+3*3+4*4)/(1+2+3+4)=3.0。

## 统计数组中的标准差 std()、方差 var()
  
  `例子：`
    
    a = np.array([1,2,3,4])
    print np.std(a)
    print np.var(a)
  
    avg = (1+2+3+4)/4 = 2.5
    std = np.sqrt((1-1.5)^2+(2-1.5)^2+(3-1.5)^2+(4-1.5)^2)/4) 

  `运行结果：`
  
    1.118033988749895
    1.25
    
`方差` 的计算是指每个数值与平均值之差的平方求和的平均值，即 mean(Σ(x - x.mean())** 2)。

`标准差` 是方差的算术平方根。在数学意义上，代表的是一组数据离平均值的分散程度。所以 np.var(a)=1.25, np.std(a)=1.118033988749895。
    
  `例子2：`

    a = np.array([[1, 2], [3, 4]])
    a.std()

  不论是上面的 一维 还是 这里的二维，如果在std()函数中指定axis那么会将所有内容当作一维进行计算。即：

    avg = (1+2+3+4)/4 = 2.5
    std = np.sqrt((1-1.5)^2+(2-1.5)^2+(3-1.5)^2+(4-1.5)^2)/4) 

  `运行结果：`
  
    1.118033988749895

    
  `例子3：`

    a = np.array([[1, 2], [3, 4]])

    a.std(0)  # 计算每一列的标准差
    a.std(1)  # 计算每一行的标准差

  `运行结果：`
  
    [1. 1.]
    [0.5 0.5]

## 对数据进行 `对数化` 和 `还原` 操作

## numpy log1p 和 expm1

`np.log1p` 和 `np.expm1` 对数据进行转换

`log1p` 就是求 `log(1+x)`

*   在数据预处理时首先可以对偏度比较大的数据用log1p函数进行转化，使其更加服从高斯分布，此步处理可能会使我们后续的分类结果得到一个更好的结果；

*   log1p的使用就像是将一个数据压缩到了一个区间，与数据的标准化类似。下面再说说它的逆运算expm1函数。

*   由于前面使用过log1p将数据进行了压缩，所以最后需要记得将预测出的平滑数据进行一个还原，而还原过程就是log1p的逆运算expm1。

`np.log1p`：对 a 进行对数化

    a = 23
    a_log1p = np.log1p(a)
    a_log1p

output:

    3.1780538303479458

`np.expm1`：将对数化后的数据进行还原

    np.expm1(a_log1p)

output:

    23.000000000000004

* `log1p和expm1：`https://www.cnblogs.com/wqbin/p/10346292.html


## numpy log 和 exp

`np.log` 和 `np.exp` 对数据进行转换

`np.log`：对 a 进行对数化

    a = 23
    log_a = np.log(a+1)
    log_a

output:

    3.1780538303479458

`np.exp`：将对数化后的数据进行还原

    np.exp(log_a)-1

output:

    23.000000000000004


## NumPy 排序

  排序是算法中使用频率最高的一种，也是在数据分析工作中常用的方法，计算机专业的同学会在大学期间的算法课中学习。那么这些排序算法在 NumPy 中实现起来其实 非常简单，一条语句就可以搞定。这里你可以使用 sort 函数，sort(a, axis=-1, kind=‘quicksort’, order=None)，默认情况下使用的是快速排序；在 kind 里，可以指定 quicksort、mergesort、heapsort 分别表示快速排序、合并排序、堆排序。同样 axis 默认是 -1，即沿着数组的最后一个轴进行排序，也可以取不同的 axis 轴，或者 axis=None 代表采用扁平化的方式作为一个向量进行排序。另外 order 字段，对于结构化的数组可以指定按照某个字段进行排序。

`例子：`

    a = np.array([[4,3,2],[2,4,1]])
    print np.sort(a)
    print np.sort(a, axis=None)
    print np.sort(a, axis=0)  
    print np.sort(a, axis=1)  
    
`运行结果：`

    [[2 3 4]
     [1 2 4]]
    [1 2 2 3 4 4]
    [[2 3 1]
     [4 4 2]]
    [[2 3 4]
     [1 2 4]]


### np.argsort 数组值从小到大排序，返回值为索引值


`例子：`

    >> a = np.array([2,7,5,1,8,6])
    >> a

    out：array([2, 7, 5, 1, 8, 6])


    >> index = np.argsort(a)
    >> index

    out：array([3, 0, 2, 5, 1, 4], dtype=int64)

    >> a[index]

    out：array([1, 2, 5, 6, 7, 8])

## numpy reshape

*   `案例`

    构造数据：

        y = np.arange(35)

    out：

        array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
            34])

    `将 一维数组 转为 二维数组：`

        # 一共35个数据，分成5行7列，二维数组
        y = np.arange(35).reshape(5,7)

    `out：`

        array([[ 0,  1,  2,  3,  4,  5,  6],
              [ 7,  8,  9, 10, 11, 12, 13],
              [14, 15, 16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25, 26, 27],
              [28, 29, 30, 31, 32, 33, 34]])

    `将 一维数组 转为 三维数组：`

        # 一共45个数据，分成3，3，5，三维数组
        y = np.arange(45).reshape(3,3,5)

    `out：`

        array([[[ 0,  1,  2,  3,  4],
                [ 5,  6,  7,  8,  9],
                [10, 11, 12, 13, 14]],

              [[15, 16, 17, 18, 19],
                [20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29]],

              [[30, 31, 32, 33, 34],
                [35, 36, 37, 38, 39],
                [40, 41, 42, 43, 44]]])

## `ndarray.resize()`

* resize 可以用于重塑数据的形状，不足的元素用0填充，不过需要要求数据在内存中连续。


      #a = np.arange(10)
      
      a = dd.iloc[0].values       ## ndarray
      ## 让a在内存中连续，不使用下面方法，有的时候会报错
      a = np.ascontiguousarray(a)
      a.resize(9,9)
      display(a)

      plt.imshow(a,cmap="gray")



<div align=center><img width="350" height="300" src="./static/resize.jpg"/></div>





## `numpy 索引切片`

*   `案例`

    生成数据：

        y = np.arange(35).reshape(5,7)
        y

    out:

        array([[ 0,  1,  2,  3,  4,  5,  6],
               [ 7,  8,  9, 10, 11, 12, 13],
               [14, 15, 16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25, 26, 27],
               [28, 29, 30, 31, 32, 33, 34]])

    `行切割，并指定步长：`

      切割 np 数据 y，取前面五行，并且输出时，每隔2行进行输出

          # 取 1 - 5 列，步长为2
          y[1:5:2]

    out:

          array([[ 7,  8,  9, 10, 11, 12, 13],
                [21, 22, 23, 24, 25, 26, 27]])

    `行列切割，并指定行步长：`


          # 取 1 - 5 列，步长为2，同时取前面三列
          y[1:5:2,:3]

    out:

          array([[ 7,  8,  9],
                [21, 22, 23]])


    `行列切割，并指定行列步长：`


          # 取 1 - 5 列，步长为2，同时每隔3步取一个元素
          y[1:5:2,::3]
          
    out:

          array([[ 7, 10, 13],
                [21, 24, 27]])


## numpy stack方法、hstack方法、vstack方法

一般用于三维以下的数组

*   `stack 案例1 二维数据：`

        import numpy as np
        a=[
            [1,2,3],
          [4,5,6]
          ]
        print("列表a如下：")
        print(a)
        print('\n')

        print("增加一维，axis=0")
        c=np.stack(a,axis=0)
        print(c)
        print('\n')

        print("增加一维，axis=1")
        c=np.stack(a,axis=1)
        print(c)
        print('\n')

        print("a 的转置")
        c=np.asarray(a).T
        print(c)

    `out:`

        列表a如下：
        [[1, 2, 3], [4, 5, 6]]


        增加一维，axis=0
        [[1 2 3]
        [4 5 6]]


        增加一维，axis=1
        [[1 4]
        [2 5]
        [3 6]]

        a 的转置
        [[1 4]
        [2 5]
        [3 6]]

    `解析：`

    *   我们其实可以看到，`在二维数组中，他的stack(axis=0)相当于他的自身，他的stack(axis=0)相当于他的转置(仅限二维)`。

    *   axis=0是本身，我们先不做分析，当axis=1时，我们只观察他对应的 `列数据` 就好了，因为这里我们是二维，所以我们的列表中：
        
        第一行第一列 1，对应第二行第一列4。

        第一行第二列 2，对应第二行第二列5。

        第一行第三列 3，对应第二行第三列6。

        所以我们将一个对应组合成一行，如 [1,4],[2.5],[3,6] ,然后因为是二维，所以在外面加上大括号 即 [[1,4],[2.5],[3,6]]。


*   `stack 案例2 三维数据：`

        import numpy as np
        a=[
            [
                [1,2,3],
          [4,5,6]],
            
            [
                [7,8,9],
          [10,11,12]],
            
            
          ]
        print("列表a如下：")
        print(a)
        print('\n')

        print("增加一维，axis=0")
        c=np.stack(a,axis=0)
        print(c)
        print('\n')

        print("增加一维，axis=1")
        c=np.stack(a,axis=1)
        print(c)
        print('\n')

    `out:`

        列表a如下：
        [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]


        增加一维，axis=0
        [[[ 1  2  3]
          [ 4  5  6]]

        [[ 7  8  9]
          [10 11 12]]]


        增加一维，axis=1
        [[[ 1  2  3]
          [ 7  8  9]]

        [[ 4  5  6]
          [10 11 12]]]


        a 的转置
        [[[ 1  7]
          [ 4 10]]

        [[ 2  8]
          [ 5 11]]

        [[ 3  9]
          [ 6 12]]]

    `解析：`

    *   和二维一样，三维数组中stack(axis=0)是本身。

    *   axis=0是本身，我们先不做分析，当axis=1时，我们只观察他对应的 `列数据` 就好了，因为这里我们是三维，所以我们的列表中：
        
        [1,2,3] 对应 [7,8,9]。

        [4,5,6] 对应 [10,11,12]。

        所以我们将一个对应组合成一行，如 [[1,2,3],[7,8,9]],[[4,5,6],[10,11,12]] ,然后因为是三维，所以在外面加上大括号 即 [[[1,2,3],[7,8,9]],[[4,5,6],[10,11,12]]]。



*   `hstack 案例1 一维数组组合：`


        a=[1,2,3]
        b=[4,5,6]
        print(np.hstack((a,b)))

    `out：`

        [1 2 3 4 5 6]

    *   沿着水平方向将数组堆叠起来。在一维数组中也就是 将一维数据按照 `水平方向` 进行组合

        一维的 hstack 组合 和一维的 vstack组合都是增加 shape 出来的行数 
        
        a shape (3,) 
        b shape (3,)

        组合 新的 shape (6,)

*   `hstack 案例2 二维数组组合：`

        arr1 = np.array([[1, 2], [3, 4], [5, 6]])
        arr2 = np.array([[7, 8], [9, 0], [0, 1]])
        res = np.hstack((arr1, arr2))

        res

    `out：`

        array([[1, 2, 7, 8],
               [3, 4, 9, 0],
               [5, 6, 0, 1]])

    *   根据列方向 (`列变，行不变`) 将数据沿着水平方向将数组堆叠起来。

            arr1:         arr2:

              [                  [
                [1,2]              [7,8]
                [3,4]              [9,10]
                [5,6]              [11,12]
              ]                  ]

    *   根据他们的形状画出他们的分布，然后一一对应按照水平方向将数组堆叠即可：
        
        如 [1,2] 和 [7,8] 按照水平堆叠 [[1,2,7,8]]

        shape  从 (3,2) -> (3,4)


*   `vstack 案例1 一维数组组合：`

        a=[1,2,3]
        b=[4,5,6]
        print(np.vstack((a,b)))

    `out：`

        [[1 2 3]
        [4 5 6]]

    *   沿着垂直方向将数组堆叠起来。在一维数组中也就是 将一维数据按照 `垂直方向` 进行组合

        vstack 和 hstack 相反，将原来的 a 的 shape 看成是 (,3) 的二维数组，然后在这个基础上进 行方向 的扩展

        a shape (1,3) 
        b shape (1,3)

        组合 新的 shape (2,3)

*   `vstack 案例2 二维数组组合：`

        arr1 = np.array([[1, 2], [3, 4], [5, 6]])
        arr2 = np.array([[7, 8], [9, 0], [0, 1]])
        res = np.vstack((arr1, arr2))

        res

    `out：`

        array([[1, 2],
               [3, 4],
               [5, 6],
               [7, 8],
               [9, 0],
               [0, 1]])

    *   根据行方向 (`行变，列不变`) 将数据沿着垂直方向将数组堆叠起来。

            arr1:         
              [                  
                [1,2]             
                [3,4]              
                [5,6]           
              ]                  

            arr2:         
              [                  
                [7,8]             
                [9,10]              
                [11,12]           
              ]                  


    *   根据他们的形状画出他们的分布，然后一一对应按照垂直方向将数组堆叠即可 
        
        如 [1,2] 和 [3,4] 按照垂直堆叠 [1,2],[3,4]

        shape  从 (3,2) -> (6,2)

## numpy.transpose()

numpy.transpose()是对矩阵按照所需的要求的转置

*   `二维数组进行 numpy.transpose() 相当于进行转置` 。(0,1) 变为 (1,0) 行数据和列数据进行了转换

    对于二维 ndarray，transpose在不指定参数是默认是矩阵转置，即相当于 nd.transpose(1，0)

*   `案例 三维数组：`

        import numpy as np
    
        a = np.array(range(30)).reshape(3, 2, 5)
        
        print ("a = ")
        print (a)
        
        print( "\n=====================\n")
        
        print ("a.transpose() = ")
        print (a.transpose(1, 0, 2))

    `out：`

        a = 
          [[[ 0  1  2  3  4]
            [ 5  6  7  8  9]]

          [[10 11 12 13 14]
          [15 16 17 18 19]]

          [[20 21 22 23 24]
            [25 26 27 28 29]]]

        =====================

        a.transpose() = 
          [[[ 0  1  2  3  4]
            [10 11 12 13 14]
            [20 21 22 23 24]]

          [[ 5  6  7  8  9]
            [15 16 17 18 19]
            [25 26 27 28 29]]]

 


*   `解释：`

    我们先构造一个 (3,2,5) 的三维数组，那么这个元组对应的索引为：(0,1,2), 所以如果我们使用 a.transpose(0, 1, 2) 就是他本身
    
    这里我们指定 a.transpose(1, 0, 2)  相当于 他的 0 轴和 1 轴进行了变化 那么：

    1、原先 shape 为 (3,2,5) 会变成 (2,3,5)

    2、对应的数据结构会发生变化：
        
        比如原先 10 的位置在 [1,0,0] 变换后变为 [0,1,0]

        原先 22 的位置为 [2,0,2] 变换后变为 [0,2,2]

  <div align=center><img  src="./static/transpose.jpg"/></div>


## `np.clip：`

给定一个区间，区间外的值被裁剪到区间边缘。例如，如果 指定了区间，则小于 0 的值变为 0，大于 1 的值变为 1。


    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    >>> np.clip(a, 1, 8)
    array([1, 1, 2, 3, 4, 5, 6, 7, 8, 8])



## `numpy的数字符号`
    
    np.pi 表示 π
     
## `numpy易错点：`
  
  numpy之axis：
    
    axis=0 和 axis=1 的顺序。axis=0 代表跨行（实际上就是按列），axis=1 代表跨列（实际上就是按行）。
    如果排序的时候，没有指定 axis，默认 axis=-1，代表就是按照数组最后一个轴来排序(二维数组最后一个轴就是轴1所以轴1和轴-1一致)。如果 axis=None，代表以扁平化的方式作为一个向量进行排序。
   
  例子：
  
    a = np.array([[4,3,2],[2,4,1]])
    print(np.sort(a))
    print(np.sort(a, axis=None))
    print(np.sort(a, axis=0))
    print(np.sort(a, axis=1))


  运行结果：
  
    [[2 3 4]
     [1 2 4]]
    [1 2 2 3 4 4]
    [[2 3 1]
     [4 4 2]]
    [[2 3 4]
     [1 2 4]]

axis=0 的排序结果，axis=0 代表的是跨行（跨行就是按照列），所以实际上是对 [4, 2] [3, 4] [2, 1] 来进行排序，排序结果是 [2, 4] [3, 4] [1, 2]，对应的是每一列的排序结果。还原到矩阵中也就是 [[2 3 1], [4, 4, 2]]。
    
  这里做个笔记：
    当asix=-1时是按照数组最后一个轴来排序其实就是按数组最内部的数据进行排序
    
  例子：三维数组 
  
  第一个轴0：   这三个比较大小
  
               [[ 0 -2 -3]
                [ 3  1  5]
                [ 0  1  9]]

               [[ 0  2 -3]
                [ 3 -1  5]
                [ 0 -1  9]]

  第一个轴是最外层的轴，索引为0，只用关注轴0即可。     及轴0变，轴1和轴2不变。 图中看轴0发生变化的是  
  
      这个一个整块       [[ 0 -2 -3]       和这个一个整块   [[ 0  2 -3]
                         [ 3  1  5]                        [ 3 -1  5]
                         [ 0  1  9]]                       [ 0 -1  9]]
  
  轴1和轴2是第二层和第三层，如果要保证不变的话就要 0和0对比因为第一个0和第二个0的索引是(0,0,0)和(1,0,0)分别只有1发生变化。所以按照0轴就是一个和一个分别对应。
  
  如果按轴1排序，那要保证轴0和轴2相等，那就是 [0 3 0] [-2,1,1] [-3,5,9] 之间排序,也就是第一个3x3的数组中的竖下来排序。
  
  轴2的话就是[ 0 -2 -3] [ 3  1  5] [ 0  1  9]横着排序，因为保证轴0和轴1相同。
  
 ## 使用numpy显示全部的矩阵(不用省略号省略)
    
    np.set_printoptions(threshold=np.inf)

## 矩阵相乘：np.dot 和 np.multiplay
  `np.dot会将矩阵相乘之后的结果相加，但是multiplay不会`
  
  `例子:`
    
      w2=[
    [0,1/2,1,0],
    [1/3,0,0,1/2],
    [1/3,0,0,1/2],
    [1/3,1/2,0,0],
        ]

`w2.shape 为 (4,4)`
    
    v=[
        [1/4],[1/4],[1/4],[1/4]
    ]
    
`v.shape 为 (4,1)`
    
`np.dot(w2, v) 输出结果：`

    [[0.375     ]
     [0.20833333]
     [0.20833333]
     [0.20833333]]
`np.multiply(w2, v) 输出结果 ：`

    [[0.         0.125      0.25       0.        ]
     [0.08333333 0.         0.         0.125     ]
     [0.08333333 0.         0.         0.125     ]
     [0.08333333 0.125      0.         0.        ]]
     

## np.newaxis:

`np.newaxis 的功能是插入新维度，看下面的例子`

`例子:`

    a=np.array([1,2,3,4,5])
    a[:,np.newaxis]

`out:`

    array([[1],
       [2],
       [3],
       [4],
       [5]])

`例子:`

    a=np.array([1,2,3,4,5])
    a[np.newaxis,:]

`out:`

    array([[1, 2, 3, 4, 5]])


## numpy.argsort 

`返回对数组进行排序的索引。`

`数据:`

    a=np.array([6,3,5,7,10])
    a=a[:,np.newaxis]
    a
    
    array([[ 6],
       [ 3],
       [ 5],
       [ 7],
       [10]])

`例子1:`

    a.argsort(axis=1)[:5] 默认按行排序

`out:` 这个索引是排序后的索引

    array([[0],
       [0],
       [0],
       [0],
       [0]], dtype=int64)

`例子2:`

    a.argsort(axis=0)[:5] 按列排序

`out:` 这个索引是排序后的索引

    array([[1],
          [2],
          [0],
          [3],
          [4]], dtype=int64)

`例子3:` 通过索引获取值

    a[a[:,0].argsort()[:5]]

`out:`

    array([[ 3],
       [ 5],
       [ 6],
       [ 7],
       [10]])

## 使用numpy计算矩阵关系系数：

通过np.corrcoef计算矩阵关系系数

`例子:`

    top_ten=10
    # 取 SalePrice 列中值最大的前 top_ten 个 (有正负之分，负相关强的不予显示)
    columns=corrmat.nlargest(top_ten,'SalePrice')['SalePrice'].index
    # 计算协方差矩阵，可以用于绘制热力图
    cm=np.corrcoef(train_data[columns].values.T)
    cm
    
`运行结果:`

    array([[1.        , 0.7909816 , 0.70862448, 0.6404092 , 0.62343144,
          0.61358055, 0.60585218, 0.56066376, 0.53372316, 0.52289733],
         [0.7909816 , 1.        , 0.59300743, 0.60067072, 0.56202176,
          0.5378085 , 0.47622383, 0.55059971, 0.42745234, 0.57232277],
         [0.70862448, 0.59300743, 1.        , 0.46724742, 0.46899748,
          0.4548682 , 0.56602397, 0.63001165, 0.82548937, 0.19900971],
         [0.6404092 , 0.60067072, 0.46724742, 1.        , 0.88247541,
          0.43458483, 0.43931681, 0.46967204, 0.36228857, 0.53785009],
         [0.62343144, 0.56202176, 0.46899748, 0.88247541, 1.        ,
          0.48666546, 0.48978165, 0.40565621, 0.33782212, 0.47895382],
         [0.61358055, 0.5378085 , 0.4548682 , 0.43458483, 0.48666546,
          1.        , 0.81952998, 0.32372241, 0.28557256, 0.391452  ],
         [0.60585218, 0.47622383, 0.56602397, 0.43931681, 0.48978165,
          0.81952998, 1.        , 0.38063749, 0.40951598, 0.28198586],
         [0.56066376, 0.55059971, 0.63001165, 0.46967204, 0.40565621,
          0.32372241, 0.38063749, 1.        , 0.55478425, 0.46827079],
         [0.53372316, 0.42745234, 0.82548937, 0.36228857, 0.33782212,
          0.28557256, 0.40951598, 0.55478425, 1.        , 0.09558913],
         [0.52289733, 0.57232277, 0.19900971, 0.53785009, 0.47895382,
          0.391452  , 0.28198586, 0.46827079, 0.09558913, 1.        ]])



##  `NumPy自然指数计算函数`

NumPy中以自然数为底的指数计算方法为exp 也就是e的多少次方，expm1用来计算exp(x) - 1

    >>> import numpy as np
    >>> import math
    
    >>> np.exp(2)
    7.38905609893065

    >>> math.exp(2)
    7.38905609893065

    >>> np.expm1(2)
    6.38905609893065

    >>> A=np.array([1,2,3])
    >>> np.exp(A)
    array([ 2.71828183,  7.3890561 , 20.08553692])



## `将 ndarray 转成 image`


* 单一 numpy 

      ## 将数据保存为 ndarray（向量）
      ## dd 为 dataframe ，a 为 ndarray 
      a = dd.iloc[326].values
      a = np.ascontiguousarray(a)
      a.resize(9,9)
      plt.imshow(a)


      ## 保存文件
      import imageio
      output_filename = './class1/1.png'
      imageio.imwrite(output_filename,a)


      ## 读取文件并展示
      path_to_image = "./class1/1.png"

      image = PIL.Image.open(path_to_image)
      display(np.array(image).shape)

      # jpg 有压缩损失，不太好用，像素值有偏离
      # imarray = np.asarray(image)   
      # plt.figure()
      # plt.imshow(imarray)
      # plt.show()

      # png
      imarray = np.asarray(image)   
      plt.figure()
      plt.imshow(imarray)
      # plt.imshow(imarray,cmap="gray")

      plt.show()

* 最后结果：

  <div align=center><img src="./static/save_image.jpg"/></div>


* 批量numpy：

      ## 1、定义 numpy 到 image 函数
      import imageio
      def ndarray_to_image(nd,i,output_dir):

          nd = np.ascontiguousarray(nd)
          nd.resize(9,9)
      #     print(nd)
          
          imageio.imwrite(output_dir+"{}.png".format(i),nd)
          




      ## 2、定义要进行标准化的特征，最后输出为 ss_cut_df
      ## 数据中有两个 Label，这里以先分析 Label.1 为例。
      retain_columns = df.drop(["Label",'Label.1','Flow ID','Timestamp'],axis=1).columns
      retain_columns
      
      ## app df
      cut_df = df.drop(['Label',"Label.1",'Flow ID','Timestamp'],axis=1)

      ss_y1 = df[['Label']]
      ss_y2 = df[['Label.1']]

      ss_cut_df = pd.concat([pd.DataFrame(ss.fit_transform(cut_df),columns=retain_columns),ss_y2],axis=1)





      ## 3、给每一个类别创建一个文件夹，将数据中的不同类别数据单独取出，每一个类别为一个元素，存放在total_list 中。
      import os
      total_list = []
      app_output_dir=['./class0/','./class1/','./class2/','./class3/','./class4/','./class5/','./class6/','./class7/']

      for dirname in app_output_dir:
          os.makedirs(dirname)

      for i in range(8):
          class_dir_name = 'app_class'+ str(i)
          class_dir_name = ss_cut_df[ss_cut_df['Label.1'] == i]
          total_list.append(class_dir_name)




      ## 4、开始进行保存
      for i,single_df in enumerate(total_list):
      rows = single_df.shape[0]
      output_dir = app_output_dir[i]
      for row in range(rows):
          ndarray_to_image(single_df.values[row],row,output_dir)


## `总结：`
  在 NumPy 学习中，你重点要掌握的就是对数组的使用，因为这是 NumPy 和标准 Python 最大的区别。在 NumPy 中重新对数组进行了定义，同时提供了算术和统计运算，你也可以使用 NumPy 自带的排序功能，一句话就搞定各种排序算法。

