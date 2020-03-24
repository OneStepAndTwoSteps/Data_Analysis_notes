import numpy as np
from sklearn import metrics
y = np.array([1, 1, 2, 2])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)

print('取不同阈值时fpr的变化：',fpr)
print('取不同阈值时tpr的变化：',tpr)


print('\n')
print('阈值：',thresholds)


# 取不同阈值时fpr的变化： [0.  0.5 0.5 1. ]
# 取不同阈值时tpr的变化： [0.5 0.5 1.  1. ]
#
#
# 阈值： [0.8  0.4  0.35 0.1 ]