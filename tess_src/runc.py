import ctypes as c
import os
import sys

os.system('g++ -std=c++11 recognition_name.cpp -o batter -llept -ltesseract')
e = os.system('./batter')

