# Android Studio 모션 인식을 이용한 영상 제어 시스템

<p aligh="center">
    <img src="https://user-images.githubusercontent.com/95459089/202703971-2c0ac543-a56e-4604-a9a4-ba9ec73fd3c6.gif">
</p>

----------
## ***Introduction*** ✔

+ Why: 레시피 영상이 요리 초보의 진도에 맞춰 재생되게 하고 싶다.
+ What: 레시피 영상이 요리 초보의 진도에 맞춰 재생되게 하는 시스템
+ How: 안드로이드 어플리케이션
<hr>

----------
### ***Summary*** 🔽 
- Project Block Diagram
<img width="864" alt="스크린샷 2022-03-30 오전 3 32 08" src="https://user-images.githubusercontent.com/88064555/160681059-60287651-0453-441f-8509-bf327c3f328f.png">

- Project 소개
    - ViCon (모션 인식을 기반한 영상 제어 시스템)
    - Youtube 영상 크롤링
    - 제스처 분류 API 구현
    - 영상 제어 API 구현
    - Youtube 영상과 안드로이드 내장 카메라 concurrent execution
    
- BACKEND
    - Mediapipe(안드로이드)를 활용한 안드로이드 카메라 입력 데이터화
    - TensorFlow Lite를 활용하기 위해 데스크탑 환경에서 학습시킨 데이터를 tflite 모델로 변환
    - Youtube API를 이용한 영상 제어 함수 커스터마이징
    - 학습된 데이터를 기반으로 클래스 분류 API
    
- FRONTEND
    - Youtube 크롤링으로 받아온 JSON 객체 이미지화
    - 분류된 클래스로 실행한 함수 시각화
    - 영상과 카메라 concurrent execution
 
----------
### ***조원 및 역할*** 🤔

+ 김진만 - 음성 인식부
+ 이정연 - 카메라/마이크, 명령어 분류부/적용부
+ 조시언 - 제스쳐 인식부
+ 최동혁 - 음성/제스쳐 통신부

## 폴더 사용 방법
---
+ **project_core**

    _모든 블록들을 병합한 프로젝트_

    모든 서브 블록들의 기능들을 병합한 프로젝트를 올리는 폴더이다. 리포지토리에 있는 각 서브 블록들을 많은데 최종적으로는 이 폴더 하나로 모든 기능이 구현된다.

+ **not_use**

    _백업용 폴더_

    현재 사용하지 않지만 혹시 모를 상황에 대비하여 백업을 위한 폴더이다. 프로젝트를 진행하며 폴더가 많아지면 헷갈리므로 안 쓰는 파일들을 여기에 저장한다.

+ **그 외 폴더**

    프로젝트를 진행하며 필요에 따라 자유롭게 사용한다.
    


