# Automated Guidance RC System
## Konkuk University 2018 Fall Graduation Project
### Team Members: 송종원, 강태준, 홍유리, 김태홍

### Summary
현재 국내외로 자율주행 차량은 많은 기업들이 관심을 가지고 투자하고 연구하는 분야이다. 자율주행 자동차는 총 6 단계로 나누어 지는데, 현재 상용화된 자율주행 자동차는 1,2 단계 정도이고, 여러 기업들이 3,4 단계의 자율주행 자동차를 연구하고있다. 완전한 자율주행을 하기 위해선 자동차 스스로 생각하고 판단을 내려야 하는데 그러기 위해서는 인공지능이 필수적이다.
본 논문에서는 카메라를 설치한 모형자동차를 사용하여, 사진을 수집하고, 수집한 사진들을 여러가지 딥 러닝(신경망)을 사용해서 학습을 시킨 후에, 학습한 내용대로 모형자동차가 제작한 트랙에서 별다른 조작없이 정해진 트랙을 주행하는지 확인한다.

<br></br>
<br></br>
<br></br>
## ***현재 이 Repository는 완벽한 코드 상태가 아닙니다***
 - *백업 과정에서 에러가 생겨 많은 코드들이 날아가, 최대한 갖고 있던 코드를 저장해둔 Repository입니다.*
<br></br>
<br></br>

-------------

### Handling Criteria
1. Raspberry Pi 3B
2. Arduino Uno
3. Neural Network (CNN)
4. Haar Classifier

### Priorities
1. 임베디드 차량 조립
 - [x] 아두이노 모터 연결
 - [x] 아두이노 모터 제어
 - [x] 라파 아두이노 직렬 통신
 - [x] 라파 아두이노 제어
 - [x] 라파 서버 통신
 - [x] 외부 컴퓨터로 라파 제어
 - [x] 2륜 차량에서 4륜 차량으로 변경하여 조립
 - [x] 160도 광각 카메라 모듈로 변경

2. 서버 컴퓨터 설정
 - [x] 무선 공유기 내부 Bridged 통신
 - [x] client-to-server 통신 설정

3. Neural Network 설정
 - [x] 라파로 부터 받은 사진으로 학습 데이터 구축
 - [x] 분류기 구축
 - [x] 서버에 올리기

4. 트랙
 - [x] 장애물
 - [x] 신호등
 - [x] 급커브

### Workflow Progress
- [Trello Link](https://trello.com/b/l4zTimYV/finished-ku2018fallgradproject)

### Docs
 - [KISC_추계학술대회_9D-41](https://github.com/rlaxoghd94/automated_guidance_rc/blob/master/Docs/%5BKISC_%EC%B6%94%EA%B3%84%ED%95%99%EC%88%A0%EB%8C%80%ED%9A%8C%5D9D-41.pdf)
 - [Konkuk_최종보고서](https://github.com/rlaxoghd94/automated_guidance_rc/blob/master/Docs/%5B%EC%A1%B8%EC%97%85%EC%9E%91%ED%92%88%5D_%EC%B5%9C%EC%A2%85%EB%B3%B4%EA%B3%A0%EC%84%9C.pdf)
 - [Konkuk_졸업작품전_PPT](https://github.com/rlaxoghd94/automated_guidance_rc/blob/master/Docs/%5B%EC%BB%B4%EA%B3%B5_%EC%A1%B8%EC%97%85%EC%9E%91%ED%92%88%EC%A0%84%5D%20PPT.pptx)
