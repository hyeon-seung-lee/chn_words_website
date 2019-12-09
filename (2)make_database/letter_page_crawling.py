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
        letter = soup.find('div', id='container').find('div', class_="section section_entry _section_entry") \
            .find('div', class_="entry_title _guide_lang")
        # find_all('a', class_="link")
        letter_meaning = soup.find('div', id='container').find('div', class_="section section_entry _section_entry") \
            .find('p', class_="entry_mean")  # 뜻
        pronunc = soup.find('div', id='container').find('div', class_="section section_entry _section_entry"). \
            find('dl', class_="entry_pronounce").find('div', class_="item").find('span', class_="pronounce")  # 병음

        dict_list = [pronunc.text, letter_meaning.text]
        return dict_list


# x = get_letter_relation('#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca')
hsk_letters_link = pd.read_csv('../csv/merged_df.csv', encoding='UTF-8')
# print(hsk_words_link.iloc[:,1])
for index in range(118, 713, 50):
    get_data_list = []
    letter_index = index
    for link in hsk_letters_link.iloc[index:index + 50, 2]:
        get_data_list.append(hsk_letters_link.iloc[letter_index, 1])
        try_number = 0
        while True:
            try:
                get_data = Get_chndic_data(link)
                get_data_list.append(get_data.find_letter_inf())
                df = pd.DataFrame(get_data_list)
                print(df.tail())
                df.to_csv(f'../csv/letters_dictionary{index}.csv')
                letter_index += 1
                break
            except AttributeError:
                print('try again')
                if try_number < 5:
                    try_number += 1
                    continue
                else:
                    break

