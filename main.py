from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from news_crawler import crawl_naver_news

app = FastAPI(
    title="네이버 뉴스 크롤링 API",
    description="키워드를 입력하면 네이버 뉴스 상위 3개를 크롤링합니다.",
    version="1.0.0"
)

class NewsRequest(BaseModel):
    keyword: str

class NewsItem(BaseModel):
    title: str
    content: str
    press: str
    date: str
    link: str

class NewsResponse(BaseModel):
    keyword: str
    news: List[NewsItem]

@app.get("/")
async def root():
    return {"message": "네이버 뉴스 크롤링 API입니다. /docs에서 API 문서를 확인하세요."}

@app.post("/news", response_model=NewsResponse)
async def get_news(request: NewsRequest):
    if not request.keyword or not request.keyword.strip():
        raise HTTPException(status_code=400, detail="키워드를 입력해주세요.")

    try:
        news_data = crawl_naver_news(request.keyword.strip(), max_results=3)

        if not news_data:
            raise HTTPException(status_code=404, detail="검색 결과가 없습니다.")

        news_items = [NewsItem(**item) for item in news_data]

        return NewsResponse(
            keyword=request.keyword.strip(),
            news=news_items
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)