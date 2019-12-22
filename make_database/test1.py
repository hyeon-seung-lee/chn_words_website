# import pandas as pd
# data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#         'year': [2012, 2012, 2013, 2014, 2014],
#         'reports': [4, 24, 31, 2, 3],
#         'coverage': [25, 94, 57, 62, 70]}
#
# df0 = pd.DataFrame(data, index=['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
# print(df0)
#

# text = 'HSK1급단어'
# print(text.find('1급'))
# for index in range(0, 713, 100):
#     print(index)
import os

import pandas as pd

# folder_path = os.path.join('..', 'csv', 'letters_dictionary0.csv')
# df = pd.read_csv(folder_path, encoding='UTF-8')
# df = df.iloc[:, 1]
# print(df)
# for row in range(len(df)-1):
#     if df.iloc[row].item==df.iloc[row+1].item:
#         pass


# list = [1, 2, 3, 4]
# print(list)
# list[0] = 3
# print(list)
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def BTS(level, page):
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

    hsk_word=[]
    for tr in entry_list:
        letter = tr.find('div', class_='w_baseInfo').find('a').text
        letter_link = tr.find('div', class_='w_baseInfo').find('a').get('href')
        pronun = tr.find('span', class_='e_12_a').text
        meaning = tr.find_all('td')[2].text
        level = tr.find_all('td')[3].text
        # print(letter, letter_link, pronun, meaning, level)
        temp=[letter, letter_link, pronun, meaning, level]
        print(temp)
        hsk_word.append(temp)
    return hsk_word

if __name__ == '__main__':

    BTS(3, 1)
