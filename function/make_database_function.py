import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def get_dic_link():
    file_path = os.path.join('..', 'csv', 'dic_link.csv')
    df = pd.read_csv(file_path)
    return df


def get_total_hsk_words_link():
    file_path = os.path.join('..', 'csv', 'total_hsk_words.csv')
    df = pd.read_csv(file_path)
    return df


def get_merged_csv():
    file_path = os.path.join('..', 'csv', 'merged_df.csv')
    df = pd.read_csv(file_path)
    return df


def get_letters_df():
    letters = {
        'id': [],
        'letter': [],
        'mean': [],
        'pron': [],
        'hsk': [],
        'rel': []
    }
    return letters


def get_words_df():
    words = {
        'id': [],
        'word': [],
        'mean': [],
        'pron': [],
        'hsk': [],
        'rel': []
    }
    return words


def get_hsk_level(letter_link):
    """
    Beautiful Soup를 이용한 hsk_level chr을 return
    다음과 같은 Beautiful Soup 코드가 포함됨
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

    hsk_level = soup.find('div', id='container').find('div', class_="section section_entry _section_entry").find('span',
                                                                                                                 class_="btn_toggle_square")
    # print(type(hsk_level))
    return hsk_level.text


def get_pronun(letter_link):
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

    pronun = soup.find('div', id='container').find('div', class_="section section_entry _section_entry"). \
        find('dl', class_="entry_pronounce").find('span', class_="pronounce")
    # print(type(hsk_level))
    return pronun.text.strip('[]').strip(' ')


def get_meaning(letter_link):
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

    pronun = soup.find('div', id='container').find('div', class_="section section_entry _section_entry"). \
        find('p', class_="entry_mean")
    # print(type(hsk_level))
    return pronun.text.split()
