import numpy as np
import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

def loadDataset():
    train_images = mnist.train_images()
    train_labels = mnist.train_labels()
    
    test_images = mnist.test_images()
    test_labels = mnist.test_labels()

    return (train_images, train_labels, test_images, test_labels)

def normizeImages(train_images, test_images):
    train_images = (train_images/255) - 0.5
    test_images = (test_images/255) - 0.5

    train_images = train_images.reshape((-1, 784))
    test_images = test_images.reshape((-1, 784))

    return (train_images, test_images)

def buildModel():
    model = Sequential()
    model.add( Dense(64, activation='relu', input_dim=784))
    model.add( Dense(64, activation='relu'))
    model.add( Dense(10, activation='softmax'))
    return model

def compileModel(model):
    model.compile(
        optimizer='adam',
        loss = 'categorical_crossentropy',
        metrics = ['accuracy']
    )

def trainModel(model, train_images, train_labels):
    model.fit(
        train_images,
        to_categorical(train_labels),
        epochs = 5,
        batch_size=32
    )

def evaluateModel(model, test_images, test_labels):
    model.evaluate(
        test_images,
        to_categorical(test_labels)
    )

def predictImages(model, test_images):
    predictions = model.predict(test_images[:100])

    return np.argmax(predictions, axis=1)