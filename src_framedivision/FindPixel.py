# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:28:01 2018

@author: bok
"""


import cv2

def main():
    fname = '.\\sample_pixel_image\\sample_pixel.jpg'
    
    original = cv2.imread(fname, cv2.IMREAD_COLOR)
    
    cv2.imshow('Original', original)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    main()
