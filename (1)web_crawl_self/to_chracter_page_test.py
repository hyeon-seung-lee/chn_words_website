from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

hanyu = ['东']


def get_han_chr_link(han_chr):
    while True:
        try:
            driver = webdriver.Chrome("D:/dev/chromedriver.exe")
            url = f'https://zh.dict.naver.com/#/search?range=all&query={han_chr}'
            driver.get(url)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content, "html.parser")
            chr_link = soup.find('div', id='container').find('div', class_='origin').find('a', class_='link')
            driver.close()
            return chr_link['href']

        except AttributeError:
            driver.close()
            pass

chr_dic_address = {}

for i in hanyu:
    chr_dic_address[i] = get_han_chr_link(i)
    print(chr_dic_address)

link_data = pd.DataFrame(chr_dic_address.items(), columns=['chr', 'link'])
link_data.to_csv('dic_link.csv', encoding='utf-8')
# print(f'chrlink: {chr_link}')

# print(chr_link['href'])

# https://zh.dict.naver.com/#/search?range=all&query='문자'
# for chn_character in hanyu_list.hanyu:
# html = urlopen(f"https://zh.dict.naver.com/#/search?range=all&query={chn_character}")

"""							11,579건
						</span>
</h3>
<div class="component_keyword has-saving-function">
<div class="row">
<div class="origin">
<a class="link" href="#/entry/zhko/2f2072ca48fe4153b63f6d7d8c664b09" lang="zh_CN" onclick="clickcr(this,'wrd.entry','2f2072ca48fe4153b63f6d7d8c664b09','1',event);">"""

# #/entry/zhko/2f2072ca48fe4153b63f6d7d8c664b09
# https://zh.dict.naver.com/ 뒤에 위의 주소를 붙여주면 그 글자의 페이지로 접속
