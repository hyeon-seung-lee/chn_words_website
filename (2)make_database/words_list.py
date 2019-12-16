"""
words list가 링크만 있고, 글자 데이터가 없음. 글자 리스트를 받아오기 위한 파일
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class Get_chndic_data:

    def __init__(self, link):
        self.link = link
        self.get_data = []

    def beautiful_soup(self, link):
        """
        Beautiful Soup Type의 객체를 return
        return값에 다음과 같은 메소드 가능
        data = soup.find('div', id='container').find('div', class_='section_hsk')
        :param link: https://zh.dict.naver.com/ 뒤에 들어갈 {letter_link}  주소
        :return: row 데이터
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument("disable-gpu")
        # https://beomi.github.io/2017/09/28/HowToMakeWebCrawler-Headless-Chrome/

        # driver = webdriver.Chrome("D:/dev/chromedriver.exe", chrome_options=chrome_options)  # 집에서 chromedriver 경로
        driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe", chrome_options=chrome_options)
        # 학원에서 chromedriver 경로
        url = f'https://zh.dict.naver.com/{link}'
        driver.get(url)
        driver.minimize_window()
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html.parser")
        driver.close()
        return soup

    def find_letter_inf(self):
        """
        글자 link를 이용해 글자와 글자 뜻, 병음, 단어일 경우 구성 글자와 구성 글자 링크를 받아옴
        :return:  위 자료로 구성된 list
        """
        # 병음 추가해야 함.
        soup = self.beautiful_soup(self.link)
        letter = soup.find('div', id='container').find('div', class_="section section_entry _section_entry") \
            .find('div', class_="entry_title _guide_lang").find('strong', class_='word').text
        return letter


temp_df = pd.read_csv('../csv/hsk_words_listed.csv', encoding='UTF-8')
hsk_words_link = temp_df.iloc[:, 1]
index = 500
get_data_list = []

########################################## 파일명 변환 ##################################
for lim in range(3,6):
    for i in range(500*lim, 500*(lim+1)):
        while True:
            try:
                get_data = Get_chndic_data(hsk_words_link[i])
                get_data_list.append(get_data.find_letter_inf())
                df = pd.DataFrame(get_data_list)
                print(df.tail())
                df.to_csv(f'../csv/letters_list{500*lim}.csv')
                break
            except AttributeError:
                print('try again')
                continue
