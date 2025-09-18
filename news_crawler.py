import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from typing import List, Dict

def crawl_naver_news(keyword: str, max_results: int = 3) -> List[Dict[str, str]]:
    encoded_keyword = quote(keyword)
    url = f"https://search.naver.com/search.naver?where=news&query={encoded_keyword}&sort=1"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.select('.news_area')

        results = []

        for i, item in enumerate(news_items):
            if i >= max_results:
                break

            title_elem = item.select_one('.news_tit')
            content_elem = item.select_one('.news_dsc')
            press_elem = item.select_one('.info_group .press')
            date_elem = item.select_one('.info_group .info')

            if title_elem:
                title = title_elem.get_text(strip=True)
                link = title_elem.get('href', '')
                content = content_elem.get_text(strip=True) if content_elem else ''
                press = press_elem.get_text(strip=True) if press_elem else ''
                date = date_elem.get_text(strip=True) if date_elem else ''

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