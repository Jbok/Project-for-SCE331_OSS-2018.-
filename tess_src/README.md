# How to Run recognition_name.cpp
<br>
Written by TaekLim Kim
<br><br><br><br>

## Setting OpenCV & Tessearct
* * *

### OpenCV
<br>
You need to set OpenCV and Tesseract to run this source code. <br>
It was tested on the Linux Ubuntu 16.04. Below websites are the references for building these SW. <br>
There are reference about how to build OpenCV on JBok's Markdown file, so I only talk about the Tesseract. <br>
Also, you can refer below sites for building OpenCV. <br>
<br>
> JBok's Reference for OpenCV: <http://git.ajou.ac.kr/open-source-2018-spring/kbo/blob/master/opencv_src/opencv.md>
<br>
> How to build OpenCV: <http://webnautes.tistory.com/1030?category=704653>

<br>
### Tesseract
<br>

**1. Install the Packages**
<br>
```
$ sudo apt-get install autoconf automake libtool 
$ sudo apt-get install autoconf-archive 
$ sudo apt-get install pkg-config 
$ sudo apt-get install libpng12-dev 
$ sudo apt-get install libjpeg8-dev 
$ sudo apt-get install libtiff5-dev 
$ sudo apt-get install zlib1g-dev
$ sudo apt-get install libleptonica-dev
```
<br>
**2. Download the Github source and Compile it**
```
$ git clone --depth 1 https://github.com/tesseract-ocr/tesseract.git 
$ cd tesseract $ ./autogen.sh 
$ ./configure --enable-debug 
$ LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make 
$ sudo make install $ sudo ldconfig
```
<br>
**3. Download Datafile(Korean, English..)**

There are github wiki on tesseract-ocr and you can download the Language Data files. <br>
For testing the English and Korean recognition, you should download two files. <br>

> https://github.com/tesseract-ocr/tesseract/wiki/Data-Files

<br>
**4. Test the Tesseract in Command Line**
```
tesseract image.png outputbase -l kor
```
Your image should be in the same directory as your current position. <br>
While you enter that command line, you can checkout the recognition of the image letter.

<br><br>
### Issues while Compiling and Building OpenCV
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
<br><br><br><br>


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

limkim4233@ajou.ac.kr
<br><br>

### Reference site

> <http://jybaek.tistory.com/620>
<br>



