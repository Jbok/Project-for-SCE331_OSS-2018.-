# How to Install OpenCCV
<br><br>
***
* * *
## Linux 
<br>
**0. Upgrade existing package**
<br>
```
$ sudo apt-get update
$ sudo apt-get upgrade
```
<br><br>
**1. Remove Opencv 2.4 Version**
<br><br>
Check whether OpenCV 2.4 Version is already installed or not
```
$ pkg-config --modversion opencv
```
<br>
If you see that message, Opencv is not installed. Go to step2
```
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing 'opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opoencv' found
```
<br>
If you see that message, Opencv is already installed.
```
2.4.9.1
```
Then you should remove version 2.4.9.1.
```
$ sudo apt-get purge libopencv* python-opencv
$ sudo apt-get autoremove
```

**2. Install OpenCV package**
<br>
```
$ sudo apt-get install build-essential cmake
$ sudo apt-get install pkg-config
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev
$ sudo apt-get install libv4l-dev v4l-utils
$ sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
$ sudo apt-get install libqt4-dev 
$ sudo apt-get install mesa-utils libgl1-mesa-dri libqt4-opengl-dev 
$ sudo apt-get install libatlas-base-dev gfortran libeigen3-dev
$ sudo apt-get install python2.7-dev python3-dev python-numpy python3-numpy
```
<br><br>
**3. Install and build OpenCV**
<br>
*download Opencv*
```
$ mkdir opencv
$ cd opencv
$ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.2.0.zip
$ unzip opencv.zip
$ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip
$ unzip opencv_contrib.zip
```

*build opencv*
```
$ cd opencv-3.2.0/
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=OFF -D WITH_IPP=OFF -D WITH_1394=OFF -D BUILD_WITH_DEBUG_INFO=OFF -D BUILD_DOCS=OFF -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=OFF -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D ENABLE_NEON=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules -D WITH_V4L=ON -D WITH_FFMPEG=ON -D WITH_XINE=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D PYTHON_INCLUDE_DIR=/usr/include/python2.7 -D PYTHON_INCLUDE_DIR2=/usr/include/x86_64-linux-gnu/python2.7 -D PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so ../
$ make -j
$ sudo make install
```

*Identify Installation*
```
$ pkg-config --modversion opencv
$ pkg-config --libs --cflags opencv

```
* * *
***
