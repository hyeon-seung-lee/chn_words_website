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
        driver = webdriver.Chrome("D:/dev/chromedriver.exe")  # 집에서 chromedriver 경로
        # driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")  # 학원에서 chromedriver 경로
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
        pronunc = soup.find('div', id='container').find('div', class_="section section_entry _section_entry"). \
            find('dl', class_="entry_pronounce").find('div', class_="item").find('span', class_="pronounce")
        get_letter = ''  # 글자
        letter_component = []  # 단어일 경우 구성 글자
        letter_component_link = []  # 구성 글자 링크
        letter_pronoun = [pronunc.text]
        letter_link = letter.find_all('a', class_="link")
        if letter_link:
            for i in letter_link:
                get_letter += i.text
                letter_component.append(i.text)

            for y in letter_link:
                letter_component_link.append(y['href'])
        else:
            get_letter = letter.find('strong', lang="zh").text
            print('letter: ',get_letter)
        self.get_data.append(get_letter)  # 글자
        self.get_data.append(letter_pronoun)
        self.get_data.append(letter_component)  # 단어일 경우 구성 글자
        self.get_data.append(letter_component_link)  # 구성 글자 링크
        print(self.get_data)
        return self.get_data

    def to_dict_page(self):
        """
        get_data[2] 의 주소 데이터(검색 페이지)를 모두 (글자 페이지) 주소로 변환
        """
        data_list = []
        self.get_data = self.find_letter_inf()
        # print(self.get_data[3][1])
        for link in self.get_data[3]:
            # print('link:', link)
            soup = self.beautiful_soup(link)
            letter_page_link = soup.find('div', id='container') \
                .find('div', id="content").find('div', class_="section section_keyword") \
                .find('div', class_='row') \
                .find('div', class_="origin").find('a', class_='link')
            print(letter_page_link)
            if letter_page_link is not None:
                data_list.append(letter_page_link['href'])
            else:
                continue
            # print(data_list)
        self.get_data[3] = data_list
        return self.get_data


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
get_data_list = []
hsk_words_link = pd.read_csv('../csv/hsk_words_link6.csv', encoding='UTF-8')
# print(hsk_words_link.iloc[:,1])
for link in hsk_words_link.iloc[24:, 1]:
    get_data = Get_chndic_data(link)
    get_data_list.append(get_data.to_dict_page())
    df = pd.DataFrame(get_data_list)
    print(df.tail())
    df.to_csv('../csv/hsk_words_dictionary2.csv')