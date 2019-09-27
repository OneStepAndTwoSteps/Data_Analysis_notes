# plotly mapbox地图可视化

plotly mapbox地图可视化，可以分为两个步骤，第一步设置 mapbox token，第二步 制作数据，第三步 编写代码。


### first set mapbox token

__- [设置mapbox token](https://account.mapbox.com/)__


### 制作数据

制作一个 dataframe 数据，在plotly中可以直接引用 dataframe 中的数据


### 代码案例 1


    mapbox_access_token="YOUR MAPBOX TOKEN"

    Libaimap = Data([
        Scattermapbox(
            # 绘制散点的经纬度
            lat=data['centroid_lat'],   # 引用 data 中的  centroid_lat 作为纬度
            lon=data['centroid_lon'],   # 引用 data 中的  centroid_lon 作为经度
            mode='markers',
            marker=Marker(              # 绘制点
                size=12,                # 图中点的大小
                color=data['peak_hour'] # 图中点的颜色，数据值不同他们的点颜色也不同
            ),
            # 散点对应的文本
            text=data['province'],      # text 表示描述信息，当鼠标移动到节点处，会有显示
            name='scatter'
        ),
        
        Scattermapbox(
            # 绘制直线端点的经纬度
            lat=data['centroid_lat'],
            lon=data['centroid_lon'],
            mode='lines',
            line=Line(              # 绘制线                  
                color='#ff00ee',
                width=1
            ),
            # 散点对应的文本
            text=data['province'],
            name='line'
        )
    ])

    layout = Layout(
        title='“初唐四杰”之一——王勃',
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            # 地图中心坐标，不要远离绘制的散点坐标
            center=dict(
            lat=28.25591,
            lon=112.98626),
            pitch=0,
            zoom=4
        ),
    )

    fig = dict(data=Libaimap, layout=layout)
    iplot(fig)

### 效果展示

<div align=center><img  src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/plotly/mapbox/1.png"/></div>


### 代码案例 2


    px.set_mapbox_access_token("YOUR MAPBOX TOKEN")

    # px.scatter_mapbox 是已经封装好了的方法，可用于绘制地图上的点 
    # data 就是指明我们的dataframe
    # lat 用于指定 dataframe 中的 centroid_lat 列作为纬度
    # lon 用于指定 dataframe 中的 centroid_lon 列作为经度
    # color 用于指定 dataframe 中的 peak_hour 列作为颜色列表，里面的数据值如果不同则节点颜色不同
    # size 用于指定 dataframe 中的 size 列作为节点大小的标准，里面的数据值如果不同则节点大小不同
    # text="province" 就是描述信息
    # opacity=0.4 透明度
    # zoom 图生成时，我们的缩放大小为多少，越小地图看到的面积越多。
    # size_max=15 节点最大为15
    # title 标题
    fig = px.scatter_mapbox(data, lat="centroid_lat", lon="centroid_lon",color="peak_hour",size='size',text="province",opacity=0.4,
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=5,title='初唐四杰”之一——王勃')


    fig.show()

### 效果展示

<div align=center><img  src="https://raw.githubusercontent.com/OneStepAndTwoSteps/Data_Analysis/master/static/plotly/mapbox/2.png"/></div>


