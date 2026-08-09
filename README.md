# 나홀로 링크 메모장

Flask + MongoDB로 만든 간단한 메모장 웹 애플리케이션입니다.
메모를 작성하고, 좋아요를 누르고, 수정/삭제할 수 있습니다.

## 주요 기능

- 메모 작성 (제목 + 내용)
- 메모 목록 조회 (좋아요 순 정렬)
- 좋아요 기능
- 메모 수정 / 삭제

## 기술 스택

- **Backend**: Python, Flask
- **Database**: MongoDB (pymongo)
- **Frontend**: HTML, Bootstrap 5, jQuery

## 실행 방법

### 1. 사전 준비

- Python 3.x
- MongoDB가 로컬(localhost:27017)에서 실행 중이어야 합니다.

### 2. 설치

```bash
git clone https://github.com/<your-username>/jg.git
cd jg
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### 3. 실행

```bash
python app.py
```

브라우저에서 `http://localhost:5000` 접속

## API

| Method | URL            | 설명                       |
| ------ | -------------- | -------------------------- |
| GET    | `/`            | 메인 페이지                |
| GET    | `/memo`        | 메모 전체 조회 (좋아요 순) |
| POST   | `/memo`        | 메모 작성                  |
| POST   | `/memo/like`   | 좋아요 +1                  |
| POST   | `/memo/update` | 메모 수정                  |
| POST   | `/memo/delete` | 메모 삭제                  |
