
## KNN

### KNN的工作原理
“近朱者赤，近墨者黑”可以说是 KNN 的工作原理。整个计算过程分为三步：
  
    一、计算待分类物体与其他物体之间的距离；
    
    二、统计距离最近的 K 个邻居；
    
    三、对于 K 个最近的邻居，它们属于哪个分类最多，待分类物体就属于哪一类。

### K值的选择：
__关于KNN为什么K值变大会造成欠拟合，K值过小会造成过拟合：__
首先明确题目，K值是过大，或者过小的，第二KNN的思想是用目标点邻点的类别投票判断目标点的类别。 __如果K过大，即和它距离较远的不同类别的点就变成了邻点，偏差变大，准确率就低了。如果K过小，比如就选最近的一个点，容易被噪声和错误的样本干扰，就容易过拟合。__

如果 K 值比较小，就相当于未分类物体与它的邻居非常接近才行。这样产生的一个问题就是，如果邻居点是个噪声点，那么未分类物体的分类也会产生误差，这样 KNN 分类就会产生过拟合。
                   
如果 K 值比较大，相当于距离过远的点也会对未知物体的分类产生影响，虽然这种情况的好处是鲁棒性强，但是不足也很明显，会产生欠拟合情况，也就是没有把未分类物体真正分类出来。
                 
所以 K 值是个实践出来的结果，并不是我们事先而定的。在工程上， __我们一般采用交叉验证的方式选取 K 值。__
            
__交叉验证的思路就是，把样本集中的大部分样本作为训练集，剩余的小部分样本用于预测，来验证分类模型的准确性。__ 所以在 KNN 算法中，我们一般会把 K 值选取在较小的范围内，同时在验证集上准确率最高的那一个最终确定作为 K 值。


### 距离如何计算
在 KNN 算法中，还有一个重要的计算就是关于距离的度量。 __两个样本点之间的距离代表了这两个样本之间的相似度。距离越大，差异性越大；距离越小，相似度越大。__

__关于距离的计算方式有下面五种方式：__
  
    一、欧氏距离；
    二、曼哈顿距离；
    三、闵可夫斯基距离；
    四、切比雪夫距离；
    五、余弦距离。


__欧氏距离__:
            
是我们最常用的距离公式，也叫做欧几里得距离。在二维空间中，两点的欧式距离就是：

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/KNN/1.png)


__注意：__ 因为我们以后可能涉及到N维的空间，所以为了方便我们将这里的两个点定义为(x1,x2,x3……,xn)和(y1,y2,y3……,yn) 所以这样我们两个点之间的距离就是按照上面这个式子来计算了。

__同理，我们也可以求得两点在 n 维空间中的距离：__

![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/KNN/5.png)


__曼哈顿距离__ 
         
在几何空间中用的比较多。以下图为例，绿色的直线代表两点之间的欧式距离，而红色和黄色的线为两点的曼哈顿距离。所以曼哈顿距离等于两个点在坐标系上绝对轴距总和。用公式表示就是：
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/KNN/2.png)
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/KNN/3.png)

__闵可夫斯基距离__:
          
闵可夫斯基距离不是一个距离，而是一组距离的定义。对于 n 维空间中的两个点 x(x1,x2,…,xn) 和 y(y1,y2,…,yn) ， x 和 y 两点之间的闵可夫斯基距离为：   
![Image_text](https://raw.githubusercontent.com/OneStepAndTwoSteps/data_mining_analysis/master/static/KNN/4.png)

__其中 p 代表空间的维数，当 p=1 时，就是曼哈顿距离；当 p=2 时，就是欧氏距离；当 p→∞时，就是切比雪夫距离。__

__余弦距离__:
     
余弦距离实际上计算的是两个向量的夹角，是在方向上计算两者之间的差异，对绝对数值不敏感。在兴趣相关性比较上，角度关系比距离的绝对值更重要，因此余弦距离可以用于衡量用户对内容兴趣的区分度。比如我们用搜索引擎搜索某个关键词，它还会给你推荐其他的相关搜索，这些推荐的关键词就是采用余弦距离计算得出的。 

### KD 树

__KNN 的计算过程是大量计算样本点之间的距离。__ 为了减少计算距离次数，提升 KNN 的搜索效率，人们提出了 KD 树（K-Dimensional 的缩写）。KD 树是对数据点在 K 维空间中划分的一种数据结构。在 KD 树的构造中，每个节点都是 k 维数值点的二叉树。既然是二叉树，就可以采用二叉树的增删改查操作，这样就大大提升了搜索效率。


### KNN 可以用来做回归也可以用来做分类

一、使用sklearn做分类器：

    from sklearn.neighbors import KNeighborsClassifier

二、使用sklearn做回归：

    from sklearn.neighbors import KNeighborsRegressor

### KNN分类器：

KNeighborsClassifier方法中有几个重要的参数：
  
    KNeighborsClassifier(n_neighbors=5, weights=‘uniform’, algorithm=‘auto’, leaf_size=30)

1.n_neighbors：即 KNN 中的 K 值，代表的是邻居的数量。K 值如果比较小，会造成过拟合。如果 K 值比较大，无法将未知物体分类出来。一般我们使用默认值 5。
           
2.weights：是用来确定邻居的权重，有三种方式：
        
     一、weights=uniform，代表所有邻居的权重相同；

     二、weights=distance，代表权重是距离的倒数，即与距离成反比；

     三、自定义函数，你可以自定义不同距离所对应的权重。大部分情况下不需要自己定义函数。

3.algorithm：用来规定计算邻居的方法，它有四种方式：
  
    一、algorithm=auto，根据数据的情况自动选择适合的算法，默认情况选择 auto；
    
    二、algorithm=kd_tree，也叫作 KD 树，是多维空间的数据结构，方便对关键数据进行检索，不过 KD 树适用于维度少的情况，一般维数不超过 20，如果维数大于 20 之后，效率反而会下降；
    
    三、algorithm=ball_tree，也叫作球树，它和 KD 树一样都是多维空间的数据结果，不同于 KD 树，球树更适用于维度大的情况；
    
    四、algorithm=brute，也叫作暴力搜索，它和 KD 树不同的地方是在于采用的是线性扫描，而不是通过构造树结构进行快速检索。当训练集大的时候，效率很低。

4.leaf_size：代表构造 KD 树或球树时的叶子数，默认是 30，调整 leaf_size 会影响到树的构造和搜索速度。







