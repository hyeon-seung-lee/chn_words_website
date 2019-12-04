from selenium import webdriver
from bs4 import BeautifulSoup


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
        url = f'https://zh.dict.naver.com/{self.link}'
        driver.get(url)
        driver.minimize_window()
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html.parser")
        driver.close()
        return soup

    def find_letter_inf(self):
        soup = self.beautiful_soup(self.link)
        letter = soup.find('div', id='container').find('div', class_="section section_entry _section_entry"). \
            find('div', class_="entry_title _guide_lang").find_all('a', class_="link")

        get_letter = ''
        get_related_letters = []
        get_related_link = []

        if len(letter) > 1:
            for i in letter:
                get_letter += i.text
                get_related_letters.append(i.text)

            for y in letter:
                get_related_link.append(y['href'])

        else:
            get_letter = letter.text

        self.get_data.append(get_letter)
        self.get_data.append(get_related_letters)
        self.get_data.append(get_related_link)
        # print(self.get_data)
        return self.get_data

    def get_hsk_words(self):
        """
        get_data[2] 의 주소 데이터(검색 페이지)를 모두 (글자 페이지) 주소로 변환
        """
        data_list = []
        self.get_data = self.find_letter_inf()
        print(self.get_data[2])
        for link in self.get_data[2]:
            soup = self.beautiful_soup(link)

            for i in range(5):
                try:
                    letter_page_link = soup.find('div', id='container')
                    print(letter_page_link)


                    #     .find('div', class_="section section_keyword")\
                    #     .find('div', class_='origin').find('a', class_='link')
                    # for link_ in letter_page_link:
                    #     data_list.append(link_['href'])
                    #     break
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

print(x.get_hsk_words())

