import pandas as pd

dict_list = pd.read_excel('../excel/nav_arranged.xlsx')
len_1_words = dict_list.loc[dict_list['word'].str.contains('(儿)')]
print(len_1_words.iloc[:30,:])
# print(len_1_words.iloc[:20,:])