# violinplot


### 案例解析：

<div align=center> <img src='https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/%E5%8F%AF%E8%A7%86%E5%8C%96%E5%9B%BE%E8%A7%A3/1.png'/></div>

在上图中，白点是中位数，黑色盒型的范围是下四分位点到上四分位点，细黑线表示须。外部形状即为核密度估计（在概率论中用来估计未知的密度函数，属于非参数检验方法之一）。


小提琴图，可以认为是 __密度图 + 箱式图 + 其他特性__ 的合体。

<div align=center> <img src='https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/%E5%8F%AF%E8%A7%86%E5%8C%96%E5%9B%BE%E8%A7%A3/2.jpg'/></div>


其实就是把上面那个密度图（进行一个切割然后放倒），下面其实就是一个箱式图，然后合在一起。这样就充分发挥了两种图的优势。


*   __数据化分析解读：__

    1.Drama等于0 的分布比較分散，Drama等于1 的分布很不均匀（中间大两头小）；

    2.Drama 等于 0 和 Drama 等于 1 的分布存在比较明显的离散值（上侧的须或下侧的须较长）。
