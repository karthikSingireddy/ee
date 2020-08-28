from keras.models import load_model
import numpy as np
from PIL import Image

model = load_model("mnist.h5")

image = Image.open('2.png')


def predict_digit(img):
    #resize image to 28x28 pixels
    img = img.resize((28, 28))
    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    #reshaping to support our model input and normalizing
    img = img.reshape(1, 28, 28, 1)
    # img.resize((28,28))
    img = img/255.0
    #predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

digit, acc = predict_digit(image)

print(digit, acc)