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


y = [255,255,0]  # Yellow
aq = [0,128,128]  # Teal (Ocean-Blue)
m = [139,69,19]  # Sadle Brown
g = [0,255,0]  # Lime green
b = [0,0,128]  # Blue navy
o = [0,0,0]  # Black
r = [255,0,0]  # Red


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
