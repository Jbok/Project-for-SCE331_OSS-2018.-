# How to Run Sample Codes

## Setting OpenCV & Tessearct

<br>
You need to set OpenCV and Tesseract to run this source code. <br>
It was tested on the Linux Ubuntu 16.04. Below websites are the references for building these SW. <br>

How to build OpenCV: <http://webnautes.tistory.com/1030?category=704653> <br>
How to build tesseract: <http://jybaek.tistory.com/620> <br>
<br>

## Compiling

### Compile

It should be compiled with c++11 because the tesseract only support the c++11 (not OpenCV)
```
g++ -std=c++11 sample.cpp -o opencv-tesseract `pkg-config --cflags --libs opencv tesseract`
```
<br>
After that, you can find the executable file name ```opencv-tesseract``` <br>

### Run

```./opencv-tesseract``` will run this sample code. <br>

If you using the virtual machine or if you get some error message that is ```: cannot connect to X server```, <br>
you should run with ```xvfb-run -a ./opencv-tesseract``` 
<br><br>
Then, you can get the result from it


<br>



