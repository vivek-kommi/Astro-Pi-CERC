import csv
import datetime
from time import sleep
from picamera import PiCamera
import os
import sys

start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
list = []
count = 0
camera = PiCamera()
CSVFile=open('astro.csv', 'w')
while(now_time<(start_time + datetime.timedelta(hours = 0,minutes = 1))):
	        now_time = datetime.datetime.now()
		file_name = "astro_pi_image" + str(count)  + ".jpg"
		camera.capture("/home/pi/CERC-ASTROPI/Photos/" + file_name)
    	        count += 1
	        sleep(10)
	       # list.update(file_name)
	        CSVFile.write(file_name + '\n')
#CSVFile=open('astro.csv', 'w')
#CSVFile.write(list)
CSVFile.close()
