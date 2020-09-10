from ModelSetup import loadDataset, normizeImages, buildModel, compileModel, trainModel, evaluateModel, predictImages
import math
from BlurAlgorithms import averageBlur2x2, averageBlur2x1Horizontal, averageBlur2x1Vertical, keepMax2x2, keepMax2x1Horizontal, keepMax2x1Vertical
from Utils import saveImage

(train_images, train_labels, test_images, test_labels) = loadDataset()



(train_images, test_images) = normizeImages(train_images, test_images)


# model = buildModel()
# compileModel(model)

# trainModel(model, train_images, train_labels)

# evaluateModel(model, test_images, test_labels)


# predictions = predictImages(model, test_images)
# print(predictions)

img = test_images[2]
# img = img.reshape((28, 28))


# print("Values", img)
# print("Size", img.size)

# for x in range(0, 27):
#     for y in range(0, 27):
#         num = (img[x][y] + 0.5) * 100
#         num = math.trunc(num)
#         print(str(num) + " ", end='')
#     print()
    
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

# saveImage(img, "img/original.png")

# imgb = averageBlur2x2(img)
# saveImage(imgb, 'img/averageBlur2x2.png')

# imgb = averageBlur2x1Horizontal(img)
# saveImage(imgb, "img/averageBlur2x1Horizontal.png")

# imgb = averageBlur2x1Vertical(img)
# saveImage(imgb, 'img/averageBlur2x1Vertical.png')

# imgb = keepMax2x2(img)
# saveImage(imgb, 'img/keepMax2x2.png')

# imgb = keepMax2x1Vertical(img)
# saveImage(imgb, 'img/keepMax2x1Vertical.png')

# imgb = keepMax2x1Horizontal(img)
# saveImage(imgb, 'img/keepMax2x1Horizontal.png')
num = 0
for img in test_images[:3]:


    saveImage(img, f"img/big/{str(num)}original.png")

    imgb = averageBlur2x2(img)
    saveImage(imgb, f'img/big/{str(num)}averageBlur2x2.png')

    imgb = averageBlur2x1Horizontal(img)
    saveImage(imgb, f"img/big/{str(num)}averageBlur2x1Horizontal.png")

    imgb = averageBlur2x1Vertical(img)
    saveImage(imgb, f'img/big/{str(num)}averageBlur2x1Vertical.png')

    imgb = keepMax2x2(img)
    saveImage(imgb, f'img/big/{str(num)}keepMax2x2.png')

    imgb = keepMax2x1Vertical(img)
    saveImage(imgb, f'img/big/{str(num)}keepMax2x1Vertical.png')

    imgb = keepMax2x1Horizontal(img)
    saveImage(imgb, f'img/big/{str(num)}keepMax2x1Horizontal.png')

    num += 1
