import math
import rasterio
import matplotlib.pyplot as plt
import csv
import os
import cv2 as cv
from logzero import logger, logfile
import ephem
from datetime import datetime, timedelta
import numpy as np
import time

sat_data = rasterio.open('image.tif')
b, r, g = sat_data.read()

fig = plt.imshow(r)
fig.set_cmap('inferno')
plt.colorbar()
plt.show()
fig = plt.imshow(b)
plt.show()
fig = plt.imshow(g)

fig.set_cmap('gist_earth')
plt.show()


y = [255,255,0]  # Yellow
aq = [0,128,128]  # Teal (Ocean-Blue)
m = [139,69,19]  # Sadle Brown
g = [0,255,0]  # Lime green
b = [0,0,128]  # Blue navy
o = [0,0,0]  # Black
r = [255,0,0]  # Red


def Night_Detector(img, ImgHeight, ImgWidth):
    #  Function to identify a night photo.

    #  Finding the average pixel BGR value. Instead of reading each pixel value,
    #  which takes an average of 176 seconds, we are reading every four pixels
    #  for an improved efficiency, reducing analysis time to 11 seconds (16 times less).
    #  The average BGR value results more or less the same as previously obtained values.
    #  Note: OpenCV reads pixels in the format BGR.

    TotalB = 0
    TotalR = 0
    TotalG = 0

    count = 0  # Counting variable to output loading images

    #  Totalling BGR values of every pixel
    try:
        for row in range(0, ImgHeight, 4):

           # sh.set_pixels(loading[count % len(loading)])  # Output loading images
            count += 1

            for column in range(0, ImgWidth, 4):
                RGB_Value = list(img[row, column])
                TotalB = TotalB + RGB_Value[0]
                TotalG = TotalG + RGB_Value[1]
                TotalR = TotalR + RGB_Value[2]
    except Exception as e:
        logger.error(("Night_Detector function error: {}: {}").format(e.__class__.__name__, e))

    AverageB = TotalB / ((ImgWidth * ImgHeight) / 16)
    AverageG = TotalG / ((ImgWidth * ImgHeight) / 16)
    AverageR = TotalR / ((ImgWidth * ImgHeight) / 16)

    # Translating the individual BGR values to a unified greyscale value

    Average_GreyScale = (AverageB + AverageG + AverageR) / 3

    Night_Value = 40  # When experimenting, we have considered night a value below 40 in greyscale

    if Average_GreyScale < Night_Value:
        Night = True
    elif Average_GreyScale == 0:
        logger.error("Night_Detector function error: Average_GreyScale cannot be equal to zero")
    else:
        Night = False

    return(Night)

def Sea_Detector(img, ImgHeight, ImgWidth):
    TotalB = 0
    TotalR = 0
    TotalG = 0

    count = 0  # Counting variable to output loading images

    #  Totalling BGR values of every pixel
    try:
        for row in range(0, ImgHeight, 4):

           # sh.set_pixels(loading[count % len(loading)])  # Output loading images
            count += 1

            for column in range(0, ImgWidth, 4):
                RGB_Value = list(img[row, column])
                TotalB = TotalB + RGB_Value[0]
                TotalG = TotalG + RGB_Value[1]
                TotalR = TotalR + RGB_Value[2]
    except Exception as e:
        logger.error(("Night_Detector function error: {}: {}").format(e.__class__.__name__, e))
    if TotalB > TotalR:
        Sea = True
    else:
        Sea = False
    return(Sea)

img = cv.imread("zz_astropi_1_photo_216.jpg")
ImgHeight = 1944 
ImgWidth = 2592
Sea = Sea_Detector(img, ImgHeight, ImgWidth)
Night = Night_Detector(img, ImgHeight, ImgWidth)


if not Sea:
    print('No water')
else:
    print('Water')
if not Night:
    print('It is daytime')
else:
    print('It Is Nightime')


#Finissons
