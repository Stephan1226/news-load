import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from typing import List, Dict

def crawl_google_news(keyword: str, max_results: int = 3) -> List[Dict[str, str]]:
    encoded_keyword = quote(keyword)
    url = f"https://news.google.com/search?q={encoded_keyword}&hl=ko&gl=KR&ceid=KR:ko"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.select('article')

        results = []

        for i, item in enumerate(news_items):
            if i >= max_results:
                break

            title_elem = item.select_one('h3 a')
            content_elem = item.select_one('p')
            press_elem = item.select_one('[data-source]')
            time_elem = item.select_one('time')

            if title_elem:
                title = title_elem.get_text(strip=True)
                link = 'https://news.google.com' + title_elem.get('href', '').replace('./', '/')
                content = content_elem.get_text(strip=True) if content_elem else ''
                press = press_elem.get_text(strip=True) if press_elem else ''
                date = time_elem.get('datetime', '') if time_elem else ''

                results.append({
                    'title': title,
                    'content': content,
                    'press': press,
                    'date': date,
                    'link': link
                })

        return results

    except requests.RequestException as e:
        raise Exception(f"뉴스 크롤링 중 오류가 발생했습니다: {str(e)}")
    except Exception as e:
        raise Exception(f"뉴스 파싱 중 오류가 발생했습니다: {str(e)}")