#author py chen

import networkx as nx
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# 创建有向边：nx.Graph()创建的为无向边
G=nx.DiGraph()
# 增加节点：可以使用 G.add_node(A)增加一个A节点 也可以使用G.add_nodes_from(['B','C','D','E'])增加节点集合
# 删除节点：G.remove_nodes(node) 也可以使用G.remove_nodes_from(['B','C','D','E'])
# 查询节点：G.nodes()
# 查询节点个数：G.number_of_nodes()
# 指定节点的方向 从edge[0] 指向 edge[1]


# 定义有向边之间的关系
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=5)
G.add_edge('A', 'D', weight=10)

edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
print('edge_labels: ',edge_labels)

print(G.edges())

# 因为networkx可视化节点位置是随机的，所以我们这样可以进行固定设置
fixed_position = {'A':[ 0.55072989,  0.00426975], 'B': [ 1.,  0.], 'D': [ 0.38252302,  0.10520343], 'C': [ 0.,0.09481996]}

# 可视化布局 除了 spring_layout 外，NetworkX 还有另外三种可视化布局，circular_layout（在一个圆环上均匀分布节点），random_layout（随机分布节点 ），shell_layout（节点都在同心圆上）。
position = nx.spring_layout(G,pos=fixed_position)
sizes=1000
alpha=0.5
colors=range(5)
# 定义节点属性 nodelist中定义我们要定义的节点是哪些节点，node_color是nodelist节点中的颜色，node_size节点大小，alpha透明度,edgecolors节点边框颜色,linewidths节点边框的宽度
nx.draw_networkx_nodes(G,position, nodelist=['A'], node_color="r",node_size=sizes,alpha=alpha,edgecolors='black',linewidths=3)
nx.draw_networkx_nodes(G,position, nodelist=['C'], node_color="g",node_size=sizes,alpha=alpha)
nx.draw_networkx_nodes(G,position, nodelist=['B'], node_color="lightgrey",node_size=sizes,alpha=alpha)
nx.draw_networkx_nodes(G,position, nodelist=['D'], node_color="lightgrey",node_size=sizes,alpha=alpha)
# 同于设置边的属性：width边的宽度 用于映射边缘强度的Colormap(根据colors的大小显示线的深浅，越大颜色显示的越深)
nx.draw_networkx_edges(G,position,edge_color=colors,width=3,edge_cmap=plt.cm.Blues,style='dashed')
# 用于显示节点的名称 edge_labels为线的权重，会显示出来 font_size字体大小 labels将key替换成value
nx.draw_networkx_labels(G,position,edge_labels=edge_labels,font_size=20,labels={"A":1,"B":'B','C':'C','D':'D'})
# 隐藏坐标轴
plt.axis('off')
plt.show()

# nx.draw(G, with_labels=True, edge_color='b', node_size=1000,edge_cmap=plt.cm.Blues)
# plt.show()
