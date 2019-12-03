from function.make_database_function import get_hsk_level, get_pronun, get_meaning
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

"""
가져와야 할 자료:
 letters = {
        'id': [],
        'letter': [],
        'mean': [],
        'pron': [],
        'hsk': [],
        'rel': []
    }
    중 mean, pron, hsk, rel, letter

"""



# women = {'hsk': get_net_access('#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca')}
# hsk level
a = get_hsk_level('#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca')
print(x)
# meaning
b = get_meaning('#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca')

# pronunciation
c = get_pronun('#/entry/zhko/0cb25d23fd4c4afe9b4cd5a22ccad8ca')

# letter

# related words (상호 연결)
