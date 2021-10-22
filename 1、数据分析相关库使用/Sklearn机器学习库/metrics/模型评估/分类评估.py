from sklearn.metrics import accuracy_score,precision_score
from sklearn.metrics import confusion_matrix

y_pred= [0,1,0,0,0,1,1,1,1,1] # y_pred 

y_test= [0,0,1,0,0,1,1,1,0,1] # y_test 


print(confusion_matrix(y_pred,y_test))

# TP:3 , FP:1 , FN:2 , TN:4

print(accuracy_score(y_pred,y_test))
print(precision_score(y_pred,y_test,average='macro'))  # TP/(TP+FP)



