import cv2
import numpy as np

pic_dir = '/home/evga/rxy/color_test/gen_color_pic/'

colors = ['yellow.jpg', 'red.jpg', 'blue.jpg', 'green.jpg', 'black.jpg', 'white.jpg']
test_pic = ['test_yellow.jpg', 'test_deep_blue.png', 'test_green.jpg', 'test_blue.jpg', 'test_red.jpeg', 'mid_yellow.png', 'gold_yellow.jpeg', 'test_green_2.jpg']

count = len(test_pic)
right_num = 0.0

for t in test_pic:
    value_dict = {}
    for c in colors:
        img_test = cv2.imread(pic_dir + t)
        img_real = cv2.imread(pic_dir + c)
        img_test = cv2.resize(img_test, (400, 400), interpolation=cv2.INTER_CUBIC)
        #dist = np.sqrt(np.sum(np.square(img_test - img_real)))

        '''
        r3 = (r1 - r2) / 256
        g3 = (g1 - g2) / 256
        b3 = (b1 - b2) / 256
        diff = sqrt(r3 * r3 + g3 * g3 + b3 * b3)
        '''

        r3 = (img_test[:, :, 0] - img_real[:, :, 0])
        g3 = (img_test[:, :, 1] - img_real[:, :, 1])
        b3 = (img_test[:, :, 2] - img_real[:, :, 2])
        dist = np.sqrt(np.sum(np.multiply(r3, r3))+np.sum(np.multiply(g3, g3))+np.sum(np.multiply(b3, b3)))

        value_dict.update({c:np.mean(dist)})


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