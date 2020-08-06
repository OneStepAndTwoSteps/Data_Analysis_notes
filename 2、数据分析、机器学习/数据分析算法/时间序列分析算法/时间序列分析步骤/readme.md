# 时间序列相关处理方法

* https://github.com/OneStepAndTwoSteps/Data_Analysis_notes/blob/master/2%E3%80%81%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E3%80%81%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%AE%97%E6%B3%95/%E6%97%B6%E9%97%B4%E5%BA%8F%E5%88%97%E5%88%86%E6%9E%90%E7%AE%97%E6%B3%95/README.md

## 加法模型或乘法模型？

我们公开了时间序列的幼稚分解（应该优先使用更复杂的方法）。它们是分解时间序列的几种方法，但在我们的示例中，我们将简单分解为三个部分。

* 加法模型是：`Y[t] = t[t] + S[t] + e[t]`

* 乘法模型是：`Y[t] = t[t] x S[t] x e[t]`

其中：


* `T[T]`：趋势

* `S[t]`：季节性

* `e[t]`：残余

`加性模型`是线性的，随时间变化的量是相同的。线性趋势是一条直线。线性季节性具有相同的频率（周期宽度）和振幅（周期高度）。

`乘法模型`是非线性的，如二次型或指数型。变化随着时间的推移而增加或减少。非线性趋势是一条曲线，非线性的季节性随时间的推移有增加或减少的频率和/或振幅。

在例子中，如果我们可以看到它不是一个线性模型。这就是我们使用乘法模型的原因。

### `综上所述`

`小结：`就是如果时间序列图的趋势随着时间的推移，序列的季节波动变得越来越大，则建议使用乘法模型；如果序列的季节波动能够基本维持恒定，则建议使用加法模型。

## 时间序列平稳性检测

### 1、`平稳性是先决条件：`

* 时间序列的平稳性是时间序列分析过程中进行许多统计操作处理的基本前提假设。所以，非平稳的时间序列数据常常需要被转换成平稳性的数据。时间序列的平稳性过程是一个随机过程，它的无条件联合概率分布不会随着时间的变换而变换，所以平稳序列的均值和方差等参数也不会随时间的变化而变化，这就为后续的平稳性检验提供理论基础。

* 我们想一下，假如一个时间序列的波动趋势从来没有稳定过，那么它每个时期的波动对于之后一段时期的影响都是无法预测的，因为它随时可能“变脸”。而当一个时间序列的特征维持稳定，比如它的均值和方差是稳定的，那么我们认为在之后的一段时间里，它的数据分布跟历史的数据分布大概率是保持一致的，这时，我们就可以基于历史数据对未来的走势做一个预测，这能帮助我们找到更大概率成功的决策。


* 对时间序列的平稳性进行检验，我们通常可以先查看数据的时间序列图来初步判定数据是否平稳。

  比如通过 `Python` 中的 `seasonal_decompose` 函数可以提取序列的趋势、季节和随机效应。对于非平稳的时间序列，可以通过对趋势和季节性进行建模并将它们从模型中剔除，从而将非平稳的数据转换为平稳数据，并对其残差进行进一步的分析。

因为平稳性是时间序列分析的前提，所以我们需要先进行平稳性检测:

### `2、如何判断数据是否是平稳？`


<div align=center><img width="470" height="550" src="./static/stationary.png"/></div>

平稳性是指序列的时间不变性。（即）时间序列中的两个点之间的关系只取决于它们之间的距离，而不是方向（向前/向后）

当一个时间序列是静止的，它可以更容易地建模。统计建模方法假设或要求时间序列是平稳的。

有多种测试可以用来检查平稳性。


* `seasonal_decompose 方法进行初步判断`

* `ADF( Augmented Dicky Fuller Test)`

* `KPSS`

* `PP (Phillips-Perron test)`

### `2.1、使用 seasonal_decompose 序列的趋势、季节和随机效应`

* `seasonal_decompose` : https://zhuanlan.zhihu.com/p/127032260

* `seasonal_decompose` 周期的指定：https://github.com/statsmodels/statsmodels/issues/3085

除此之外，还可以使用 `小波去噪` 或者 `均值平滑` 的方法查看数据的趋势。


`seasonal_decompose` 使用模板：

    from statsmodels.tsa.seasonal import seasonal_decompose

    weeks_per_year = 365

    time_series = store_sum["CA_1"]
    sj_sc = seasonal_decompose(time_series, freq= weeks_per_year)
    sj_sc.plot()

    plt.show()

输出结果：

<div align=center><img src="./static/3.jpg"/></div>


### `2.2、通常我们会使用 ADF 来进行检测: 使用 ADF 进行平稳检测`

*   Augmented Dickey-Fuller test
    An augmented Dickey–Fuller test (ADF) tests the null hypothesis that a unit root is present in a time series sample. It is basically Dickey-Fuller test with more lagged changes on RHS.

*   时间序列分析之ADF检验: https://blog.csdn.net/FrankieHello/article/details/86766625/

    简单点说，有 `单位根` 是不平稳的一种特殊情况。使用 `单位根检验` ，如果 `单位根` 存在，这个过程就是一个 `随机游走（random walk）`。

    `随机游走（random walk）` 也称 `随机漫步`，`随机行走` 等是指基于过去的表现，无法预测将来的发展步骤和方向。

*   返回平稳的定义，一阶二阶矩不随时间改变就是宽平稳。有单位跟则二阶矩随时间改变而改变，所以不平稳。 其他情况比如有确定性趋势项之类的，也是不平稳，但是没有单位根，减掉趋势项就平稳了。

    具体操作的时候一定要注意是确定性趋势还是随机趋势（单位根），两者相差很大。

*   `ADF` 检验模板：

        from statsmodels.tsa.stattools import adfuller

        # Stationarity tests
        def test_stationarity(timeseries):
            
            #Perform Dickey-Fuller test:
            print('Results of Dickey-Fuller Test:')
            dftest = adfuller(timeseries, autolag='AIC')
            dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
            for key,value in dftest[4].items():
                dfoutput['Critical Value (%s)'%key] = value
            print (dfoutput)

        test_stationarity(ts)

*   输出结果：

        Results of Dickey-Fuller Test:
        Test Statistic                 -4.395704
        p-value                         0.142953
        #Lags Used                      0.000000
        Number of Observations Used    33.000000
        Critical Value (1%)            -3.646135
        Critical Value (5%)            -2.954127
        Critical Value (10%)           -2.615968
        dtype: float64


*   `如何查看是否拒绝原假设：`1%、%5、%10不同程度拒绝原假设的统计值和ADF Test result的比较，ADF Test result同时小于1%、5%、10%即说明非常好地拒绝该假设，本数据中，adf结果为-4.395704， 小于三个level的统计值。所以是平稳的，否则可以进行一阶差分后，再进行检验。


## `3、不平稳该如何解决？`

### `1、常用的方法：差分`

可以通过 `pandas` 来实现差分

    df.diff(1) 实现一阶差分
    df.diff(2) 实现二阶差分


## 时间序列的滞后特征

Lags appears when we think in our prediction like "today is the same that was yesterday". In this kernel lag1 - mean the value of itemcnt that was in previous block (yesterday block), lag2 - itemcnt from 2 day earlier block, lag3 - itemcnt 3 blocks earlier. Lags can help to catch the time trend of cnt variable. Itemcnt is the goal variable so to predict it we used values of item_cnt from the past in different configuration. The same idea for the price.

当我们认为“今天和昨天一样”时，滞后就会出现。在这个内核中，lag-1 表示前一天（昨天）中的 itemcnt 的值，lag-2 来自2天前的块的 itemcnt，lag-3 itemcnt 3天之前的值。滞后有助于捕捉cnt变量的时间趋势。Itemcnt是目标变量，因此为了预测它，我们使用了过去在不同配置中item_cnt的值。价格也一样。




## `extend: 查看趋势的其他方法：`

###  `一、小波去噪`

`小波去噪在寻找销售数据趋势方面显然更有效`

* [小波去噪](https://blog.csdn.net/qq_40587575/article/details/83188527
)

* [小波去噪 2](https://blog.csdn.net/danxibaoxxx/article/details/81539233?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight)


* [小波去噪 3 ](https://www.cnblogs.com/YiYA-blog/p/10705969.html)

* [小波去噪 4 api](https://blog.csdn.net/Fvine_/article/details/83381250)


* [小波阀值去噪法基础](http://blog.sina.com.cn/s/blog_4d7c97a00101cib3.html)

* [kaggle Wavelet Transform](https://www.kaggle.com/theoviel/denoising-with-direct-wavelet-transform)

当遇到销售数据非常不稳定时，我们需要某种“去噪”技术来发现销售数据的潜在趋势并作出预测。

现在，我将展示如何消除这些不稳定的销售价格，以提取潜在的趋势。这种方法可能会丢失原始时间序列中的一些信息，但在提取有关时间序列趋势的某些特征时，它可能是有用的。

小波去噪（通常用于电信号）是一种去除时间序列中不必要噪声的方法。这种方法计算称为“小波系数”的系数。这些系数决定了保留哪些信息（信号）和丢弃哪些信息（噪声）。

我们利用平均绝对偏差（MAD）值来理解销售中的随机性，从而确定时间序列中小波系数的最小阈值。我们从小波中过滤出低系数，然后从剩余的系数中重建销售数据，就这样，我们成功地从销售数据中去除了噪声。

#### `定义小波去噪函数`

    def maddest(d, axis=None):
        return np.mean(np.absolute(d - np.mean(d, axis)), axis)

    def denoise_signal(x, wavelet='db4', level=1):
        coeff = pywt.wavedec(x, wavelet, mode="per")
        sigma = (1/0.6745) * maddest(coeff[-level])

        uthresh = sigma * np.sqrt(2*np.log(len(x)))
        coeff[1:] = (pywt.threshold(i, value=uthresh, mode='hard') for i in coeff[1:])

        return pywt.waverec(coeff, wavelet, mode='per')

#### `绘图`

    y_w1 = denoise_signal(x_1)
    y_w2 = denoise_signal(x_2)
    y_w3 = denoise_signal(x_3)


    fig = make_subplots(rows=3, cols=1)

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_1)), mode='lines+markers', y=x_1, marker=dict(color="mediumaquamarine"), showlegend=False,
                name="Original signal"),
        row=1, col=1   # 指定绘制的子图
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_1)), y=y_w1, mode='lines', marker=dict(color="darkgreen"), showlegend=False,
                name="Denoised signal"),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_2)), mode='lines+markers', y=x_2, marker=dict(color="thistle"), showlegend=False),
        row=2, col=1
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_2)), y=y_w2, mode='lines', marker=dict(color="purple"), showlegend=False),
        row=2, col=1
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_3)), mode='lines+markers', y=x_3, marker=dict(color="lightskyblue"), showlegend=False),
        row=3, col=1
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_3)), y=y_w3, mode='lines', marker=dict(color="navy"), showlegend=False),
        row=3, col=1
    )

    fig.update_layout(height=1200, width=800, title_text="Original (pale) vs. Denoised (dark) sales")
    fig.show()

<div align=center><img width="550" height="650" src="./static/2.jpg"/></div>



###  `二、均值平滑`

均值平滑是一种相对简单的去噪时间序列数据的方法。在这种方法中，我们取一个固定大小的“窗口”（如10）。我们首先将窗口放在时间序列的开始处（前十个元素），然后计算该部分的平均值。我们现在在时间序列中向前移动一个特定的“步幅”，计算新窗口的平均值并重复这个过程，直到到达时间序列的末尾。然后，我们计算出的所有平均值被连接到一个新的时间序列中，形成去噪后的销售数据。

`但是一般来说，小波去噪在寻找销售数据趋势方面显然更有效。尽管如此，平均平滑或“滚动平均”也可以用于计算建模的有用特征。`

#### `均值平滑函数`

    def average_smoothing(signal, kernel_size=3, stride=1):
        sample = [0]*(kernel_size-stride)    # 通过 len(y_a1) 可以发现与原始数据同长度
        start = 0
        end = kernel_size
        while end <= len(signal):
            start = start + stride
            end = end + stride
            sample.extend([np.mean(signal[start:end])])
        return np.array(sample)

#### `绘图`

    y_a1 = average_smoothing(x_1)
    y_a2 = average_smoothing(x_2)
    y_a3 = average_smoothing(x_3)

    fig = make_subplots(rows=4, cols=1)

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_1)), mode='lines+markers', y=x_1, marker=dict(color="lightskyblue"), showlegend=False,
                name="Original sales"),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_1)), y=y_a1, mode='lines', marker=dict(color="navy"), showlegend=False,
                name="Denoised sales"),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_2)), mode='lines+markers', y=x_2, marker=dict(color="thistle"), showlegend=False),
        row=2, col=1
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_2)), y=y_a2, mode='lines', marker=dict(color="indigo"), showlegend=False),
        row=2, col=1
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_3)), mode='lines+markers', y=x_3, marker=dict(color="mediumaquamarine"), showlegend=False),
        row=3, col=1
    )

    fig.add_trace(
        go.Scatter(x=np.arange(len(x_3)), y=y_a3, mode='lines', marker=dict(color="darkgreen"), showlegend=False),
        row=3, col=1
    )


    # fig.add_trace(
    #     go.Scatter(x=np.arange(int(len(x_1)/3)), mode='lines+markers', y=pd.Series(np.array(x_1)).rolling(3).mean(), marker=dict(color="lightskyblue"), showlegend=False,
    #                name="Original sales"),
    #     row=4, col=1
    # )

    fig.update_layout(height=1200, width=800, title_text="Original (pale) vs. Denoised (dark) signals")
    fig.show()

<div align=center><img width="650" height="600" src="./static/1.jpg"/></div>


## FFT 快速傅里叶变换

傅里叶变换介绍：

* [傅里叶分析之掐死教程（完整版）更新于2014.06.06](https://zhuanlan.zhihu.com/p/19763358)

* [傅里叶变换、拉普拉斯变换、Z 变换的联系是什么？为什么要进行这些变换？](https://www.zhihu.com/answer/774074211)

* [如何通俗地解释什么是离散傅里叶变换？](https://www.zhihu.com/answer/542909849)

* [如何通俗地讲解傅立叶分析和小波分析间的关系？](https://www.zhihu.com/question/22864189/answer/40772083)

* [傅里叶变换 fft_generic halcon](https://www.cnblogs.com/tmdsleep/p/5424854.html)


通过傅里叶变换可以看出时间序列的周期性：

* [时间序列检测周期性 FFT 和 ACF](https:/www.zhihu.com/answer/952512004)

* [时间序列检测周期性 kaggle](https://www.kaggle.com/kk0105/wikipedia-traffic-eda-arima)



## `时间序列相关资料`

### `1、关于时间序列分析的 参考链接 ：`

* [数据分析之时间序列分析](https://www.jianshu.com/p/ff6abad2514f)

* [Python量化基础：时间序列的平稳性检验](https://blog.csdn.net/qixizhuang/article/details/86716149)


* [时间序列-平稳性](https://www.jianshu.com/p/dedf38416694)

* [时间序列预测初学者指南（Python）](https://www.biaodianfu.com/time-series-forecasting-codes-python.html)


### `2、关于时间序列分析的实战 notebook ：`

* `M5 Forecasting - Accuracy `：https://www.kaggle.com/kk0105/time-series-forecasting-eda-sarima

* `Web Traffic Time Series Forecasting `：https://www.kaggle.com/kk0105/predictive-analysis-with-different-approaches
