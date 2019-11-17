# 데벨업 퀘스트 세 번째

## 프로젝트명 미정

데벨업 퀘스트 세 번째를 위한 레포지토리입니다.


[github 링크](https://github.com/YMGYM/develup_quest3)

[goorm 프로젝트 주소](https://goor.me/AWVdz)

[개발 일지 Notion 페이지](https://www.notion.so/628d4600e7744eba8af1434bb340018e?v=4d985c298110496da98c5c9b69bab472)
## 주제

'소속 단체를 위한 서비스'라는 주제에 맞게, 대학생을 위한 종강일 계산기를 만드려고 합니다.
이 종강일 계산기 프로젝트는 다음과 같은 기능을 갖추고 있습니다.

- 회원가입을 통해 개인별 종강일 계산
- 전역일 계산기(곰신톡 등)와 같이 실시간으로 종강일을 계산해서 표시
- 종강일 말고도 학교 행사등 이벤트 등록 후 남은 기간을 실시간으로 표시


모티브가 된 전역일 계산기(곰신톡)

![https://lh3.googleusercontent.com/y0m4kUwMSB9R8wlrWkqaOHL_PAtMMP3urENzq5aV_sPA9G1zcwvWh6MwUaEls8TkYeam=w1870-h936-rw](https://lh3.googleusercontent.com/y0m4kUwMSB9R8wlrWkqaOHL_PAtMMP3urENzq5aV_sPA9G1zcwvWh6MwUaEls8TkYeam=w1870-h936-rw)

## 소스파일 설명

이 프로젝트는 Django를 통해 제작하였습니다.

### account

`account` app에서는 유저 등록을 위한 회원가입, 로그인 페이지를 등록합니다.


### 계산기

종강일 계산기를 구현합니다.
User 모델에서 유저 정보를 불러온 상태(로그인 상태) 에서만 접속 가능합니다.

### 종강일, 이벤트 등록

종강일과 이벤트를 등록합니다.
User모델과 1:N으로 연결되어 구현됩니다.
