# from ModelSetup import loadDataset, normizeImages
# # , buildModel, compileModel, trainModel, evaluateModel, predictImages
import ModelSetup
import math
from BlurAlgorithms import averageBlur2x2, averageBlur2x1Horizontal, averageBlur2x1Vertical, keepMax2x2, keepMax2x1Horizontal, keepMax2x1Vertical
from Utils import saveImage, npArrayToString
import mysqlManager

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


for n in range(0, 100):
    images = sql.getImage(image_index=n, limit=10)
    for img in images: 
        (prediction, certainty) = ModelSetup.predictImage(model, img.img)
        if img.blur_type == 'original' or img.blur_type == 'max_2x2':
            print(f"Actual Value: {img.value}\tImage:index: {img.image_index}\tBlur type: {img.blur_type}\t\t\t\t\tPredicted Value: {prediction}\tCertainty: {certainty}\t Match:{img.value == prediction}")
        elif img.blur_type == "average_blur_2x2" or img.blur_type == "max_2x1_vertical" or img.blur_type == "max_2x1_horizontal":
            print(f"Actual Value: {img.value}\tImage:index: {img.image_index}\tBlur type: {img.blur_type}\t\tPredicted Value: {prediction}\tCertainty: {certainty}\t Match:{img.value == prediction}")
        else:
            print(f"Actual Value: {img.value}\tImage:index: {img.image_index}\tBlur type: {img.blur_type}\tPredicted Value: {prediction}\tCertainty: {certainty}\t Match:{img.value == prediction}")
    print('\n\n')


# img = sql.getImage(image_index=8)

# # for i in img:
# #     saveImage(i.img, f"img/testfail/{i.blur_type}")






# img = img.reshape((28, 28))




# sqlConn = mysqlManager.MySqlWrapper()1







