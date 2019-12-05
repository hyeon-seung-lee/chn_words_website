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
        # driver = webdriver.Chrome("D:/dev/chromedriver.exe")  # 집에서 chromedriver 경로
        driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")  # 학원에서 chromedriver 경로
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
        letter = soup.find('div', id='container').find('div', class_="section section_entry _section_entry"). \
            find('div', class_="entry_title _guide_lang")  # find_all('a', class_="link")
        pronunc
        get_letter = ''  # 글자
        letter_component = []  # 단어일 경우 구성 글자
        letter_component_link = []  # 구성 글자 링크

        if len(letter) > 1:
            for i in letter:
                get_letter += i.text
                letter_component.append(i.text)

            letter_link = letter.find_all('a', class_="link")
            for y in letter_link:
                letter_component_link.append(y['href'])

        else:
            get_letter = letter.text

        self.get_data.append(get_letter)
        self.get_data.append(letter_component)
        self.get_data.append(letter_component_link)
        # print(self.get_data)
        return self.get_data

    def to_dict_page(self):
        """
        get_data[2] 의 주소 데이터(검색 페이지)를 모두 (글자 페이지) 주소로 변환
        """
        data_list = []
        self.get_data = self.find_letter_inf()
        print(self.get_data[2])
        for link in self.get_data[2]:
            soup = self.beautiful_soup(link)

            try:
                while True:
                    letter_page_link = soup.find('div', id='container') \
                        .find('div', id="content").find('div', class_="component_keyword has-saving-function") \
                        .find('div', class_="origin").find('a', class_='link')
                    print(letter_page_link)
                    if letter_page_link is not None:
                        data_list.append(letter_page_link['href'])
                        break
                    else:
                        continue


            except AttributeError:
                pass
                print('error?')

        self.get_data[2] = data_list
        return self.get_data


def split_str(self, row):
    """to_csv(dict.items()) 형태로 저장된 csv파일은 str class 형태로 저장되기 때문에 데이터 가공이 필요함"""
    inst_list_ = row.replace("\'", '').replace(' ', '').replace('[', '').replace(']', '').split(',')
    return inst_list_


"""
<div class="entry_title _guide_lang">
<!--[D] 각 언어(en, zh)에 맞는 lang값 추가 : 기본값 한글 기준 (kr은 lang값 추가 없음) -->
<strong class="word" lang="zh">
<a href="#/search?query=%E6%88%91" class="link" lang="zh">我</a>
<a href="#/search?query=%E4%BB%AC" class="link" lang="zh">们</a></strong>
</div>
워 -ㅅ-
"""

# x = get_letter_relation('#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca')
x = Get_chndic_data('#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca')
pd.read_csv('')
print(x.to_dict_page())
