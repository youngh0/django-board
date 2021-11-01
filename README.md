# django-board

# 게시판 만들면서 장고 연습하기

## 사용 기술 : django
## CSS : Boot-Strap
<br>

# 회원
### url: localhost:8000/accounts/
## 기능
1. 회원가입(이메일 형식, 이메일 인증은 X)
2. 로그인(입력값에 따라 이메일이 유효하지 않은지 비밀번호가 유효하지 않은지 알려주기)
3. 닉네임 변경
4. 회원탈퇴
5. 로그아웃
<br>

# 게시판
### url : localhost:8000/board/
## 기능
    1. 게시판 생성
    2. 게시글 CRUD
    3. 댓글 CRUD
    4. 로그인 여부에 따라 권한 삭제 및 수정 권한 부여
    5. 게시글 목록에서 해당 게시글에 달린 댓글 개수 보여주기
<br>

# 화면 캡쳐

## 홈 화면

### 로그인 안한 상태

![홈화면](https://user-images.githubusercontent.com/62167801/139658048-19774234-4f8c-49cd-ba1e-586e9776d0b8.png)


### 로그인 한 홈화면 - 상단에 닉네임과, logout버튼

![로그인한 홈 화면](https://user-images.githubusercontent.com/62167801/139658085-0b1971a8-4b61-48c1-b350-7f1a2de200c9.png)

## 게시판

### 게시판 목록화면

- 자신이 작성한 글은 삭제 및 수정가능한 버튼이 나옴
- 해당 글에 달린 댓글 수 보여주기

![게시글 목록 화면](https://user-images.githubusercontent.com/62167801/139658099-cc5a1e96-bbf4-4ad5-a105-75eba931f041.png)

### 게시글 안으로 들어가면 댓글 내용 확인

![스크린샷 2021-11-01 오후 7 30 17](https://user-images.githubusercontent.com/62167801/139658257-3020b952-64b5-411a-b877-bf70ee229d27.png)

### 댓글이 없는 경우

![스크린샷 2021-11-01 오후 7 31 00](https://user-images.githubusercontent.com/62167801/139658344-d0045ba5-3899-450d-bc36-a40c94929bd8.png)

## 회원

### 프로필

![스크린샷 2021-11-01 오후 7 31 36](https://user-images.githubusercontent.com/62167801/139658417-114ea3b2-57be-4388-a889-c9f56ae022d3.png)

### 닉네임 변경

![스크린샷 2021-11-01 오후 7 32 00](https://user-images.githubusercontent.com/62167801/139658461-ce6f2730-3765-4d2d-ac1e-c262594fe1a1.png)

### 비밀번호 변경

![스크린샷 2021-11-01 오후 7 32 12](https://user-images.githubusercontent.com/62167801/139658485-98576cb6-b373-440d-be9f-7da53a4ecfa4.png)
### 잘못된 이메일로 로그인 시도

![등록된 이메일이 아닌경우](https://user-images.githubusercontent.com/62167801/139658518-593e675d-d3a2-411b-9465-ba62817d0b8c.png)

### 잘못된 비밀번호로 로그인 시도
![잘못된 비밀번호](https://user-images.githubusercontent.com/62167801/139658524-c4eca911-f728-410d-b2fb-c7f42231673e.png)

