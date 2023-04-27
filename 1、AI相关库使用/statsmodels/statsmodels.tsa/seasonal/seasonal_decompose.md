# seasonal_decompose

季节分解显示了一个时间序列在多大程度上表现出季节性和趋势性。这是一个很好的方式来考虑有多少销售是由于季节性，趋势，或一次性事件，如假日。

## example

* 现在我们将使用每年一次的频率，直到我们做更详细的分析。

        from statsmodels.tsa.seasonal import seasonal_decompose
        
        weeks_per_year = 365

        time_series = store_sum["CA_1"]
        sj_sc = seasonal_decompose(time_series, freq= weeks_per_year)
        sj_sc.plot()

        plt.show()

* 输出结果：

<div align=center><img width="400" height="300" src="./static/1.png"/></div>

