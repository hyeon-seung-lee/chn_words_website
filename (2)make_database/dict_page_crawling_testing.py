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
        url = f'https://zh.dict.naver.com/{link}'
        driver.get(url)
        driver.minimize_window()
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html.parser")
        driver.close()
        return soup

    def find_word_inf(self):
        soup = self.beautiful_soup(self.link)
        letter = soup.find('div', id='container').find('div', class_="section section_entry _section_entry"). \
            find('div', class_="entry_title _guide_lang").find_all('a', class_="link")
        get_letter = ''
        get_related_letters = []
        get_related_link = []

        for i in letter:
            get_letter += i.text
            get_related_letters.append(i.text)

        for y in letter:
            get_related_link.append(y['href'])

        self.get_data.append(get_letter)
        self.get_data.append(get_related_letters)
        self.get_data.append(get_related_link)

        return self.get_data

    def find_letter_inf(self):
        soup = self.beautiful_soup(self.link)
        letter = soup.find('div', id='container').find('div', class_="section section_entry _section_entry"). \
            find('div', class_="entry_title _guide_lang").find('strong', class_="word")
        get_letter = ''
        get_related_letters = []
        get_related_link = []



        for y in letter:
            get_related_link.append(y['href'])

        self.get_data.append(get_letter)
        self.get_data.append(get_related_letters)
        self.get_data.append(get_related_link)

        return self.get_data

    def change_related_words(self):
        """
        get_data[2] 의 주소 데이터(검색 페이지)를 모두 (글자 페이지) 주소로 변환
        """
        data_list = []
        self.get_data = self.find_word_inf()
        for link in self.get_data[2]:
            soup = self.beautiful_soup(link)

            for i in range(5):
                try:
                    letter_page_link = soup.find('div', id='container').find('div', class_="section section_keyword")\
                        .find('div', class_='origin').find('a', class_='link')
                    data_list.append(letter_page_link['href'])
                    break
                except AttributeError:
                    pass
                    print('error?')

        self.get_data[2] = data_list
        return self.get_data

    def execute(self):
        pass





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
# x = Get_chndic_data('#/entry/zhko/3991a2a5344e40cbb91d4b08c3e36e26')  # 星
# ['我们', ['我', '们'], ['#/entry/zhko/a163884686ac406abadf39a35d06c9f5', '#/entry/zhko/a4dce4b8e2b742abab8555684e8d845f']]

x = Get_chndic_data('#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca')  # 我们

print(x.change_related_words())
