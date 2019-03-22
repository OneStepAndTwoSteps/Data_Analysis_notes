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

### ndarray 对象
  ndarray 实际上是多维数组的含义。在 NumPy 数组中，维数称为秩（rank），一维数组的秩为 1，二维数组的秩为 2，以此类推。
  在 NumPy 中，每一个线性的数组称为一个轴（axes），其实秩就是描述轴的数量。  
  
  __创建数组__
  
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b[1,1]=10
    print a.shape
    print b.shape
    print a.dtype
    print b
    
 __运行结果：__
 
    (3L,)
    (3L, 3L)
    int32
    [[ 1  2  3]
     [ 4 10  6]
     [ 7  8  9]]

  创建数组前，你需要引用 NumPy 库，可以直接通过 array 函数创建数组，如果是多重数组，比如示例里的 b，那么该怎么做呢？
  你可以先把一个数组作为一个元素，然后嵌套起来，比如示例 b 中的 [1,2,3] 就是一个元素，然后 [4,5,6][7,8,9] 也是作为元素，然后把三个元素再放到 [] 数组里，赋值给变量 b。

  当然数组也是有属性的，比如你可以通过函数 shape 属性获得数组的大小，通过 dtype 获得元素的属性。如果你想对数组里的数值进行修改的话，直接赋值即可，注意下标是从 0 开始计的，所以如果你想对 b 数组，九宫格里的中间元素进行修改的话，下标应该是 [1,1],1]。
  
### 结构数组

  如果你想统计一个班级里面学生的姓名、年龄，以及语文、英语、数学成绩该怎么办？
  当然你可以用数组的下标来代表不同的字段，比如下标为 0 的是姓名、小标为 1 的是年龄等，但是这样不显性。
  
  实际上在 C 语言里，可以定义结构数组，也就是通过 struct 定义结构类型，结构中的字段占据连续的内存空间，每个结构体占用的内存大小都相同，那在 NumPy 中是怎样操作的呢？
    
  __定义结构数组:__
    
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

  __运行结果：__
    
    28.25
    77.5
    93.25
    93.75

  你看下这个例子，首先在 NumPy 中是用 dtype 定义的结构类型，然后在定义数组的时候，用 array 中指定了结构数组的类型 dtype=persontype，这样你就可以自由地使用自定义的 persontype 了。
  比如想知道每个人的语文成绩，就可以用 chineses = peoples[:][‘chinese’]，当然 NumPy 中还有一些自带的数学运算，比如计算平均值使用 np.mean。

###  ufunc 运算
  ufunc 是 universal function 的缩写，是不是听起来就感觉功能非常强大？确如其名，它能对数组中每个元素进行函数操作。NumPy 中很多 ufunc 函数计算速度非常快，因为都是采用 C 语言实现的。
  
###  连续数组的创建
  NumPy 可以很方便地创建连续数组，比如我使用 arange 或 linspace 函数进行创建：
  
    x1 = np.arange(1,11,2)
    x2 = np.linspace(1,9,5)
    
  np.arange 和 np.linspace 起到的作用是一样的，都是创建等差数组。这两个数组的结果 x1,x2 都是 [1 3 5 7 9]。结果相同，但是你能看出来创建的方式是不同的。   
  >
  arange() 类似内置函数 range()，通过指定 __初始值、终值、步长__ 来创建等差数列的一维数组，默认是不包括终值的。
  >
  linspace 是 linear space 的缩写，代表线性等分向量的含义。linspace() 通过指定 __初始值、终值、元素个数__ 来创建等差数列的一维数组，默认是包括终值的。



