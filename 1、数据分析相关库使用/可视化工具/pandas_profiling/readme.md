# pandas_profiling

`pandas` 的 `df.describe()` 函数虽然功能强大，但对于进行认真的探索性数据分析却有些基础。 `pandas_profiling` 扩展了 `pandas DataFrame` 的功能。

可使用 `df.profile_report()` 进行快速数据分析。


## 使用方法

    import pandas_profiling
    profile = train_data.profile_report(title='Pandas Profiling Report')
    profile.to_file(output_file="Titanic data profiling.html")
