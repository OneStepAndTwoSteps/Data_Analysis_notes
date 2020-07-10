# note

## 小波去噪

[小波去噪](https://blog.csdn.net/qq_40587575/article/details/83188527
)

[小波去噪 2](https://blog.csdn.net/danxibaoxxx/article/details/81539233?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight)


[小波去噪 3 ](https://www.cnblogs.com/YiYA-blog/p/10705969.html)

[小波去噪 4 api](https://blog.csdn.net/Fvine_/article/details/83381250)


[小波阀值去噪法基础](http://blog.sina.com.cn/s/blog_4d7c97a00101cib3.html)

[kaggle Wavelet Transform](https://www.kaggle.com/theoviel/denoising-with-direct-wavelet-transform)

当遇到销售数据非常不稳定时，比如，销售额连续几天为零，而在其他时候，则会在几天内保持在峰值。因此，我们需要某种“去噪”技术来发现销售数据的潜在趋势并作出预测。


现在，我将展示如何消除这些不稳定的销售价格，以提取潜在的趋势。这种方法可能会丢失原始时间序列中的一些信息，但在提取有关时间序列趋势的某些特征时，它可能是有用的。

小波去噪（通常用于电信号）是一种去除时间序列中不必要噪声的方法。这种方法计算称为“小波系数”的系数。这些系数决定了保留哪些信息（信号）和丢弃哪些信息（噪声）。

我们利用平均绝对偏差（MAD）值来理解销售中的随机性，从而确定时间序列中小波系数的最小阈值。我们从小波中过滤出低系数，然后从剩余的系数中重建销售数据，就这样，我们成功地从销售数据中去除了噪声。

### 定义小波去噪函数

    def maddest(d, axis=None):
        return np.mean(np.absolute(d - np.mean(d, axis)), axis)

    def denoise_signal(x, wavelet='db4', level=1):
        coeff = pywt.wavedec(x, wavelet, mode="per")
        sigma = (1/0.6745) * maddest(coeff[-level])

        uthresh = sigma * np.sqrt(2*np.log(len(x)))
        coeff[1:] = (pywt.threshold(i, value=uthresh, mode='hard') for i in coeff[1:])

        return pywt.waverec(coeff, wavelet, mode='per')

### 绘图

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



## 均值平滑

均值平滑是一种相对简单的去噪时间序列数据的方法。在这种方法中，我们取一个固定大小的“窗口”（如10）。我们首先将窗口放在时间序列的开始处（前十个元素），然后计算该部分的平均值。我们现在在时间序列中向前移动一个特定的“步幅”，计算新窗口的平均值并重复这个过程，直到到达时间序列的末尾。然后，我们计算出的所有平均值被连接到一个新的时间序列中，形成去噪后的销售数据。

### 均值平滑函数

    def average_smoothing(signal, kernel_size=3, stride=1):
        sample = []
        start = 0
        end = kernel_size
        while end <= len(signal):
            start = start + stride
            end = end + stride
            sample.extend(np.ones(end - start)*np.mean(signal[start:end]))
        return np.array(sample)


### 绘图

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
