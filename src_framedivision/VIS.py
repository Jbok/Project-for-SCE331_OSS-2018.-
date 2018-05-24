# -*- coding: utf-8 -*-
"""
Created on Tue May  8 02:54:42 2018

@author: bok
"""

import os
import cv2
from matplotlib import pyplot as plt
 
###############################################################################
# parameters defined by user
PATH_TO_INPUT_VIDEO_PATH = '.\\sample_video\\'
VIDEO_NAME = 'sample_2018'
VIDEO_EXTENSION = '.mp4'
PATH_TO_OUTPUT_IMAGES_DIR = '.\\sample_frame_image\\'
###############################################################################
 
def main():
    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture(PATH_TO_INPUT_VIDEO_PATH + VIDEO_NAME + VIDEO_EXTENSION)
     
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
     
    # Read until video is completed
    cnt = 0
    
    #make folder to save frame if there is no exisiting folder about video file
    if not os.path.isdir(PATH_TO_OUTPUT_IMAGES_DIR + VIDEO_NAME):
       os.mkdir(PATH_TO_OUTPUT_IMAGES_DIR + VIDEO_NAME)
        
    
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        
        if ret == True:
            ##COLOR_BGR2RGB
            ##frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            ##COLOR_BGR2GRAY
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            frame = frame[630:685, 455:580]

            # Capture only 1/10 frame
            if (int(cap.get(1)) % 10 == 0):
                OUTPUT_IMAGE_PATH = os.path.join(PATH_TO_OUTPUT_IMAGES_DIR + VIDEO_NAME +'\\', 'image_%09d.jpg' % (cnt/10))
                print("Now %d-th images being processed..." % (cnt/10))
        
                # save image
                cv2.imwrite(OUTPUT_IMAGE_PATH, frame)
     
        # Break the loop
        else: 
            break
        
        cnt += 1
     
    # When everything done, release the video capture object
    cap.release()
 
 
if __name__ == '__main__':
    main()