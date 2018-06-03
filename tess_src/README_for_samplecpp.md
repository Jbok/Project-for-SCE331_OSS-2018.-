# How to Run recognition_name.cpp
<br><br>
Written by TaekLim Kim
<br><br><br>

## Setting OpenCV & Tessearct

<br>
You need to set OpenCV and Tesseract to run this source code. <br>
It was tested on the Linux Ubuntu 16.04. Below websites are the references for building these SW. <br>

OpenCV

How to build OpenCV: <http://webnautes.tistory.com/1030?category=704653> <br>
How to build tesseract: <http://jybaek.tistory.com/620> <br>
<br><br>

### Issues while compiling and building OpenCV

There are some building error while we install OpenCV. <br><br>

The main problem of this issue is that conflict between OpenCV and Tesseract.<br>
Tesseract is based on C++11 version, while OpenCV is not support this version.<br>
So, when we build OpenCV after installed Tesseract, there are dependency between those APIs.<br><br>

I gave an Issue to OpenCV github Repository, about Building error between Tesseract API.<br><br>

Issue on OpenCV Github: <https://github.com/opencv/opencv_contrib/issues/1636> <br>

<!--
This part will be img and link of Issue on Github
-->

<br>
I found some solution about this problem, and I uploaded on to OpenCV Issue. <br>
There are ```CMakeFilelist.txt```, and we can change the C++ version. <br>

<br><br>


## Compiling

### Compile

It should be compiled with c++11 because the tesseract only support the c++11 (not OpenCV)
```
g++ -std=c++11 sample.cpp -o opencv-tesseract `pkg-config --cflags --libs opencv tesseract`
```
<br>
After that, you can find the executable file name `````` <br>

### Run

```./opencv-tesseract``` will run this sample code. <br>

If you using the virtual machine or if you get some error message that is ```: cannot connect to X server```, <br>
you should run with ```xvfb-run -a ./opencv-tesseract``` 
<br><br>
Then, you can get the result from it


<br>



