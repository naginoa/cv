import math
import cv2
import numpy as np

pic_dir = '/home/evga/rxy/color_test/gen_color_pic/'

colors = ['yellow.jpg', 'red.jpg', 'blue.jpg', 'green.jpg', 'black.jpg', 'white.jpg']
test_pic = ['test_yellow.jpg', 'test_blue.jpg', 'test_green.jpg']

for t in test_pic:
    value_dict = {}
    img1 = cv2.imread(pic_dir+t, cv2.IMREAD_COLOR)

    HSV1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    aH1, aS1, aV1 = cv2.split(HSV1)
    H1 = np.array(aH1).flatten()
    S1 = np.array(aS1).flatten()
    V1 = np.array(aV1).flatten()

    for c in colors:
        # img2 = cv2.imread('/home/*/allAreaColor/result1.jpg',cv2.IMREAD_COLOR)
        img2 = cv2.imread(pic_dir+c,cv2.IMREAD_COLOR)

        HSV2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
        aH2, aS2, aV2 = cv2.split(HSV2)
        H2 = np.array(aH2).flatten()
        S2 = np.array(aS2).flatten()
        V2 = np.array(aV2).flatten()

        R = 100.0
        angle = 30.0
        h = R * math.cos(angle / 180 * math.pi)
        r = R * math.sin(angle / 180 * math.pi)

        sum = 0.0
        for i in range(0, len(H1)):
            x1 = r * V1[i] * S1[i] * math.cos(H1[i] / 180.0 * math.pi)
            y1 = r * V1[i] * S1[i] * math.sin(H1[i] / 180.0 * math.pi)
            z1 = h * (1 - V1[i])

            x2 = r * V2[i] * S2[i] * math.cos(H2[i] / 180.0 * math.pi)
            y2 = r * V2[i] * S2[i] * math.sin(H2[i] / 180.0 * math.pi)
            z2 = h * (1 - V2[i])

            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2

            sum = sum + dx * dx + dy * dy + dz * dz

        eucli_dean = math.sqrt(sum)
        value_dict.update({c: eucli_dean})

    print t, 'is testing .........'
    print 'the minium is ....'
    for i, j in sorted(value_dict.items(), key=lambda x: x[1]):
        print i, j