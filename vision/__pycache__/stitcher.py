
import cv2
import os
import mediapipe as mp
import time
import math
import numpy as np

source= 'pic'

if source!='vid':
    path= os.path.abspath('ims')
    images = os.listdir('ims')
    collector=[]
    for image in images:
        image = path +'/'+image
        collector.append(cv2.imread(image))
    streams = collector

else: 
    streams = cv2.VideoCapture(['192.168.1.10', '192.168.1.11','192.168.1.12'])

stitcher = cv2.Stitcher.create()
fourcc = cv2.VideoWriter_fourcc(*'h264')
(status, out) = stitcher.stitch(streams)

if (status==cv2.Stitcher_OK):
    # send(out)
    cv2.imshow('test',out)
    cv2.waitKey(0)
       
else:
    print("CV2 stitching error")
    print(status)
cv2.destroyAllWindows()


