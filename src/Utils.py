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