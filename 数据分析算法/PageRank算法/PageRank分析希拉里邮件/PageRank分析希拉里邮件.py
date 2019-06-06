#author py chen

import networkx as nx
import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

# 数据读取到变量
emails=pd.read_csv("input/Emails.csv")

# 读取别名文件
aliases_data=pd.read_csv("input/Aliases.csv")
alias_dict={}
# iterrows遍历文件的index和行中的内容 将别名文件中的数据读取出来存储为字典格式
for index,row in aliases_data.iterrows():
    # print("row['Alias'],row['PersonID']: ",row['Alias'],row['PersonId']) ==  print("row[1],row[2]: ",row[1],row[2])
    alias_dict[row['Alias']]=row['PersonId']

persons_file=pd.read_csv('input/Persons.csv')
person_dict={}
# iterrows遍历文件的index和行中的内容 将别名文件中的数据读取出来存储为字典格式
for index,row in persons_file.iterrows():
    person_dict[row['Id']]=row['Name']

# 别名转换
def unify_name(name):
    # 名字统一小写
    name=str(name).lower()
    # 除去名字中的逗号和@
    name = name.replace(',','').split('@')[0]
    # 别名转换
    if name in aliases_data.keys():
        return person_dict[alias_dict[name]]
    return name

# 画网络图：layout是我们要话的网络图的布局，spring_laout表示呈中心放射状的图
def show_graph(graph,layout='spring_layout'):
    if layout=="circular_layout":
        positions=nx.circular_layout(graph)
    else:
        positions=nx.spring_layout(graph)
    # 设置网络图的节点大小，大小和pagerank的值相关，因为PageRank的值很小所以我们乘上20000
    # x是pagerank的值，v是名字，是因为下面设置了 nx.set_node_attributes(graph, name = 'pagerank', values=pagerank)
    # data=True 如果为True，则将整个节点属性dict返回为（n，ddict）。如果为False，则仅返回节点n。
    nodesize=[x['pagerank']*20000 for v,x in graph.nodes(data=True)]
    # 设置网络图的边长度 根据权重值设置边长 np.sqrt表示数组各个元素的平方根
    edgesize=[np.sqrt(e[2]['weight']) for e in graph.edges(data=True)]
    # 绘制节点
    nx.draw_networkx_nodes(graph,positions,node_size=nodesize,alpha=0.4)
    # 绘制边
    nx.draw_networkx_edges(graph,positions,edge_size=edgesize,alpha=0.2)
    # 绘制节点的label
    nx.draw_networkx_labels(graph,positions,font_size=10)
    # 输出希拉里邮件中的所有人物关系图

# 将寄件人和收件人的姓名规范化
emails.MetadataTo=emails.MetadataTo.apply(unify_name)
emails.MetadataFrom=emails.MetadataFrom.apply(unify_name)

# 设置边的权重，权重为发邮件的次数
# defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值,否则访问报错，list的默认值是[],int的默认值是0
edge_weights_temp=defaultdict(int)
# 发件人MetadataFrom 收件人MetadataTo 内容RawText
for row in zip(emails.MetadataFrom,emails.MetadataTo,emails.RawText):
    temp=(row[0],row[1])
    # 如果edge_weights_temp没有temp这个key则执行下面代码 创建一个key:value 也就是创建一个权重为1
    if temp not in edge_weights_temp:
        edge_weights_temp[temp]=1
    else:
        # 对应的key上的权重+1
        edge_weights_temp[temp]=edge_weights_temp[temp]+1

# 转化格式刚刚我们定义edge_weights_temp的时候里面的数据是这样的((row[0],row[1]),weight)
edge_weights=[(key[0],key[1],val) for key,val in edge_weights_temp.items()]

# 创建有向图
graph=nx.DiGraph()

# 设置有向边的路径和权重(from,to,weight)
graph.add_weighted_edges_from(edge_weights)

# 计算每一个点的pagerank值，并作为pagerank属性
pagerank=nx.pagerank(graph)

# 将pagerank值作为节点的属性
nx.set_node_attributes(graph,name='pagerank',values=pagerank)

# 画网络图
show_graph(graph)

# ---------------------------------------------------
# 将完整的图片进行一个修剪
# 设置PR值的阈值，筛选大于阈值的节点进行显示
pagerank_threshold=0.006

# 复制一份计算好的网络图
small_graph=graph.copy()

# 裁剪掉PR值小于阈值的节点
for n,p_rank in graph.nodes(data=True):
    if p_rank["pagerank"] < pagerank_threshold:
        small_graph.remove_node(n)

# 画网络图，采用circular_layout格式
show_graph(small_graph,layout='circular_layout')

