# violinplot


### 案例解析：

<div align=leftr> <img src='https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/%E5%8F%AF%E8%A7%86%E5%8C%96%E5%9B%BE%E8%A7%A3/1-1.png'/></div>



<div align=right> <img src='https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/%E5%8F%AF%E8%A7%86%E5%8C%96%E5%9B%BE%E8%A7%A3/3.png'/></div>


*   上图讲解：
    
    白点是中位数。
    
    黑色盒型的范围是下四分位点到上四分位点
    
    __细黑线表示须__
    
    最上面的细长部分我们不需要参考他，相当于箱型图的异常点。
    
    外部形状即为核密度估计，越宽表示出现的频率越多（在概率论中用来估计未知的密度函数，属于非参数检验方法之一）。

箱形图在数据显示方面受到限制，简单的设计往往隐藏了有关数据分布的重要细节。例如使用箱形图时，我们不能了解数据分布是 __双模还是多模__(正太分布时是单个峰值，两个峰值，还是多个) 。虽然小提琴图可以显示更多详情，但它们也可能包含较多干扰信息。



小提琴图，可以认为是 __密度图 + 箱式图 + 其他特性__ 的合体。

<div align=center> <img src='https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/%E5%8F%AF%E8%A7%86%E5%8C%96%E5%9B%BE%E8%A7%A3/2.jpg'/></div>


其实就是把上面那个密度图（进行一个切割然后放倒），下面其实就是一个箱式图，然后合在一起。这样就充分发挥了两种图的优势。


*   __数据化分析解读：__

    1.Drama等于0 的分布很不均匀（中间大两头小），Drama等于1 的分布比较分散；

    2.Drama 等于 0 和 Drama 等于 1 的分布存在比较明显的离散值（上侧的须或下侧的须较长）。
