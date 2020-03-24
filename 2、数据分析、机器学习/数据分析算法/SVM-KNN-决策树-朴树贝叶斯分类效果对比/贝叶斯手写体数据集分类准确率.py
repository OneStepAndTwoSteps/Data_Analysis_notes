
from sklearn.metrics import  accuracy_score
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.datasets import load_digits
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# 数据导入
digits=load_digits()
data=digits.data

# 数据切分
x_train,x_test,y_train,y_test=train_test_split(data,digits.target,test_size=0.3)

# 数据归一化Z-score之后我们进行模型训练会报错 Input X must be non-negative 输入X必须是非负的，所以这里我们使用MinMaxScaler 将数据归到[0,1]之间
mm=MinMaxScaler()
train_x_mm=mm.fit_transform(x_train)
test_x_mm=mm.transform(x_test)

# 开始建立模型
model=MultinomialNB()
model.fit(train_x_mm,y_train)

# 模型预测
predicted=model.predict(test_x_mm)

# 输出准确率
print("贝叶斯分类准确率：%.4lf"% accuracy_score(predicted,y_test))


# 贝叶斯分类准确率：0.900
