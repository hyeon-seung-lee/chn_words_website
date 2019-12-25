import pandas as pd

nav_fin = pd.read_excel('../excel/nav_final.xlsx')
len_1_words = nav_fin.loc[nav_fin['len'] == 1]
len_234_words = nav_fin.loc[nav_fin['len'] != 1]
for i in range(len(len_1_words)):
    len_1_words.iloc[i] = len_1_words.iloc[i].str.replace('儿', '')
    len_1_words.iloc[i] = len_1_words.iloc[i].str.replace('(', '')
    len_1_words.iloc[i] = len_1_words.iloc[i].str.replace(')', '')

len_1_words_word = len_1_words['word']

for word in len_1_words_word:
    len_234_words.loc[len_234_words['word'].str.contains(word)]
