from ModelSetup import loadDataset, normizeImages, buildModel, compileModel, trainModel, evaluateModel, predictImages


(train_images, train_labels, test_images, test_labels) = loadDataset()



(train_images, test_images) = normizeImages(train_images, test_images)


# model = buildModel()
# compileModel(model)

# trainModel(model, train_images, train_labels)

# evaluateModel(model, test_images, test_labels)


# predictions = predictImages(model, test_images)
# print(predictions)

img = test_images[1]
img = img.reshape((28, 28))


# print("Values", img)
# print("Size", img.size)

for x in range(0, 27):
    for y in range(0, 27):
        # print(str(img[x][y]) + "\t", end='')
        if img[x][y] == -0.5:
            print("  ", end='')
        else:
            print("+ ", end='')
    print()
    
