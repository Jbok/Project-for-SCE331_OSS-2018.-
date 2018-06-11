# -*- coding: utf-8 -*-
"""
Created on Tue May  8 02:54:42 2018

@author: bok
"""

import os
import cv2
import pathlib

###############################################################################
# parameters defined by user
# PATH_TO_INPUT_VIDEO_PATH = 'sample_video'
# VIDEO_NAME = 'sample_2018.mp4'
# PATH_TO_OUTPUT_IMAGES_DIR = 'sample_frame_image'

###############################################################################
 
def captureWordbyPixel(path_to_input_video, pixel_value_x, pixel_value_y):

    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    video_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_to_input_video)
    cap = cv2.VideoCapture(video_path)
    
    video_name = os.path.split(video_path)[1]
    video_name = os.path.splitext(video_name)[0]
    print(video_name)

    path_to_output_video = os.path.join(os.path.dirname(os.path.realpath(__file__)), "sample_frame_image", video_name)

    # Check if camera opened successfuly
    if (cap.isOpened()== False):
        print("Error opening video stream or file")
     
    # Read until video is completed
    cnt = 0
    


    #make folder to save frame if there is no exisiting folder about video file
    if not os.path.isdir(path_to_output_video):
       os.mkdir(path_to_output_video)
        
    
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        
        if ret == True:
            ##COLOR_BGR2RGB
            ##frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            ##COLOR_BGR2GRAY
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            
            ##Calculate original height and width of video
            height_origin, width_origin = frame.shape[:2]

            ##Resize frame to enhance recognition rate
            frame = cv2.resize(frame,(2000, 1000))
            
            ##Re calculate height and width of resize frame
            height, width = frame.shape[:2]
            
            ##Calculate namespace pixel value by the ratio
            x_left = int(width * (pixel_value_x[0]/width_origin))
            x_right = int(width * (pixel_value_x[1]/width_origin))
            y_top = int(height * (pixel_value_y[0]/height_origin))
            y_bottom = int(height * (pixel_value_y[1]/height_origin))
            
            ##Cropping image frame[height, width]
            frame = frame[y_top:y_bottom, x_left:x_right]
          
            # Capture only 1/10 frame
            if (int(cap.get(1)) % 10 == 0):
                OUTPUT_IMAGE_PATH = os.path.join(path_to_output_video, 'image_%09d.jpg' % (cnt/10))
                print("Now %d-th images being processed..." % (cnt/10))
        
                # save image
                cv2.imwrite(OUTPUT_IMAGE_PATH, frame)
     
        # Break the loop
        else: 
            break
        
        cnt += 1
     
    # When everything done, release the video capture object
    cap.release()
 
 
def main():
    pixel_x = [275, 340]
    pixel_y = [460, 485]
    captureWordbyPixel("sample_video\\sample_2018.mp4", pixel_x, pixel_y)

if __name__ == '__main__':
    main()
