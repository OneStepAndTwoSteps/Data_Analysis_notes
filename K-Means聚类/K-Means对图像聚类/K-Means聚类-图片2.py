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
KM=KMeans(n_clusters=16)
KM.fit(data)
# 图像聚类的结果
label=KM.predict(data)
# print("label1: ",label.shape)
# 将图像聚类的结果转化成图像尺寸的矩阵。
label=label.reshape([width,height])
print('label2: ',label)
# print("label2: ",label.shape)

# 创建一个图像用于保存聚类的结果，并设置灰度值
# 创建一个新的图片，PIL.Image.new(mode, size, color=0) L表示mode为8位像素，黑白
pic_new=image.new('RGB',(width,height))
for x in range(width):
    for y in range(height):
        # 实际上label[x,y]是得到当前点的类别，kmeans.cluster_centers_可以得到某类别的数值，
        # 因为图像JPG是3个通道，所以通过kmeans.cluster_centers_[label[x, y], 0]，kmeans.cluster_centers_[label[x, y], 1]，
        # kmeans.cluster_centers_[label[x, y], 2]可以获得这3个通道的数值，然后将这些数值作为当前点的数值。因为当前点已经被划分到了这个类别，
        # 所以数值是一致的。这样如果原来图像中有N种颜色，现在聚类数是16，相当于每个点的颜色值就变成了其中一个类别的颜色值，也就是变成了16种颜色
        # ，完成了聚类（降维）。
        c1=KM.cluster_centers_[label[x][y],0]
        c2=KM.cluster_centers_[label[x][y],1]
        c3=KM.cluster_centers_[label[x][y],2]

        pic_new.putpixel((x,y),(int(c1*256)-1,int(c2*256)-1,int(c3*256)-1))

pic_new.save("new_weixin2.jpg","JPEG")