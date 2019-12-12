import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd


# C:\dev\lab-python\venv\Scripts\pyinstaller.exe

class job_korea_search():
    def __init__(self, keyword):
        self.keyword = keyword
        self.return_list = []
        self.beautiful_soup()

    def beautiful_soup(self):
        url = 'http://www.jobkorea.co.kr/Search/?tabType=recruit'
        # http://www.jobkorea.co.kr/Search/?stext=%EB%94%A5%EB%9F%AC%EB%8B%9D&tabType=recruit&Page_No=2
        # 검색 결과는 1페이지부터 10페이지 까지
        for page in range(1, 11):
            print(f'=== Page {page} ===')
            req_params = {
                'stext': self.keyword,  # 검색어(키워드)를 쿼리 스트링에 파라미터로 추가
                'Page_No': page  # 검색 페이지 번호를 쿼리 스트링에 파라미터로 추가
            }
            response = requests.get(url, params=req_params)
            html = response.text.strip()
            self.soup = BeautifulSoup(html, 'html5lib')
            self.classify()
        self.save()

    def classify(self):
        soup__ = self.soup.find('div', id='content').find('div', class_='cnt-wrap').find('div', class_='recruit-info') \
            .find('ul', class_='clear').find_all('li', class_="list-post")
        # print(soup__)
        i = 1

        for link in soup__:
            x = 0
            if x == 0:
                x += 1
                print(f'<{i}>')
            else:
                pass
            try:
                # print('link: ', link)
                x += 1
                job_corp = link.find('div', class_='post-list-corp').find('a', class_='name').text.strip()
                job_info = link.find('div', class_='post-list-info').find('a', class_='title').text.strip()
                job_option = link.find('div', class_='post-list-info').find('p', class_='option')
                job_link = link.find('div', class_='post-list-corp').find('a', class_='name').get('href')

                # option_array = ['경력', '학력' , '지역', '모집기간']
                option_array = [job_option.find('span', class_='exp').text, \
                                job_option.find('span', class_='edu').text, \
                                job_option.find('span', class_='loc long').text,
                                job_option.find('span', class_='date').text]
                result = {
                    'job_corp': job_corp,
                    'job_info': job_info,
                    'job_link': 'http://www.jobkorea.co.kr/' + job_link,
                    'job_exp': job_option.find('span', class_='exp').text,
                    'job_edu': job_option.find('span', class_='edu').text,
                    'job_loc': job_option.find('span', class_='loc long').text,
                    'job_date': job_option.find('span', class_='date').text
                }
                print('job_corp: ', job_corp)
                print('job_info: ', job_info)
                print(option_array[0], option_array[1], option_array[2], option_array[3])
                print('job_link: http://www.jobkorea.co.kr/' + job_link)
                i += 1
                self.return_list.append(result)
            except AttributeError:
                i += 1
                continue
        self.result_list = pd.DataFrame(self.return_list)

    def save(self):
        now = datetime.now()
        column_names = ['회사명', '채용정보', '채용링크', '요구경력', '요구학벌', '직장위치', '지원종료일']
        save_name = f'job_korea_{self.keyword}+{now.month}월+{now.day}일+{now.hour}.csv'

        self.result_list.to_csv(save_name, encoding='UTF-8-sig', header=column_names)



if __name__ == '__main__':
    keyword = input('검색어를 입력하세요: ')
    job_korea_search(keyword)
