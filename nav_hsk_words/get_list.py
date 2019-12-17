""" 1: 8
    2: 8
    3: 16
    4: 30
    5: 65
    6: 125
    """
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def beautiful_soup(level, page):
    url = f'https://zh.dict.naver.com/CnEntry.nhn?m=hskInfo&hskParam={level}&parts=-1&sortByLetter=ALL&' \
          f'pageNo={page}&fromOldVer'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument("disable-gpu")
    # https://beomi.github.io/2017/09/28/HowToMakeWebCrawler-Headless-Chrome/

    # driver = webdriver.Chrome("D:/dev/chromedriver.exe", chrome_options=chrome_options)  # 집에서 chromedriver 경로
    driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe", chrome_options=chrome_options)
    # 학원에서 chromedriver 경로
    driver.get(url)
    driver.minimize_window()
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")
    driver.close()

    entry_list = soup.find('div', id='container').find('div', class_='entrylist') \
        .find('tbody').find_all('tr')
    # print(entry_list)

    hsk_word = []
    for tr in entry_list:
        letter = tr.find('div', class_='w_baseInfo').find('a').text
        letter_link = tr.find('div', class_='w_baseInfo').find('a').get('href')
        pronun = tr.find('span', class_='e_12_a').text
        meaning = tr.find_all('td')[2].text
        level = tr.find_all('td')[3].text
        print(letter, letter_link, pronun, meaning, level)
        temp = [letter, letter_link, pronun, meaning, level]
        hsk_word.append(temp)
    return hsk_word


level_page = {1: 8,
              2: 8,
              3: 16,
              4: 30,
              5: 65,
              6: 125}
level_page= [8, 8, 16, 30, 65, 125]

get_data_list = []
error_list = []
# level = 3  # 크롤링할 hsk 레벨  ===================
# page = level_page[level-1]  # hsk level에 따른 페이지 수
for level in range(1, 7):
    page = level_page[level - 1]
    for i in range(page):
        try_number = 0
        while True:
            try:
                temp_list = beautiful_soup(level, i+1)
                get_data_list.append(temp_list)
                df = pd.DataFrame(get_data_list)
                df.to_csv(f'../csv/nav_level{level}.csv')
                break
            except AttributeError:
                if try_number < 10:
                    try_number += 1
                    continue
                else:
                    error_list.append(f'level:{level}, page:{page}')
                    pd.DataFrame(error_list).to_csv(f'../csv/error_nav_level{level}.csv')
                    break
