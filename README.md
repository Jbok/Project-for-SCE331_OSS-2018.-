# **KBO: Knocking Baseball by Opensource**

<br><br><br>

## **★ _Contents_ (목차)★**
* * *
- About
- Overview
- Need to improvement (개선점)
- How it works (작동원리)
- How to use (사용법) example 포함 예정
- Tools
- Licenses
- Members

* * *

<br><br><br>


## **About**
* * *
해당 프로젝트는 **openCV와 Tesseract 오픈소스를 사용하여 야구 생중계 화면에서 문자를 인식**한 후 실시간으로 경기 데이터를 사용자에게 전달하는 웹 서비스를 제공한다.
* * *
<br><br>


## **Overview**
* * *
현재 인기 스포츠인 야구는 다른 스포츠와 달리 통계와 데이터 분석 능력의 발전으로 과학적이고 세부적인 접근이 가능해졌다. <br>
시청자들은 중계시스템의 향상으로 다양한 수치들을 볼 수 있게 되었지만, 더 세부적이고 입맛에 맞는 데이터를 실시간으로 받아보기 힘든 경우가 많다. <br>
따라서 아래와 같은 과정을 거쳐 시청자가 세부적인 데이터를 실시간으로 받아볼 수 있는 시스템을 제공하는 것이 **KBO(해당 프로젝트)의 목적**이다. <br><br>
1) openCV 와 Tesseract 오픈소스를 이용하여 생중계 화면에 대해 문자 인식을 하여 현재 경기 상황에 대한 실시간 정보를 얻는다. <br>
2) 기존에 가지고 있는 DB를 통하여 현 경기 상황에 대해 시청자가 바로 알지 못한 통계적 수치를 분석한다. <br>
3) 이렇게 얻어진 수치를 다시 웹을 통해 시청자한테 전달함으로써 시청자가 세부적인 데이터에 빠르게 접근할 수 있게 만든다.
* * *
<br><br>


## **Need to improvement**
* * *
해당 프로젝트의 핵심 기술은 **Tesseract를 이용한 문자 인식**이다. <br><br>
> ### **_Tesseract_**
> <br> <img src="/uploads/533c5f7685a87f512e19dc7542aeba21/캡처.JPG" width="10.5%" height="10.5%"> <br><br>
> 기존의 Tesseract 오픈소스는 사진 속의 문자를 인식하는 것에 초점이 맞춰져 있다. <br>
> KBO(해당 프로젝트)는 이 오픈소스를 개선하여 사진에서뿐만 아니라 **영상에서도 문자 인식이 가능하도록 하는 것**을 목표로 한다. <br><br>
> ### **_openCV_**
> <br> <img src="/uploads/482434afae428a2ff80e526dd07a9ef2/OpenCV_Logo_with_text.png" width="10%" height="10%"> <br><br>
> - image processing <br>
> - frame division

* * *
<br><br>


## **How it works**
* * *
#### 1. 영상에서 문자를 인식한다.
<br>
<img src="/uploads/d7547ebb50622191507138899ff22aaa/rdm1.png" width="50%" height="50%">
(▲ 동작 예시 영상 : <https://www.youtube.com/watch?v=Yv6IkGRQIWk>)
<br><br><br>
<img src="/uploads/16c5828976a803bae7df281ff2b9d95f/rdm2.png" width="50%" height="50%">
(▲ 야구 생중계 화면에서 선수의 이름을 인식하는 모습 - 예상)
<br><br><br>
#### 2. 선수의 이름을 인식하여 DB로부터 정보를 가져온다.
<br><br><br>
<img src="/uploads/cc933d39cee107f9f68cd62f4f539467/rdm3.png" width="60%" height="60%">
(▲ 2017 시즌, '한화 이글스' 팀의 '김태균' 선수의 對 롯데 자이언츠 투수 상대전적)
<br><br><br>
각종 통계자료를 확인할 수 있는 웹 서비스에서 crawling하여 데이터를 추출하고 경기 실시간으로 타자와 투수의 맞대결 전적, 예측을 사용자에게 전달한다. <br>
> 각종 통계자료를 확인할 수 있는 **참고사이트 목록**은 아래와 같다. <br>
> 1. [STATIZ](http://www.statiz.co.kr/main.php "KBO 리그의 각종 야구기록에 세이버메트릭스를 전문적으로 도입한 최초의 통계 사이트 중 하나")
> 2. [KBO](https://www.koreabaseball.com/ "KBO 공식 홈페이지")
> 3. [KBReport](http://www.kbreport.com/main "한국 프로야구 통계 사이트")
> 4. [네이버 기록실](http://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo&year=2018 "가장 기본적인 정보를 확인가능한 네이버 포탈 내의 야구 통계자료 사이트")
> 5. [야구친구](http://www.yachin.co.kr/ "과거에 했던 경기 또는 오늘 경기에서의 선수들 기록, 실시간 승리 확률 그래프 등을 확인 가능")

<br>
#### 3. DB로부터 얻은 수치를 (그대로 or 가공해서) 웹을 통해 전달한다.

* * *
<br><br>


## **How to use**
* * *
<br><br>
* * *


## **Tools**
* * *
- C++
- Python (django)
- node.js
- javascript
- html

* * *
<br><br>


## **Licenses**
* * *
#### openCV

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

#### Tesseract
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
This project is licensed under these open source licenses.

<br><br>


## **Members**
* * *
권민지 김필선 김택림 이주복
<br><br>