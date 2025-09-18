from urllib.parse import quote
from typing import List, Dict
import feedparser
import re

def crawl_google_news(keyword: str, max_results: int = 3) -> List[Dict[str, str]]:
    encoded_keyword = quote(keyword)
    rss_url = f"https://news.google.com/rss/search?q={encoded_keyword}&hl=ko&gl=KR&ceid=KR:ko"

    try:
        feed = feedparser.parse(rss_url)

        if not feed.entries:
            return []

        results = []

        for i, entry in enumerate(feed.entries):
            if i >= max_results:
                break

            title = entry.title if hasattr(entry, 'title') else ''
            link = entry.link if hasattr(entry, 'link') else ''
            raw_content = entry.summary if hasattr(entry, 'summary') else ''
            date = entry.published if hasattr(entry, 'published') else ''

            # HTML 태그 제거
            content = re.sub(r'<[^>]+>', '', raw_content)

            # 언론사명은 제목에서 추출 (보통 마지막에 - 언론사명 형태)
            press = ''
            if ' - ' in title:
                press = title.split(' - ')[-1]

            results.append({
                'title': title,
                'content': content,
                'press': press,
                'date': date,
                'link': link
            })

        return results

    except Exception as e:
        raise Exception(f"뉴스 크롤링 중 오류가 발생했습니다: {str(e)}")