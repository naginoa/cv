from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_objects import XYZColor, sRGBColor,LabColor
from colormath.color_conversions import convert_color
import numpy as np
import math
import cv2


pic_dir = 'C:\\Users\\renxinyuan\\Desktop\\color_test\\gen_color_pic\\'

colors = ['yellow.jpg', 'red.jpg', 'blue.jpg', 'green.jpg', 'black.jpg', 'white.jpg']
test_pic = ['test_yellow.jpg', 'test_deep_blue.png', 'test_green.jpg', 'test_blue.jpg', 'test_red.jpeg', 'mid_yellow.png', 'gold_yellow.jpeg', 'test_green_2.jpg']

count = len(test_pic)
right_num = 0.0

for t in test_pic:
    vector_test = []
    value_dict = {}
    img1 = cv2.imread(pic_dir+t, cv2.IMREAD_COLOR)
    img1 = cv2.resize(img1, (400, 400), interpolation=cv2.INTER_CUBIC)
    for i in range(img1.shape[0]):
        line_vector = []
        for j in range(img1.shape[1]):
            rgb1 = sRGBColor(img1[i][j][0], img1[i][j][1], img1[i][j][2])
            xyz1 = convert_color(rgb1, XYZColor)
            lab1 = convert_color(xyz1, LabColor, target_illuminant=str)
            line_vector.append(lab1)
        vector_test.append(line_vector)
    #print(len(vector_test[0]))

    for c in colors:
        vector = []
        delta_e_squares = []
        img2 = cv2.imread(pic_dir+c,cv2.IMREAD_COLOR)
        flag = 0
        for i in range(img2.shape[0]):
            line_vector_2 = []
            for j in range(img2.shape[1]):
                rgb2 = sRGBColor(img2[i][j][0], img2[i][j][1], img2[i][j][2])
                xyz2 = convert_color(rgb2, XYZColor)
                lab2 = convert_color(xyz2, LabColor, target_illuminant=str)
                line_vector_2.append(lab2)
            vector.append(line_vector_2)

        for i in range(len(vector)):
            for j in range(len(vector)):
                delta_e = delta_e_cie2000(vector_test[i][j], vector[i][j])
                delta_e_squares.append(delta_e ** 2)
        print(c, 'is calculating..........')
        E_square = sum(delta_e_squares)
        E = math.sqrt(E_square)
        value_dict.update({c: E})

    print(t, 'is completed !!! ')
    print('the minium is ....')
    flag = 0
    for i, j in sorted(value_dict.items(), key=lambda x: x[1]):
        print(i, j)
        flag += 1
        if i.split('.')[0] in t:
            right_num += 1.0
        if flag >= 3:
            break


print('right_rate is :', right_num/count)

'''
# Reference color.
color1 = LabColor(lab_l=0.9, lab_a=16.3, lab_b=-2.22)
# Color to be compared to the reference.
color2 = LabColor(lab_l=0.7, lab_a=14.2, lab_b=-1.80)
# This is your delta E value as a float.
delta_e = delta_e_cie2000(color1, color2)
print(delta_e)
'''