opencv library download link for each OS

https://opencv.org/releases.html

#How to Install OpenCCV

## Linux 

### 0. Upgrade existing package
```
$ sudo apt-get update
$ sudo apt-get upgrade
```

### 1. Remove Opencv 2.4 Version

Check whether OpenCV 2.4 Version is already installed or not
```
$ pkg-config --modversion opencv
```

If you see that message, Opencv is not installed. Go to step2
```
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing 'opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opoencv' found
```

If you see that message, Opencv is already installed.
```
2.4.9.1
```
Then you should remove version 2.4.9.1.
```
$ sudo apt-get purge libopencv* python-opencv
$ sudo apt-get autoremove
```

### 2. Install OpenCV package
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

