import matplotlib.pyplot as plt
import numpy as np

def saveImage(image, save_to: str):
    image = np.array(image, dtype='float')
    pixels = image.reshape((28, 28))
    plt.imshow(pixels)
    plt.savefig(save_to, transparent=True, bbox_inches='tight')