"""
웹 주소(URI, URL)의 형식:
    프로토콜://서버주소[:포트번호]/경로?쿼리스트링
    http://www.naver.com
    https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon
쿼리 스트링(query string): 클라이언트(브라우저)가 서버로 보내는 정보
    param이름=param값 형식으로 작성
    파라미터가 여러개일 경우에는 &로 파라미터들을 구분

다음에서 "머신 러닝"으로 검색한 기사 100개의 URL 주소와 기사 제목을 출력
다음에서 임의의 검색어(키워드)로 검색한 기사 100개의 URL 주소와 기사 제목을 출력하는
함수 작성하고 테스트
"""
import requests
from bs4 import BeautifulSoup


def daum_search(keyword):
    url = 'http://www.jobkorea.co.kr/Search/?&tabType=recruit'
    # http://www.jobkorea.co.kr/Search/?stext=%EB%94%A5%EB%9F%AC%EB%8B%9D&tabType=recruit&Page_No=2
    # 검색 결과는 1페이지부터 10페이지 까지
    for page in range(1, 11):
        print(f'=== Page {page} ===')
        req_params = {
            'stext': keyword,  # 검색어(키워드)를 쿼리 스트링에 파라미터로 추가
            'Page_No': page  # 검색 페이지 번호를 쿼리 스트링에 파라미터로 추가
        }
        response = requests.get(url, params=req_params)
        html = response.text.strip()

        soup = BeautifulSoup(html, 'html5lib')
        job_links = soup.select('#content .cnt-wrap .recruit-info .clear')  # css 선택자대로 .class, #id, tag 와 띄어쓰기로 구분
        for link in job_links:
            news_title = link.text
            news_url = link.get('href')
            print(news_url, news_title)


if __name__ == '__main__':
    daum_search('네이버')
