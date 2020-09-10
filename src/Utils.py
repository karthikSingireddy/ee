import matplotlib.pyplot as plt
import numpy as np

def saveImage(image, save_to: str):
    image = np.array(image, dtype='float')
    pixels = image.reshape((28, 28))
    fig = plt.imshow(pixels)
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig(save_to, transparent=True, bbox_inches='tight')

def numpyArrayToString(array):
    val = ""
    for num in array:
        val += str(num)
        val+=","

    val = val[:-1]
    return val

def stringToNumpyArr(string):
    vals = string.split(',')
    for x in range(0, len(vals)):
        vals[x] = float(vals[x])
    arr = np.array(vals)
    return arr