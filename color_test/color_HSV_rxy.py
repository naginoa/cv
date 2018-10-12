import math
import cv2
import numpy as np

pic_dir = '/home/evga/rxy/color_test/gen_color_pic/'

colors = ['yellow.jpg', 'red.jpg', 'blue.jpg', 'green.jpg', 'black.jpg', 'white.jpg']
test_pic = ['test_yellow.jpg', 'test_deep_blue.png', 'test_green.jpg', 'test_blue.jpg', 'test_red.jpeg', 'mid_yellow.png', 'gold_yellow.jpeg', 'test_green_2.jpg']

count = len(test_pic)
right_num = 0.0

for t in test_pic:
    value_dict = {}
    img1 = cv2.imread(pic_dir+t, cv2.IMREAD_COLOR)
    img1 = cv2.resize(img1, (400, 400), interpolation=cv2.INTER_CUBIC)

    HSV1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    aH1, aS1, aV1 = cv2.split(HSV1)
    H1 = np.array(aH1)
    S1 = np.array(aS1)
    V1 = np.array(aV1)

    for c in colors:
        # img2 = cv2.imread('/home/*/allAreaColor/result1.jpg',cv2.IMREAD_COLOR)
        img2 = cv2.imread(pic_dir+c,cv2.IMREAD_COLOR)

        HSV2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
        aH2, aS2, aV2 = cv2.split(HSV2)
        H2 = np.array(aH2)
        S2 = np.array(aS2)
        V2 = np.array(aV2)

        r3 = np.abs(H1 - H2)
        g3 = np.abs(S1 - S2)
        b3 = np.abs(V1 - V2)
        dist = np.sqrt(np.sum(np.multiply(r3, r3)) + np.sum(np.multiply(g3, g3)) + np.sum(np.multiply(b3, b3)))

        value_dict.update({c: dist})

    print t, 'is testing .........'
    print 'the minium is ....'
    flag = 0
    for i, j in sorted(value_dict.items(), key=lambda x: x[1]):
        print i, j
        flag += 1
        if i.split('.')[0] in t:
            right_num += 1.0
        if flag >= 1:
            break


print 'right_rate is :', right_num/count