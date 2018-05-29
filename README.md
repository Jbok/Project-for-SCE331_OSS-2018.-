# **KBO: Knocking Baseball by Opensource**

<br>

## **Contents**
* * *
- About
- Overview
- How it works
- Any improvements
- Open Issues
- Installation
- How to Execute
- API Languages
- Licenses
- Members

<br><br>

## **About**
* * *
해당 프로젝트의 궁극적인 목적은  **OpenCV와 Tesseract 오픈소스를 사용하여 야구 생중계 화면에서 문자를 인식**한 후 실시간으로 경기 데이터를 사용자에게 전달하는 서비스를 제공하는 것이다.<br><br>

이를 위해 **영상에서의 문자 인식 API**를 제작한다. 
<br><br><br>


## **Overview**
* * *
현재 인기 스포츠인 야구는 다른 스포츠와 달리 통계와 데이터 분석 능력의 발전으로 과학적이고 세부적인 접근이 가능해졌다. <br>
시청자들은 중계시스템의 향상으로 다양한 수치들을 볼 수 있게 되었지만, 더 세부적이고 입맛에 맞는 데이터를 실시간으로 받아보기 힘든 경우가 많다. <br><br>
따라서 아래와 같은 과정을 거쳐 시청자가 세부적인 데이터를 실시간으로 받아볼 수 있는 시스템을 제공하는 것이 해당 프로젝트의 목적이다. <br><br>

1. openCV 와 Tesseract 오픈소스를 이용하여 생중계 화면에 대해 문자 인식을 하여 현재 경기 상황에 대한 실시간 정보를 얻는다. <br>
2. 기존에 가지고 있는 DB를 통하여 현 경기 상황에 대해 시청자가 바로 알 수 없는 데이터를 제공해준다. 

<br><br>
## **How it works**
* * *

우리가 원하는 것은 생중계 영상에서 실시간으로 타자의 이름을 얻어오는 것이었다. 야구 생중계의 경우 타자의 이름은 대부분 영상의 같은 위치에서 제공된다. <br>
따라서 우리는 해당 영상의 일정 위치를 찾아 이를 인식하는 방향으로 프로젝트를 진행하였다. <br><br>
위에서 언급했듯이 OpenCV와 Tesseract 오픈소스를 사용하였는데 그 이유로는 다음과 같았다. <br><br>

1. OpenCV로 영상과 이미지 프로세싱이 동시에 가능하다.<br>
2. Tesseract의 경우 영어 뿐만 아니라 한글 또한 인식 능력이 뛰어나다.

<br><br>

OpenCV를 사용하여 영상을 프레임 별로 나눔과 동시에 우리가 원하는 타자의 이름 부분만 이미지로 저장하였다. 그리고 저장된 이름 이미지를 Tesseract로 인식하여 해당 인식된 결과를 출력해 주었다.

<br><br>
<img src="/uploads/d7547ebb50622191507138899ff22aaa/rdm1.png" width="50%" height="50%">
(▲ 동작 예시 영상 : <https://www.youtube.com/watch?v=Yv6IkGRQIWk>)
<br><br><br>
<img src="/uploads/16c5828976a803bae7df281ff2b9d95f/rdm2.png" width="50%" height="50%">
(▲ 야구 생중계 화면에서 선수의 이름을 인식하는 모습 - 예상)
<br><br><br>

생중계 영상을 이미지 프레임으로 나누게 되면 위의 그림과 같은 이미지들이 생기게 된다. 
이 때 추가적으로 해당 타자의 이름이 있는 위치를 OpenCV를 통해 설정해주면 아래와 같이 타자의 이름만 이미지로 저장이 된다. <br><br>

<br>
하지만 야구 중계 채널마다 선수의 [이름 위치가 다른 경우][1]가 존재한다. <br> 
따라서 **이 프로젝트에서는 하나의 API로 제작**하여 이 소스코드를 사용하는 SW개발자들이 원하는 좌표값을 Parameter로 지정하여 원하는 위치만을 이미지로 저장할 수 있게 제공할 것이다.<br>

[1]: http://git.ajou.ac.kr/open-source-2018-spring/kbo/issues/3 "야구 중계채널별 선수 이름의 위치"
<br>

OpenCV를 이용하여 영상을 프레임과 원하는 위치만을 이미지로 저장하는 소스코드는 **VIS.py** 이며 동작 예시는 다른 MarkDown에 기록해 놓았다. <br><br>

또한  이렇게 원하는 위치만 이미지로 저장된 것을 가지고 해당 이미지에서 우리가 원하는 타자의 이름을 추출하려 하였다. 
이를 위해 Tesseract를 사용하였고 해당 소스코드는 **recognition_name.cpp** 에 있다. <br><br>

Tesseract는 수많은 C++ API를 제공하는데 이는 보통 하나의 이미지만을 처리하는 API가 대부분이다. <br>
우리는 생중계가 진행됨과 동시에 많은 이미지들을 계속해서 인식해야 하기 때문에 이미지들을 계속해서 불러오고 이들을 인식하여야 했다. <br>
따라서 각 이미지에서 인식된 결과들 중에 가장 많이 나타난, 즉 정확도가 높은 결과를 뽑아 내는 작업을 진행하였고 현재 한 타석 정도의 영상에서 타자의 이름을 인식할 수 있게 되었다.<br><br>

<!-- Image -->

<br><br>
## **Any Improvements**
* * *

현재 프로젝트의 목적은 오픈소스들의 장점을 살려 하나의 API를 제작하는 것이다. <br>
Tesseract와 OpenCV 모두 오픈소스이기 때문에 더 나은 영상처리와 문자인식을 보여줄 것이고 그에 맞게 우리가 개발할 API 또한 더 향상될 가능성이 존재한다.
<br><br>

<br>
## **Open Issues**
* * *

해당 프로젝트에 제안된 Issue는 아니지만 개발 과정에서 더 개선되어야 할 점들이 존재하였다. <br><br>

1. 한 타석 뿐만 아니라 더 여러 타자들이 나오는 경우에서의 이름 인식
2. 해당 영상을 이미지로 나눌 때에 관련된 저장공간 Overhead

<br><br>

위의 Issue들은 앞으로 더 살펴보아야 할 과제이다.

<br><br><br>
## **Installation**
* * *
OpenCV, Tesseract 두 오픈소스 라이브러리를 사용하여 제작되었기 때문에 해당 라이브러리에 대한 설치가 필요하다. <br>
<br>
각 라이브러리 설치에 대한 링크는 아래를 참조<br><br>

> OpenCV: 
> <br><br>
> Tessearact: 


<br><br><br>
## **How to Execute**
* * *

API에 대한 개발 완료 시 작성

<br><br><br>
## **API Language**
* * *
- C++ (Tesseract)
- Python (OpenCV)

<br><br><br>


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

* * *
<br><br><br>


## **Members**
* * *
**권민지 김필선 김택림 이주복**
<br><br><br>


<br><br><br>
<!---
#### 2. 선수의 이름을 인식하여 DB로부터 정보를 가져온다.
<br><br>
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


<br><br><br>
## **Need to improvement**
* * *
해당 프로젝트의 핵심 기술은 **Tesseract를 이용한 문자 인식**이다. <br><br>
> ### **_Tesseract_**
> <br> <img src="/uploads/533c5f7685a87f512e19dc7542aeba21/캡처.JPG" width="10.5%" height="10.5%"> <br><br>
> 기존의 Tesseract 오픈소스는 사진 속의 문자를 인식하는 것에 초점이 맞춰져 있다. <br>
> KBO(해당 프로젝트)는 이 오픈소스를 개선하여 사진에서뿐만 아니라 **영상에서도 문자 인식이 가능하도록 하는 것**을 목표로 한다. <br>
> (☞[기존 Tesseract 실행 예시][2]) <br><br>
> ### **_openCV_**
> <br> <img src="/uploads/482434afae428a2ff80e526dd07a9ef2/OpenCV_Logo_with_text.png" width="10%" height="10%"> <br><br>
> - frame division
> - pixel value성
> - RGB value <br>
> (☞[openCV 실행 예시][3])
[2]: http://git.ajou.ac.kr/open-source-2018-spring/kbo/blob/master/Tesseract_example.md
[3]: http://git.ajou.ac.kr/open-source-2018-spring/kbo/blob/master/openCV_example.md
* * *
-->
<br><br><br>