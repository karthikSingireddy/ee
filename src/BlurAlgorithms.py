import numpy as np
from copy import copy
import math


IMAGE_WIDTH = 28
IMAGE_HEIGHT = 28

def averageBlur2x2(imgp):
    img = copy(imgp)
    img = img.reshape((28, 28))

    for x in range(0, 26, 2):
        for y in range(0, 26, 2):
            top_left = img[x][y]
            top_right = img[x + 1][y]
            bottom_left = img[x][y + 1]
            bottom_right = img[x + 1][y + 1]

            average = (top_left + top_right + bottom_left + bottom_right) / 4

            img[x][y] = average
            img[x + 1][y] = average
            img[x][y + 1] = average
            img[x + 1][y + 1] = average

    return img

def averageBlur2x1Vertical(imgp):
    img = copy(imgp)
    img = img.reshape((28, 28))

    for y in range (0, 26, 2):
        for x in range(0, 27):
            top  = img[y][x]
            bottom = img[y + 1][x]

            average = (top + bottom) / 2

            img[y][x] = average
            img[y + 1][x] = average
    
    return img

def averageBlur2x1Horizontal(imgp):
    img = copy(imgp)
    img = img.reshape((28, 28))

    for y in range(0, 27):
        for x in range(0, 26, 2):
            left = img[y][x]
            right = img[y][x + 1]

            average = (left + right) / 2

            img[y][x] = average
            img[y][x + 1] = average
    return img

def keepMax2x2(imgp):
    img = copy(imgp)
    img = img.reshape((28, 28))

    for y in range(0, 26, 2):
        for x in range(0, 26, 2):
            top_left = img[y][x]
            top_right = img[y + 1][x]
            bottom_left = img[y][x + 1]
            bottom_right = img[y + 1][x + 1]

            maxVal = max(top_left, top_right, bottom_left, bottom_right)

            img[y][x] = maxVal
            img[y + 1][x] = maxVal
            img[y][x + 1] = maxVal
            img[y + 1][x + 1] = maxVal
    return img

def keepMax2x1Horizontal(imgp):
    img = copy(imgp)
    img = img.reshape((28, 28))

    for y in range(0, 27):
        for x in range(0, 26, 2):
            left = img[y][x]
            right = img[y][x + 1]

            maxVal = max(left, right)

            img[y][x] = maxVal
            img[y][x + 1] = maxVal
    return img

def keepMax2x1Vertical(imgp):
    img = copy(imgp)
    img = img.reshape((28, 28))

    for y in range (0, 26, 2):
        for x in range(0, 27):
            top  = img[y][x]
            bottom = img[y + 1][x]

            maxVal = max(top, bottom)

            img[y][x] = maxVal
            img[y + 1][x] = maxVal
    
    return img
