#author py chen

import networkx as nx

# 创建有向边：nx.Graph()创建的为无向边
G=nx.DiGraph()
# 增加节点：可以使用 G.add_node(A)增加一个A节点 也可以使用G.add_nodes_from(['B','C','D','E'])增加节点集合
# 删除节点：G.remove_nodes(node) 也可以使用G.remove_nodes_from(['B','C','D','E'])
# 查询节点：G.nodes()
# 查询节点个数：G.number_of_nodes()
# 指定节点的方向 从edge[0] 指向 edge[1]

# 定义有向边之间的关系
edges=[("A","B"),("A","C"),("A","D"),("B","A"),("B","D"),("C","A"),("D","B"),("D","C")]
for edge in edges:
    # 指定增加边: G.add_edge("A","B")添加指定从A->B的边 也可以使用G.add_edges_from(['B','C','D','E'])增加节点集合
    # G.add_weight_edges_from从带有权重的边的集合中添加 其中该函数接受一个或者多个三元组[u,v,w]作为参数，u,v,w分别代表起点、终点和权重
    # 删除边：G.remove_edges() 也可以使用G.remove_edges_from()
    # 查询边：G.edges()
    # 查询边个数：G.number_of_edges()
    G.add_edge(edge[0],edge[1])


# alpha为阻尼因子，默认值：0.85
# pagerank_list=nx.pagerank(G,alpha=1)

pagerank_list=nx.pagerank(G)

# 将 pagerank 数值作为节点的属性
nx.set_node_attributes(G, name = 'pagerank', values=pagerank_list)
for  v,x in G.nodes(data=True):
    print(v,x)
# 输出结果
# A {'pagerank': 0.33333396911621094}
# B {'pagerank': 0.22222201029459634}
# C {'pagerank': 0.22222201029459634}
# D {'pagerank': 0.22222201029459634}

print("pagerank value equal: %s "%pagerank_list)
# 输出结果:
# 当 alpha=1时 pagerank value equal: {'A': 0.33333396911621094, 'B': 0.22222201029459634, 'C': 0.22222201029459634, 'D': 0.22222201029459634}
# 当 alpha=0.85时 pagerank value equal: {'A': 0.3245609358176831, 'B': 0.22514635472743894, 'C': 0.22514635472743894, 'D': 0.22514635472743894} 

# data=True 如果为True，则将整个节点属性dict返回为（n，ddict）。如果为False，则仅返回节点n。
print(G.nodes(data=True))
print(G.nodes())
# 输出结果：
# [('A', {'pagerank': 0.33333396911621094}), ('B', {'pagerank': 0.22222201029459634}), ('C', {'pagerank': 0.22222201029459634}), ('D', {'pagerank': 0.22222201029459634})]
# ['A', 'B', 'C', 'D']

