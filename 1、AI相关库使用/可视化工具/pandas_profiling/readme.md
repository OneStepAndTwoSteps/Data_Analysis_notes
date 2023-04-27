# pandas_profiling

`pandas` 的 `df.describe()` 函数虽然功能强大，但对于进行认真的探索性数据分析却有些基础。 `pandas_profiling` 扩展了 `pandas DataFrame` 的功能。

可使用 `df.profile_report()` 进行快速数据分析。


## 使用方法

    import pandas_profiling
    profile = train_data.profile_report(title='Pandas Profiling Report')
    profile.to_file(output_file="Titanic data profiling.html")


## 统计量解读

### 一、`MAD` 绝对中位差 `Median Absolute Deviation`

*   绝对中位数 `MAD` 是对单变量数值型数据的样本偏差的一种鲁棒性测量，对于单变量数据来说，它是定义 `数据点到中位数的绝对偏差的中位数`

*   先计算出数据与它们的中位数之间的残差（偏差），`MAD` 就是这些偏差的 `绝对值的中位数`。





