#author py chen
import PIL.Image  as image
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

def load_image(file_path):
    data=[]
    #读取文件像素值
    img=image.open(file_path)
    width,height=img.size
    for x in range(width):
        for y in range(height):
            # 得到点 (x,y) 的三个通道值, getpixel用于获取给定位置的像素值。
            c1,c2,c3=img.getpixel((x,y))
            data.append([c1,c2,c3])
    mm=MinMaxScaler()
    data=mm.fit_transform(data)
    return np.mat(data),width ,height

data,width,height=load_image('weixin.jpg')
# print(data)
np.set_printoptions(threshold=np.inf)
# 开始使用K-Means聚类
KM=KMeans(n_clusters=4)
KM.fit(data)
# 图像聚类的结果
label=KM.predict(data)
# print("label1: ",label.shape)
# 将图像聚类的结果转化成图像尺寸的矩阵。里面的就是被聚类过的类别0和1
label=label.reshape([width,height])
# print('label2: ',label)
# print("label2: ",label.shape)

# 创建一个图像用于保存聚类的结果，并设置灰度值
# 创建一个新的图片，PIL.Image.new(mode, size, color=0) L表示mode为8位像素，黑白
pic_new=image.new('L',(width,height))
for x in range(width):
    for y in range(height):
        # 这里做是做一个灰度值的深度的扩大，因为我们之前的label.reshape之后其实我们内部的数组已经是二值化了的,准确的说是已经被聚类成0和1这两类
        # 我们这里要做的其实就是扩大颜色之间的区别 使颜色从0，1 变化为127和256。
        # 因为如果你想对图像聚类的结果进行可视化，直接看 0 和 1 是看不出来的，还需要将 0 和 1 转化为灰度值。
        # 灰度值一般是在 0-255 的范围内，我们可以将 label=0 设定为灰度值 255，label=1 设定为灰度值 127。
        pic_new.putpixel((x,y),int(256/(label[x][y]+1))-1)

pic_new.save("new_weixin.jpg","JPEG")
