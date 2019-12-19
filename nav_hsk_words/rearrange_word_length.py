import pandas as pd
import numpy as np

dict_list = pd.read_excel('../excel/nav_arranged.xlsx')
dict_list = dict_list.iloc[:, :-1]
dict_list['word'] = dict_list['word'].str.replace('儿', '')
dict_list['word'] = dict_list['word'].str.replace('(', '')
dict_list['word'] = dict_list['word'].str.replace(')', '')

dict_list['len'] = dict_list['word'].str.len()
print(dict_list.iloc[-30:, :])
df = dict_list.sort_values(by=['len'], axis=0)
print(df.iloc[-30:, :])

df_1 = df.loc[~df['level'].isin(['1급', '2급', '3급', '4급', '5급', '6급'])]
print(df_1)
# dict_list.to_excel('../excel/.xlsx')
