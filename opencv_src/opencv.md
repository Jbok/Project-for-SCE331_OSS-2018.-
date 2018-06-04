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

### 2. 

