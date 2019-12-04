from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome("D:/dev/chromedriver.exe")  # 집에서 chromedriver 경로
driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")  # 학원에서 chromedriver 경로
url = 'https://zh.dict.naver.com/#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca'
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
print(len(letter))
for i in letter:
    get_letter += i.text
    get_related_letters.append(i.text)

for y in letter:
    get_related_link.append(y['href'])

get_data.append(get_letter)
get_data.append(get_related_letters)
get_data.append(get_related_link)
print(get_data)