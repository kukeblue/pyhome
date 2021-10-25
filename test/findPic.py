from PIL import Image
import numpy as np
import sklearn
from sklearn import cluster
import cv2

def Euclidean_distance(a, b):#欧氏距离
    return sum((np.array(a)-np.array(b))**2)**(0.5)
def clustering(temp_get):#用DBSCAN聚类
    mod = sklearn.cluster.DBSCAN(eps=5,min_samples=8,)
    mod.fit(temp_get)
    pro = mod.fit_predict(temp_get)
    pro = np.array(pro)
    index, num = np.unique(pro,return_counts=True)
    max_num =index[np.where(np.array(num)==np.array(num).max())]
    temp_get = [temp_get[i] for i in range(len(temp_get)) if pro[i] == max_num]
    return temp_get

def image_pyramid():  # 预处理，图像金字塔
    image_find =cv2.imread("1.png")
    image_big = cv2.imread("3.png")
    for i in range(6):
        image_find = cv2.pyrDown(image_find)
        #cv2.imshow('1',image_find)
        #print(image_find.shape)
    cv2.imwrite('1_temp.png', image_find)
    for i in range(3):
        image_big = cv2.pyrDown(image_big)
        #cv2.imshow('1',image_big)
        #print(image_find.shape)
    cv2.imwrite('2_temp.png', image_big)


def image_contrast():  # 再次读取图片进行操作
    image_find = Image.open("1_temp.png")
    image_big = Image.open("2_temp.png")
    data1 = image_find.load()
    data2 = image_big.load()
    x,y = image_big.size
    a = list(data1[0,0])
    temp_get=[]
    for i in range(x):
        for j in range(y):
            b= data2[i,j]
            temp = Euclidean_distance(a,b)#统计整张图片的的像素点与目标图像像素点的欧氏距离
            if temp < 50:
                temp_get.append([i,j])#保存符合要求的像素点的位置
    temp_get = clustering(temp_get)#聚类，返回最大的那一类的坐标
    data2 = Draw_square(temp_get,data2)
    image_big.show()

def Draw_square(temp_get, data2): # 画图，画出正方形框起来
    temp_x = [temp_get[i][0] for  i in range(len(temp_get))]
    temp_y = [temp_get[i][1] for  i in range(len(temp_get))]
    temp_y = np.array(temp_y)
    temp_x = np.array(temp_x)
    max_x = int(temp_x.max())
    max_y = int(temp_y.max())
    min_x = int(temp_x.min())
    min_y= int(temp_y.min())
    for i in range(max_x-min_x):
        data2[min_x+i, min_y] = (255, 0, 0)
        data2[min_x+i, max_y] = (255, 0, 0)
    for j in range(max_y-min_y):
        data2[min_x, min_y+j] = (255, 0, 0)
        data2[max_x, min_y+j] = (255, 0, 0)
    return data2


if __name__ == "__main__":
    image_pyramid()
    image_contrast()
