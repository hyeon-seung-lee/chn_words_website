import pandas as pd
import numpy as np

dict_list = pd.read_excel('../excel/nav_dict_list.xlsx')
dict_list['len'] = dict_list['word'].str.len()

print(dict_list)

dict=dict_list.groupby(by='len')
print(dict.head())