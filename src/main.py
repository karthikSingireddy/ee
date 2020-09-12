from ModelSetup import loadDataset, normizeImages
# , buildModel, compileModel, trainModel, evaluateModel, predictImages
import math
from BlurAlgorithms import averageBlur2x2, averageBlur2x1Horizontal, averageBlur2x1Vertical, keepMax2x2, keepMax2x1Horizontal, keepMax2x1Vertical
from Utils import saveImage, npArrayToString
import mysqlManager

(train_images, train_labels, test_images, test_labels) = loadDataset()



(train_images, test_images) = normizeImages(train_images, test_images)


# model = buildModel()
# compileModel(model)

# trainModel(model, train_images, train_labels)

# evaluateModel(model, test_images, test_labels)


# predictions = predictImages(model, test_images)
# print(predictions)

# img = img.reshape((28, 28))


# print("Values", img)
# print("Size", img.size)

# for x in range(0, 27):
#     for y in range(0, 27):
#         num = (img[x][y] + 0.5) * 100
#         num = math.trunc(num)
#         print(str(num) + " ", end='')
#     print()
    

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
# num = 0
# for img in test_images[:1]:


#     saveImage(img, f"img/big/{str(num)}original.png")

#     imgb = averageBlur2x2(img)
#     saveImage(imgb, f'img/big/{str(num)}averageBlur2x2.png')

#     imgb = averageBlur2x1Horizontal(img)
#     saveImage(imgb, f"img/big/{str(num)}averageBlur2x1Horizontal.png")

#     imgb = averageBlur2x1Vertical(img)
#     saveImage(imgb, f'img/big/{str(num)}averageBlur2x1Vertical.png')

#     imgb = keepMax2x2(img)
#     saveImage(imgb, f'img/big/{str(num)}keepMax2x2.png')

#     imgb = keepMax2x1Vertical(img)
#     saveImage(imgb, f'img/big/{str(num)}keepMax2x1Vertical.png')

#     imgb = keepMax2x1Horizontal(img)
#     saveImage(imgb, f'img/big/{str(num)}keepMax2x1Horizontal.png')

#     num += 1



# print(test_images[0])
# print('\n\n\n\n')

# string = npArrayToString(test_images[0])
# print(string, string.__len__())


sqlConn = mysqlManager.MySqlWrapper()






# for img in test_images[:5]:
# for n in range(1000, 10000):
#     img = test_images[n]

#     imgString = npArrayToString(img)
#     # print(imgString, end='\n\n\n')
#     sqlConn.insertImage(image_index=n, blur_type='original',img=imgString, value=int(test_labels[n]))

#     imgb = averageBlur2x2(img)
#     imgString = npArrayToString(imgb)
#     # print(imgString, end='\n\n\n')
#     sqlConn.insertImage(image_index=n, blur_type='average_blur_2x2',img=imgString, value=int(test_labels[n]))

#     imgb = averageBlur2x1Horizontal(img)
#     imgString = npArrayToString(imgb)
#     # print(imgString, end='\n\n\n')
#     sqlConn.insertImage(image_index=n, blur_type='average_blur_2x1_hor', img=imgString, value=int(test_labels[n]))

#     imgb = averageBlur2x1Vertical(img)
#     imgString = npArrayToString(imgb)
#     # print(imgString, end='\n\n\n')
#     sqlConn.insertImage(image_index=n, blur_type='average_blur_2x1_ver', img=imgString, value=int(test_labels[n]))

#     imgb = keepMax2x2(img)
#     imgString = npArrayToString(imgb)
#     # print(imgString, end='\n\n\n')
#     sqlConn.insertImage(image_index=n, blur_type='max_2x2', img=imgString, value=int(test_labels[n]))

#     imgb = keepMax2x1Vertical(img)
#     imgString = npArrayToString(imgb)
#     # print(imgString, end='\n\n\n')
#     sqlConn.insertImage(image_index=n, blur_type='max_2x1_vertical', img=imgString, value=int(test_labels[n]))

#     imgb = keepMax2x1Horizontal(img)
#     imgString = npArrayToString(imgb)
#     # print(imgString, end='\n\n\n')
#     sqlConn.insertImage(image_index=n, blur_type='max_2x1_horizontal', img=imgString, value=int(test_labels[n]))

#     print(f"Image index {n} completed")
