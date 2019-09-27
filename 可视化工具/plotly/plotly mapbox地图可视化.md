# plotly mapbox地图可视化

plotly mapbox地图可视化，可以分为两个步骤，第一步设置 mapbox token，第二步 编写代码。


### first set mapbox token

__- [设置mapbox token](https://account.mapbox.com/)__


### 代码案例


    mapbox_access_token="YOUR MAPBOX TOKEN"

    Libaimap = Data([
        Scattermapbox(
            # 绘制散点的经纬度
            lat=data['centroid_lat'],
            lon=data['centroid_lon'],
            mode='markers',
            marker=Marker(
                size=12,
                color=data['peak_hour']
            ),
            # 散点对应的文本
            text=data['province'],
            name='scatter'
        ),
        
        Scattermapbox(
            # 绘制直线端点的经纬度
            lat=data['centroid_lat'],
            lon=data['centroid_lon'],
            mode='lines',
            line=Line(
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


