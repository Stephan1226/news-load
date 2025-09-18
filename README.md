# 네이버 뉴스 크롤링 FastAPI 서비스

키워드를 입력하면 네이버 뉴스를 크롤링해서 상위 3개의 뉴스를 반환하는 FastAPI 백엔드 서비스입니다.

## 빠른 시작

### 1. 자동 설치 및 실행 (권장)

```bash
# 설치
./setup.sh

# 실행
./run.sh
```

### 2. 수동 설치 및 실행

```bash
# 1. 가상환경 생성
python3 -m venv venv

# 2. 가상환경 활성화
source venv/bin/activate

# 3. 패키지 설치
pip install --upgrade pip
pip install -r requirements.txt

# 4. 서비스 실행
python main.py
```

## API 사용법

### 1. 서비스 상태 확인
```
GET /
```

### 2. 뉴스 검색
```
POST /news
Content-Type: application/json

{
    "keyword": "검색할 키워드"
}
```

### 3. 헬스 체크
```
GET /health
```

## API 문서

서비스 실행 후 http://localhost:8000/docs 에서 Swagger UI로 API 문서를 확인할 수 있습니다.

## 응답 예시

```json
{
    "keyword": "인공지능",
    "news": [
        {
            "title": "뉴스 제목",
            "content": "뉴스 내용",
            "press": "언론사",
            "date": "날짜",
            "link": "뉴스 링크"
        }
    ]
}
```