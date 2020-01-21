from sklearn.feature_selection import VarianceThreshold
import numpy as np

X=np.array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11],
       [12, 13, 14],
       [15, 16, 17],
       [18, 19, 20],
       [21, 22, 23],
       [24, 25, 26],
       [27, 28, 29]])

print(X[:,2])

# 改变第三列的值为2
X[:,2]=1
print(X[:,2])

# 设置阈值，特征小于该值会被删除
vt=VarianceThreshold(threshold=3)
new_x=vt.fit_transform(X)

print(new_x)

#输出每一列的方差
print(vt.variances_)

