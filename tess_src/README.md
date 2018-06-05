# How to Run recognition_name.cpp
<br>
Written by TaekLim Kim
<br><br><br><br>

## Setting OpenCV & Tessearct
* * *
<br>
You need to set OpenCV and Tesseract to run this source code. <br>
It was tested on the Linux Ubuntu 16.04. Below websites are the references for building these SW. <br>

<br>
> How to build OpenCV: <http://webnautes.tistory.com/1030?category=704653> <br><br>

Also, you can refer the README.md written by Jbok.<br>

> How to build tesseract: <http://jybaek.tistory.com/620> <br>
<br>

### Issues while compiling and building OpenCV
<br>
There are some building error while we install OpenCV. <br><br>

The main problem of this issue is that conflict between OpenCV and Tesseract.<br>
Tesseract is based on C++11 version, while OpenCV is not support this version.<br>
So, when we build OpenCV after installed Tesseract, there are dependency between those APIs.<br><br>

I gave an Issue to OpenCV github Repository, about Building error between Tesseract API.<br><br>

> Issue on OpenCV Github: <https://github.com/opencv/opencv_contrib/issues/1636> <br>

<!--
This part will be img and link of Issue on Github
-->

<br>
I found some solution about this problem, and I uploaded on to OpenCV Issue. <br>
There are ```CMakeFilelist.txt```, and we can change the C++ version. <br>
To adapt c++11 version onto OpenCV build process, you should write a line of code <br><br>

```C++
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
```
<br>

And then, you can continue to building OpenCV process.<br>
There will be no more problem about the confilict between c++11 Tesseract & OpenCV
<br><br>


## Compiling
* * *
### Compile

It should be compiled with c++11 because the tesseract only support the c++11 (not OpenCV)
```
g++ -std=c++11 recognition_name.cpp -o batter -llept -ltesseract
```

After that, you can find the executable file <br><br>

### Run

```./batter``` will run this code. <br>

If you using the virtual machine or if you get some error message that is ```: cannot connect to X server```, <br>
you should run with ```xvfb-run -a ./batter``` 

<br>
Then, you can get the result from it. <br><br>
<img src="/uploads/83823b78674b42af0606eeb79590a1cc/batter_result.png" width="50%" height="50%">
<br><br>
If there are other problem about compiling and installing process, let me know for emailing me. <br><br>

limkim4233@ajou.ac.kr <br>

<br>



