#author py chen

import numpy as np


w2=[
    [0,1/2,1,0],
    [1/3,0,0,1/2],
    [1/3,0,0,1/2],
    [1/3,1/2,0,0],
]


v=[
    [1/4],[1/4],[1/4],[1/4]
]

w2=np.asarray(w2)
v=np.asarray(v)

print(w2)
print(v)

print(w2.shape)
print(v.shape)

for i in range(100):
    if i == 0:
        result_old = np.dot(w2, v)
        # print(result_old)
        result_new=result_old
        continue

    result_old=np.dot(w2,result_old)

    # 这里不能使用这样相等的方法，因为result_new和result_old是一直在变化的，我们将其输出出来已经是限制了显示位数，看起来相等，但是其实不相等
    # if (result_new==result_old).all():
    # 保留result_new中的前五位數，第六数四舍五入到第五位数中，这样我们判断只要这两个数组，小数点之前的数和小数点后五位数相等我们就判断W的影响力不在发送变化
    # (A==B).all() 用来测试array(A == B)的所有值是否为True。
    if (np.around(result_new,decimals=8) == np.around(result_old,decimals=8) ).all():
        print(result_old)
        print(i)
        break
    else:
        result_new=result_old

# 最后输出：
#  [[0.33333333]
#  [0.22222222]
#  [0.22222222]
#  [0.22222222]]       
        
        
        
