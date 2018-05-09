# KBO: Knocking Baseball by Opensource <br><br>

## About
* * *
해당 프로젝트는 openCV와 Tesseract 오픈소스를 사용하여 야구 생중계 화면에서 문자를 인식한 후 실시간으로 경기 데이터를 사용자에게 전달하는 웹 서비스를 제공한다.<br><br>

## Overview
* * *
현재 인기 스포츠인 야구는 다른 스포츠와 달리 통계와 데이터 분석 능력의 발전으로 과학적이고 세부적인 접근이 가능해졌다. <br>
시청자들은 중계시스템의 향상으로 다양한 수치들을 볼 수 있게 되었지만, 더 세부적이고 입맛에 맞는 데이터를 실시간으로 받아보기 힘든 경우가 많다. <br>
따라서 아래와 같은 과정을 거쳐 시청자가 세부적인 데이터를 실시간으로 받아볼 수 있는 시스템을 제공하는 것이 KBO의 목적이다. <br>
1) openCV 와 Tesseract 오픈소스를 이용하여 생중계 화면에 대해 문자 인식을 하여 현재 경기 상황에 대한 실시간 정보를 얻는다. <br>
2) 기존에 가지고 있는 DB를 통하여 현 경기 상황에 대해 시청자가 바로 알지 못한 통계적 수치를 분석한다. <br>
3) 이렇게 얻어진 수치를 다시 웹을 통해 시청자한테 전달함으로써 시청자가 세부적인 데이터에 빠르게 접근할 수 있게 만든다. <br><br>

## How it works
* * *
### 영상에서의 문자 인식
<br>

<img src="/uploads/d7547ebb50622191507138899ff22aaa/rdm1.png" width="50%" height="50%">
<br>
동작 예시 영상 <https://www.youtube.com/watch?v=Yv6IkGRQIWk>

<br>
<img src="/uploads/16c5828976a803bae7df281ff2b9d95f/rdm2.png" width="50%" height="50%">
<br>
선수의 이름을 인식하여 DB로부터 정보를 가져온다 <br>
<br>
<img src="/uploads/cc933d39cee107f9f68cd62f4f539467/rdm3.png" width="60%" height="60%">
<br>
각종 stat을 확인할 수 있는 웹서비스에서 scraping하여 데이터를 추출하고 경기 실시간으로 타자와 투수의 맞대결 전적, 예측을 사용자에게 전달함 <br>
ex) STATIZ <http://www.statiz.co.kr/main.php>

<br><br>

## Tools

- C++
- Python (django)
- node.js
- javascript
- html

<br><br>

## Licenses
* * *
### openCV <br>

```
By downloading, copying, installing or using the software you agree to this license.
If you do not agree to this license, do not download, install,
copy or use the software.


                          License Agreement
               For Open Source Computer Vision Library
                       (3-clause BSD License)

Copyright (C) 2000-2018, Intel Corporation, all rights reserved.
Copyright (C) 2009-2011, Willow Garage Inc., all rights reserved.
Copyright (C) 2009-2016, NVIDIA Corporation, all rights reserved.
Copyright (C) 2010-2013, Advanced Micro Devices, Inc., all rights reserved.
Copyright (C) 2015-2016, OpenCV Foundation, all rights reserved.
Copyright (C) 2015-2016, Itseez Inc., all rights reserved.
Third party copyrights are property of their respective owners.

```

### tesseract
```
The code in this repository is licensed under the Apache License, Version 2.0 (the "License")
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
<br>
This project is licensed under these open source licenses <br><br><br>

## Members <br>
* * *
권민지 김필선 김택림 이주복
<br><br>
