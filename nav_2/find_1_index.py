from collections import defaultdict

import pandas as pd

nav_fin = pd.read_excel('../excel/nav_final.xlsx')
len_1_words = nav_fin.loc[nav_fin['len'] == 1]
len_234_words = nav_fin.loc[nav_fin['len'] != 1]
for i in range(len(len_1_words)):
    len_1_words.iloc[i] = len_1_words.iloc[i].str.replace('儿', '')
    len_1_words.iloc[i] = len_1_words.iloc[i].str.replace('(', '')
    len_1_words.iloc[i] = len_1_words.iloc[i].str.replace(')', '')

len_1_words_word = len_1_words['word']
# print(len_234_words.loc[len_234_words['word'].str.contains('爱')].iloc[:,0].values)
related_dict = defaultdict(list)
for word in len_1_words_word:
    # print(word, len_234_words.loc[len_234_words['word'].str.contains(word)])
    # related_dict[word].append()
    rel_id=len_234_words.loc[len_234_words['word'].str.contains(word)].iloc[:,0]
    if rel_id.any():
        related_dict[word]=str(list(rel_id.values)).replace('[', '').replace(']', '')
    else:
        related_dict[word]=''
print(related_dict)
related_dict=pd.DataFrame.from_dict(related_dict, orient='index')
related_dict.to_excel('../excel/rel_index.xlsx')