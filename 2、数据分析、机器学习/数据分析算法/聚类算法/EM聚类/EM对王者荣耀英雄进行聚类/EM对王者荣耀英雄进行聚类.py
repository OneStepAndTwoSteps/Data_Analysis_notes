#author py chen
from sklearn.mixture import GaussianMixture
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

hero_data=pd.read_csv('heros.csv',encoding='gb18030')
print(hero_data.head())

# 获取到各个属性
features=hero_data.columns.values.tolist()[1:-2]
print(features)

# 各个属性相关的信息
data=hero_data[features]
# print(data)
# exit()

# 可视化各个英雄的属性关系
# 设置plt正确显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用于正常显示负号

# 用热力图显示字段之间的相关性
corr=data[features].corr()
# 指定高和宽度为14
plt.figure(figsize=(14,14))
sns.heatmap(corr,annot=True)
plt.show()

# 通过热力图我们可以看到属性之间的相关性，我们将相关性较高的属性中选取一个作为代表，目的是减少特征值
remain_features=['最大生命', '初始生命', '法力成长', '最高物攻', '初始物攻', '最大物防', '初始物防',  '最大攻速', '攻击范围']
data=data[remain_features]
# 将 最大攻速 化成小数,因为在数据规范化中，最大攻速是百分数，不适合进行矩阵运算，所以转化成小数
data["最大攻速"]=data["最大攻速"].apply(lambda x:float(x.strip('%'))/100)
# 字符串也不适合进行矩阵运算，这里我们进行一个映射用0代表近战，用1表示远程
data["攻击范围"]=data["攻击范围"].map({'近战':0,'远程':1})

# 采用Z-scores来规范化数据
ss=StandardScaler()
data=ss.fit_transform(data)

# 创建GMM聚类
gmm=GaussianMixture(n_components=30,covariance_type='full',max_iter=100)
# 使用fit函数传入样本特征矩阵，模型生成聚类器 训练模型
gmm.fit(data)
print("gmm.fit(data): ",gmm.fit(data))

# 预测聚类结果 这里传入相同的数据进行预测，因为使用fit训练不会返回聚类结果，所以使用predict返回
predicted=gmm.predict(data)
print("predicted: ",predicted)

# 将分组结果输出到CSV文件
hero_data.insert(0,'分组',predicted)
hero_data.to_csv('heros_out.csv',index=False,sep=',')

# 采用calinski_harabaz 指标来评估聚类的效果 分数越高表示聚类效果越好，也就是相同类的差异越小，不同类之间的差异越大。
from sklearn.metrics import calinski_harabaz_score
print(calinski_harabaz_score(data, predicted))

# 分数： 17.228071078913562

# 我们通过减少我们的分类的类别获得了更高的准确率 why?
# 总样本过少，分成的类越多，每个类的所拥有的个体相对越少，类中个体差异变大，导致指标分数变低。
