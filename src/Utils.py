import matplotlib.pyplot as plt
import numpy as np
import math

def saveImage(image, save_to: str):
    image = np.array(image, dtype='float')
    pixels = image.reshape((28, 28))
    fig = plt.imshow(pixels)
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig(save_to, transparent=True, bbox_inches='tight')

def npArrayToString(arr: np.array) -> str:
    s: str = ''
    for num in arr:
        s+=str(num)
        s+=','
    return s[0:len(s)-1]

def printImgAscii(img):
    img = img.reshape((28, 28))
    for x in range(0, 27):
        for y in range(0, 27):
            num = (img[x][y] + 0.5) * 100
            num = math.trunc(num)

            strNum = str(num)
            if(num < 10):
                strNum = "0" + strNum
            if num == 100:
                strNum = "++"
            if num == 0:
                strNum = "__"

            print(strNum + " ", end='')
        print()
    print('\n\n\n')
