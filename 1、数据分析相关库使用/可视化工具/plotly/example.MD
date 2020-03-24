# Plotly绘图工具

plotly本身是基于javascript开发的，但是提供了大量与其他主流数据分析语言的API，比如Python， R， Matlab


### 导入包

    import plotly.offline as py     # 绘图的函数
    import plotly.graph_objs as go  # 定义绘图的参数


### 案例

    # Scatter plot 
    trace = go.Scatter(     # 创建一个绘图对象
        y = feature_dataframe['Random Forest feature importances'].values,  # y轴
        x = feature_dataframe['features'].values,                           # x轴
        mode='markers',                                                     # mode默认为由点连接的折线图，这里的markers为散点图
        marker=dict(                                                        # marker定义每一个点的性质，比如大小，颜色
            sizemode = 'diameter',
            sizeref = 1,                                                    
            size = 25,                                                      # 点的大小
    #       size= feature_dataframe['AdaBoost feature importances'].values, # 按重要程度绘制节点大小
            #color = np.random.randn(500), #set color equal to a variable
            color = feature_dataframe['Random Forest feature importances'].values,  # 按重要程度绘制节点颜色
            colorscale='Portland',                                          # 颜色标度的配色方案
            showscale=True                                                  # 显示右侧的颜色标度
        ),
        text = feature_dataframe['features'].values                         
    )
    data = [trace]                                                          # 将trace保存于列表之中

    layout= go.Layout(                                             # 创建图层对象
        autosize= True,                                            # 自动设置图像大小，如果为False可以设置下面的width和height
    #   width=1000,                                                # 图像的宽度
    #   height=800,                                                # 图像的高度
        title= 'Random Forest Feature Importance',                 # 标题的名称
        hovermode= 'closest',                                      # str型或False，用于设置悬停交互的方式，有'x'、'y'、'closest'和False这几个可选项，False表示无悬停交互方式
    #     xaxis= dict(                                             # 设置x轴的信息
    #         title= 'Pop',                                        # x轴的标题
    #         ticklen= 5,                                          # int型，设置刻度标签的像素长度
    #         zeroline= False,                                     # bool型，控制是否在0值处绘制0刻度线
    #         gridwidth= 2,                                        # int型，控制网格线的像素宽度
    #     ),
        yaxis=dict(                                                # 设置y轴的信息
            title= 'Feature Importance',                           # y轴的标题
            ticklen= 5,
            gridwidth= 2                                           
        ),
        showlegend= False                                          # 显示右侧的颜色标度
    )
    fig = go.Figure(data=data, layout=layout)                      # 将graph部分和layout部分组合成figure对象
    py.iplot(fig,filename='scatter2010')                           # 绘图



###  案例二

    # 计算出每一年的发行的电影数量，让其按index进行排序
    d1 = train['release_date_year'].value_counts().sort_index()
    # 计算每年的 电影总收入
    d2 = train.groupby(['release_date_year'])['revenue'].sum()
    # 计算每年的 电影平均收入
    d3 = train.groupby(['release_date_year'])['revenue'].mean()
    # go.Scatter 根据数据进行绘制图线，顺序和代表的图例一一对应
    data = [go.Scatter (x=d1.index, y=d1.values, name='film count'), go.Scatter(x=d2.index, y=d2.values, name='total revenue', yaxis='y2')]
    #  yaxis='y2' 对应下面的 yaxis2 (固定写法)
    layout = go.Layout(dict(title = "Number of films and total revenue per year",
                    xaxis = dict(title = 'Year'),
                    yaxis = dict(title = 'Count'),
                    # overlaying 表示是否覆盖，不指定则只会绘制后面的线条
                    yaxis2 = dict(title='Total revenue', overlaying='y', side='right'),

                    ),
                    # orientation 指定图例放置的位置，v为右侧，h为下侧
                    legend=dict(orientation="h"))
    py.iplot(dict(data=data, layout=layout))

#### 如下图

<div align=center><img  src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/plotly/example/2.png"/></div>

