from sklearn.metrics import accuracy_score,precision_score
from sklearn.metrics import confusion_matrix

y_pred= [0,1,0,0,0,1,1,1,1,1] # y_pred 

y_test= [0,0,1,0,0,1,1,1,0,1] # y_test 


print(confusion_matrix(y_test,y_pred))



print(accuracy_score(y_test,y_pred))

print(precision_score(y_test,y_pred,average='macro'))  # TP/(TP+FP)
print(precision_score(y_pred,y_test,average='macro'))   # 错误写法，traget 和 pred 写反了

# 写反两者的计算结果是不一样的。