import cv2
import numpy as np

def cos_sim(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

pic_dir = '/home/evga/rxy/color_test/gen_color_pic/'

colors = ['yellow.jpg', 'red.jpg', 'blue.jpg', 'green.jpg', 'black.jpg', 'white.jpg']
test_pic = ['test_yellow.jpg', 'test_deep_blue.png', 'test_green.jpg', 'test_blue.jpg', 'test_red.jpeg', 'mid_yellow.png', 'gold_yellow.jpeg', 'test_green_2.jpg']

count = len(test_pic)
right_num = 0.0

for t in test_pic:
    vector_test = np.zeros((4, 4, 4))
    value_dict = {}
    img1 = cv2.imread(pic_dir+t, cv2.IMREAD_COLOR)
    img1 = cv2.resize(img1, (400, 400), interpolation=cv2.INTER_CUBIC)


    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            b = img1[i][j][0]
            g = img1[i][j][1]
            r = img1[i][j][2]

            #print b,g,r

            b /= 64
            g /= 64
            r /= 64

            #print b,g,r

            vector_test[r][g][b] += 1
            #print vector_test

    for c in colors:
        img2 = cv2.imread(pic_dir + c, cv2.IMREAD_COLOR)
        vector = np.zeros((4, 4, 4))

        for i in range(img2.shape[0]):
            for j in range(img2.shape[1]):
                b = img2[i][j][0]
                g = img2[i][j][1]
                r = img2[i][j][2]

                # print b,g,r

                b /= 64
                g /= 64
                r /= 64

                # print b,g,r

                vector[r][g][b] += 1

        value_dict.update({c:cos_sim(vector_test.flatten(), vector.flatten())})

    print t, 'is testing .........'
    print 'the minium is ....'
    flag = 0
    for i, j in sorted(value_dict.items(), key=lambda x: x[1], reverse=True):
        print i, j
        flag += 1
        if i.split('.')[0] in t:
            right_num += 1.0
        if flag >= 3:
            break


print 'right_rate is :', right_num/count