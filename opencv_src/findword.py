# -*- coding: utf-8 -*-
"""
Created on Tue May  8 02:54:42 2018

@author: bok
"""
import sys
import os
import cv2
import pathlib
import shutil 

def captureWordbyPixel(path_to_input_video, pixel_value_x, pixel_value_y):

    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    
    video_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_to_input_video)
    cap = cv2.VideoCapture(video_path)
    
    video_name = os.path.split(video_path)[1]
    video_name = os.path.splitext(video_name)[0]

    path_to_output_video = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "tess_src","temp")

    # Check if camera opened successfuly
    if (cap.isOpened()== False):
        print("Error opening video stream or file")
        sys.exit(1)
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
                OUTPUT_IMAGE_PATH = os.path.join(path_to_output_video, '%d.jpg' % (cnt/10))
                print("Now %d-th images being processed..." % (cnt/10))
        
                # save image
                cv2.imwrite(OUTPUT_IMAGE_PATH, frame)
     
        # Break the loop
        else: 
            break
        
        cnt += 1
     
    # When everything done, release the video capture object
    cap.release()


    tess_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'tess_src')
    os.chdir(tess_path)
    os.system('g++ -std=c++11 recognition_name.cpp -o batter -llept -ltesseract')
    os.system('./batter')

    
    #Remove temp frame saving files
    shutil.rmtree('temp')
 
def main(filepath, x_left, x_right, y_bottom, y_top):
     pixel_x = [int(x_left), int(x_right)]
     pixel_y = [int(y_bottom), int(y_top)]
     captureWordbyPixel(filepath, pixel_x, pixel_y)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]) #main(filepath, x_left, x_right, y_bottom, y_top)
