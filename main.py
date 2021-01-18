''' This code is made by CERC. What this code does is that it gets
pictures for a certain time and then it makes a csv file and adds all
the names of the pictures in each line .
:)
'''

# Import all libraries
#import rasterio
#import matplotlib.pyplot as plt
import os
import datetime
from time import sleep
from picamera import PiCamera
import cv2 as cv
# initialise all variables incuding the start time, now time, camera and the count variable
y = [255, 255, 0]  # Yellow
aq = [0, 128, 128]  # Teal (Ocean-Blue)
m = [139, 69, 19]  # Sadle Brown
g = [0, 255, 0]  # Lime green
b = [0, 0, 128]  # Blue navy
o = [0, 0, 0]  # Black
r = [255, 0, 0]  # Red


path = os.getcwd()
path1 = path + '/Photos'
os.mkdir(path1)
start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
count1 = 0
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

    count1 = 0  # Counting variable to output loading images

    #  Totalling BGR values of every pixel

    for row in range(0, ImgHeight, 4):
            # sh.set_pixels(loading[count % len(loading)])  # Output loading images
        count1 += 1

        for column in range(0, ImgWidth, 4):
            RGB_Value = list(img[row, column])
            TotalB = TotalB + RGB_Value[0]
            TotalG = TotalG + RGB_Value[1]
            TotalR = TotalR + RGB_Value[2]

    AverageB = TotalB / ((ImgWidth * ImgHeight) / 16)
    AverageG = TotalG / ((ImgWidth * ImgHeight) / 16)
    AverageR = TotalR / ((ImgWidth * ImgHeight) / 16)

    # Translating the individual BGR values to a unified greyscale value

    Average_GreyScale = (AverageB + AverageG + AverageR) / 3

    Night_Value = 40  # When experimenting, we have considered night a value below 40 in greyscale

    if Average_GreyScale < Night_Value:
        Night = True
    elif Average_GreyScale == 0:
        raise Exception("Night_Detector function error: Average_GreyScale cannot be equal to zero")
    else:
        Night = False

    return (Night)


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
        raise Exception("Failed!!!")
    if TotalB > TotalR:
        Sea = True
    else:
        Sea = False
    return (Sea)

count = 0
camera = PiCamera()
camera.resolution = (1300, 768)
# Creates csv file and sets it under the variable: CSVFile
CSVFile = open('astro.csv', 'w')
CSVFile.write("FILE NAME:            NIGHT VALUE:            SEA VALUE:            Date:")
# when the time is less than our time we specified:
while (now_time < (start_time + datetime.timedelta(hours=0, minutes=30))):
    # reinitialsing variables
    ImgHeight = 720
    ImgWidth = 1280
    now_time = datetime.datetime.now()
    # Creating file name using the count variable
    file_name = "astro_pi_image" + str(count) + ".jpg"
    #sat_data = rasterio.open(file_name)
    #b, r, g = sat_data.read()
    #fig = plt.imshow(g)
    #fig.set_cmap('gist_earth')
    #plt.savefig(file_name)
    # camera gets picture and saves it under the path as file_name
    camera.capture(path1 + "/" + file_name)
    # the count variable increases
    count += 1
    img = cv.imread(path1 + "/" + file_name)
        # the time interval between image captures
    sleep(10)
    var_1 = Night_Detector(img, ImgHeight, ImgWidth)
    var_2 = Sea_Detector(img, ImgHeight, ImgWidth)
        # writing the file name and then adding a new line
    CSVFile.write(file_name + " , The night value: " + str(var_1) + " , The sea value: " + str(var_2)+ " , " + str(start_time) + '\n')

    # closes the file
CSVFile.close()
