from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_objects import XYZColor, sRGBColor,LabColor
from colormath.color_conversions import convert_color
import numpy as np
import math
import cv2
import os

#train_set
pic_dir = 'C:\\Users\\renxinyuan\\Desktop\\color_test\\gen_color_pic\\'
#test_set
pic_tests_dir = 'C:\\Users\\renxinyuan\\Desktop\\color_test\\tests\\'

#train 图片的文件名
colors = os.listdir(pic_dir)
#colors = ['cyan.jpg']
#test 图片文件名
test_pic = os.listdir(pic_tests_dir)


#计算正确率的分子分母
count = len(test_pic)
right_num = 0.0

#list1 存放所有的test的LAB向量的对象 list2为train
vector_list1 = []
vector_list2 = []

for t in test_pic:
    #line_vector存放一行的向量，vector_test存放一张图片的向量，vector_list1存放所有test图片的向量
    vector_test = []
    img1 = cv2.imread(pic_tests_dir+t, cv2.IMREAD_COLOR)
    #测试集图像不一定是400*400，所以要转换
    img1 = cv2.resize(img1, (50, 50), interpolation=cv2.INTER_CUBIC)
    print(t, 'is loading..........')
    for i in range(img1.shape[0]):
        line_vector = []
        for j in range(img1.shape[1]):
            #rgb转xyz转lab
            rgb1 = sRGBColor(img1[i][j][0], img1[i][j][1], img1[i][j][2])
            xyz1 = convert_color(rgb1, XYZColor)
            lab1 = convert_color(xyz1, LabColor, target_illuminant=str)
            line_vector.append(lab1)
        vector_test.append(line_vector)
    vector_list1.append(vector_test)

print('train_set loading complete!!!')

for c in colors:
    vector = []
    img2 = cv2.imread(pic_dir+c,cv2.IMREAD_COLOR)
    img2 = cv2.resize(img2, (50, 50), interpolation=cv2.INTER_CUBIC)
    print(c, 'is loading..........')
    for i in range(img2.shape[0]):
        line_vector_2 = []
        for j in range(img2.shape[1]):
            rgb2 = sRGBColor(img2[i][j][0], img2[i][j][1], img2[i][j][2])
            xyz2 = convert_color(rgb2, XYZColor)
            lab2 = convert_color(xyz2, LabColor, target_illuminant=str)
            line_vector_2.append(lab2)
        vector.append(line_vector_2)
    vector_list2.append(vector)

print('test_set loading complete!!!')

for t in range(len(test_pic)):
    #预测结果放入
    value_dict = {}
    for c in range(len(colors)):
        delta_e_squares = []
        for i in range(len(vector)):
            for j in range(len(vector)):
                #计算每张图片上i,j值的delta_e,使用cie2000算法
                delta_e = delta_e_cie2000(vector_list1[t][i][j], vector_list2[c][i][j])
                delta_e_squares.append(delta_e ** 2)

        #将每个像素的平方求和再开方就等于图片的E
        E_square = sum(delta_e_squares)
        E = math.sqrt(E_square)
        value_dict.update({colors[c]: E})

    print(test_pic[t], 'is completed !!! ')
    print('the minium is ....')
    flag = 0
    #对值进行排序
    with open('1.txt', 'w') as f:
        for i, j in sorted(value_dict.items(), key=lambda x: x[1]):
            f.writelines(test_pic[t]+'is completed !!!'+'\n')
            f.write('the minium is ....'+'\n')
            f.write(i+'\n')
            f.write(str(int(j))+'\n')
            print(i, j)
            flag += 1
            if i.split('.')[0] in test_pic[t]:
                right_num += 1.0
            #输出TOP3
            if flag >= 3:
                break

with open('2.txt', 'w') as f:
    f.write(str(int(right_num))+'\n')
    f.write(str(count))
    print('right_rate is :', right_num/count)