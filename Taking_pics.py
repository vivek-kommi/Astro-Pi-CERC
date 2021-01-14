import datetime
from time import sleep
import PIL as pil
from time import sleep
from picamera import PiCamera
from pathlib import Path
import os
import sys


start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
count = 0
dir_path = '/home/pi/Documents/Astropi/Camera'
try:
    while(now_time<start_time + datetime.timedelta(hours = 3)):
        now_time = datetime.datetime.now()
        #camera = PiCamera()
        #camera.resolution = (1296,972)
        #camera.start_preview()
        # Camera warm-up time
        sleep(5)
        file_name = "astro_pi_images_sai_test" + str(count) + ".csv"
        #camera.capture(dir_path/file_name)
        count += 1
        sleep(5)
        print(count)
        full_file_path = dir_path + '/' + file_name
        print(full_file_path)
                                                           
    else:
        print('image capture is done exitting now')
        sys.exit(0)        # 0 means that the program has successfully exitted
except:   
    print('Failure!!!Act needed')
