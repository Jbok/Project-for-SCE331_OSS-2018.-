# How to Use findword.py
<br><br>
## findword.py
* * *
### Constitution of findword.py
It is module to find the word in video.<br>
There is function captreWordbyPixel (path_to_input_video, pixel_value_x, pixel_value_y).<br>
```
def catpureWordbyPixel(path_to_input_video, pixel_value_x, pixel_value_y)
    //path_to_input_video is the path of the video file relative to findword.py
    //pixel_value_x is the array [x_left, x_right]
    //pixel_value_y is the array [y_bottom, y_top]
    
def main(filepath, x_left, x_right, y_bottom, y_top):
     pixel_x = [int(x_left), int(x_right)]
     pixel_y = [int(y_bottom), int(y_top)]
     captureWordbyPixel(filepath, pixel_x, pixel_y)
```
<br>
### Run
I want to find sample_video/sample_2018.mp4's batter's name.<br>
sample_2018.mp4's batter name's pixel value is [275, 340] [480, 485].<br>

> If you want to know the pixel value of the desired part, Refer to this document.
> http://git.ajou.ac.kr/open-source-2018-spring/kbo/blob/master/opencv_src/openCV_example.md
<br>

Commands form Linux are as follows
```
python3 findword.py sample_video/sample_2018.mp4 275 340 460 485
```




<br><br>

## Setting OpenCV & Tesseract
* * *
You need to set OpenCV and Tesseract to use this module.<br>
Because this module import OpenCV to capture the video's frame.<br>
And run recognition_name.cpp to analysis frame's word.<br>
recognition_name.cpp file use tesseract, so we need to build OpenCV and Tesseract before use findword.py module<br>
<br>
**1. OpenCV**
<br>
> JBok's Reference for OpenCV: <http://git.ajou.ac.kr/open-source-2018-spring/kbo/blob/master/opencv_src/opencv.md>
<br>
> How to build OpenCV: <http://webnautes.tistory.com/1030?category=704653>
<br><br>

**2. Tesseract**
<br>
> TaekLim Kim's Reference for recongition_name.cpp & tesseract: <http://git.ajou.ac.kr/open-source-2018-spring/kbo/blob/master/tess_src/README.md>

