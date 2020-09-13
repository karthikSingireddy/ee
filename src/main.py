# from ModelSetup import loadDataset, normizeImages
# # , buildModel, compileModel, trainModel, evaluateModel, predictImages
import ModelSetup
import math
from BlurAlgorithms import averageBlur2x2, averageBlur2x1Horizontal, averageBlur2x1Vertical, keepMax2x2, keepMax2x1Horizontal, keepMax2x1Vertical
from Utils import saveImage, npArrayToString
import mysqlManager
import sys

(train_images, train_labels, test_images, test_labels) = ModelSetup.loadDataset()



(train_images, test_images) = ModelSetup.normizeImages(train_images, test_images)


model = ModelSetup.buildModel()
ModelSetup.compileModel(model)

ModelSetup.trainModel(model, train_images, train_labels)

ModelSetup.evaluateModel(model, test_images, test_labels)


# predictions = ModelSetup.predictImages(model, test_images[:10])

# print(predictions)


sql = mysqlManager.MySqlWrapper()



# for img in test_images[:2]:
#     prediction = ModelSetup.predictImage(model, img)
#     print(prediction)

original = 0
avg2x2 = 0
avg2x1_v = 0
avg2x1_h = 0
max2x2 = 0
max2x1_v = 0
max2x1_h = 0

numImgs = 10000

for n in range(0, numImgs):
    images = sql.getImage(image_index=n, limit=10)
    for img in images: 
        (prediction, certainty) = ModelSetup.predictImage(model, img.img)
        if img.blur_type == 'original' or img.blur_type == 'max_2x2':
            print(f"Actual Value: {img.value}\tImage:index: {img.image_index}\tBlur type: {img.blur_type}\t\t\t\t\tPredicted Value: {prediction}\tCertainty: {certainty}\t Match:{img.value == prediction}")
        elif img.blur_type == "average_blur_2x2" or img.blur_type == "max_2x1_vertical" or img.blur_type == "max_2x1_horizontal":
            print(f"Actual Value: {img.value}\tImage:index: {img.image_index}\tBlur type: {img.blur_type}\t\tPredicted Value: {prediction}\tCertainty: {certainty}\t Match:{img.value == prediction}")
        else:
            print(f"Actual Value: {img.value}\tImage:index: {img.image_index}\tBlur type: {img.blur_type}\tPredicted Value: {prediction}\tCertainty: {certainty}\t Match:{img.value == prediction}")
        

        if img.blur_type == 'original' and img.value == prediction:
            original += 1
        elif img.blur_type == 'average_blur_2x2' and img.value == prediction:
            avg2x2 += 1
        elif img.blur_type == 'average_blur_2x1_ver' and img.value == prediction:
            avg2x1_v += 1
        elif img.blur_type == 'average_blur_2x1_hor' and img.value == prediction:
            avg2x1_h += 1
        elif img.blur_type == 'max_2x2' and img.value == prediction:
            max2x2 += 1
        elif img.blur_type == 'max_2x1_vertical' and img.value == prediction:
            max2x1_v += 1
        elif img.blur_type == 'max_2x1_horizontal' and img.value == prediction:
            max2x1_h += 1
    print()
    print(f"Image {n} completed", file=sys.stderr)
    
    


print(f"Images     tested: {numImgs}")
print(f"Original   Correct: {original}\t Accuracy: {float(original)/numImgs}")
print(f"Average2x2 Correct: {avg2x2}\t Accuracy: {float(avg2x2)/numImgs}")
print(f"Avg2x1Ver  Correct: {avg2x1_v}\t Accuracy: {float(avg2x1_v)/numImgs}")
print(f"Avg2x1Hor  Correct: {avg2x1_h}\t Accuracy: {float(avg2x1_h)/numImgs}")
print(f"Max2x2     Correct: {max2x2}\t Accuracy: {float(max2x2)/numImgs}")
print(f"Max2x1Ver  Correct: {max2x1_v}\t Accuracy: {float(max2x1_v)/numImgs}")
print(f"Max2x1hor  Correct: {max2x1_h}\t Accuracy: {float(max2x1_h)/numImgs}")
    


# img = sql.getImage(image_index=8)

# # for i in img:
# #     saveImage(i.img, f"img/testfail/{i.blur_type}")






# img = img.reshape((28, 28))




# sqlConn = mysqlManager.MySqlWrapper()1







