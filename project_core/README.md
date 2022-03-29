# 프로젝트 핵심 기능 구현 소스 파일

## 전체 블록 다이어그램
---

<img width="864" alt="스크린샷 2022-03-30 오전 3 32 08" src="https://user-images.githubusercontent.com/88064555/160681059-60287651-0453-441f-8509-bf327c3f328f.png">

---

## 사용 방법
---
capstone_socket.py를 본인 PC의 IP를 입력하고 port 번호를 임의로 설정해준 후 실행시킨다.

"기다리는 중..."이라는 메시지가 뜨면

안드로이드에서 yasea-master -> MainActivity 코드 -> NetworkThread Class -> socket IP를 서버 측 IP로 수정한다. -> APP 실행 -> 서버 측에서 1,2,3,4 각 번호를 입력함에 따라 동영상이 제어된다.

## 해당 폴더가 구현한 블록(yasea-master)
---
### * 마이크 / 카메라
<img width="358" alt="sub_block_diagram1" src="https://user-images.githubusercontent.com/88064555/160377176-8b004f97-9f63-4129-af13-934831f55142.png">

### * 명령어 분류부 / 적용부
<img width="876" alt="sub_block_diagram2" src="https://user-images.githubusercontent.com/88064555/160377279-c0d02ecd-ca50-4eab-a744-56573286c3b8.png">

---
## 테스트 파이썬 서버(capstone_socket.py)

서버 측에서 전송하는 데이터로 안드로이드 동영상이 정상적으로 제어 되는지 확인하기 위한 목적이다.

---



