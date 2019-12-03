from selenium import webdriver
from bs4 import BeautifulSoup


def get_letter_relation(letter_link):
    """
    Beautiful Soup Type의 객체를 return
    return값에 다음과 같은 메소드 가능
    data = soup.find('div', id='container').find('div', class_='section_hsk')
    :param letter_link: https://zh.dict.naver.com/ 뒤에 들어갈 {letter_link}  주소
    :return: row 데이터
    """
    # driver = webdriver.Chrome("D:/dev/chromedriver.exe")  # 집에서 chromedriver 경로
    driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")  # 학원에서 chromedriver 경로
    url = f'https://zh.dict.naver.com/{letter_link}'
    driver.get(url)
    driver.minimize_window()
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")
    driver.close()

    letter = soup.find('div', id='container').find('div', class_="section section_entry _section_entry"). \
        find('div', class_="entry_title _guide_lang").find_all('a', class_="link")
    get_letter = ''
    get_related_letters = []
    get_related_link = []
    get_data = []

    for x in letter:
        get_letter += x.text
        get_related_letters.append(x.text)

    for y in letter:
        get_related_link.append(y['href'])

    get_data.append(get_letter)
    get_data.append(get_related_letters)
    get_data.append(get_related_link)

    return get_data


"""
<div class="entry_title _guide_lang">
<!--[D] 각 언어(en, zh)에 맞는 lang값 추가 : 기본값 한글 기준 (kr은 lang값 추가 없음) -->
<strong class="word" lang="zh">
<a href="#/search?query=%E6%88%91" class="link" lang="zh">我</a>
<a href="#/search?query=%E4%BB%AC" class="link" lang="zh">们</a></strong>
</div>
워 -ㅅ-
"""

x = get_letter_relation('#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca')
print(x)
