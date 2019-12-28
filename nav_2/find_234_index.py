from collections import defaultdict

import pandas as pd

nav_fin = pd.read_excel('../excel/nav_final.xlsx')
len_1_words = nav_fin.loc[nav_fin['len'] == 1]
len_234_words = nav_fin.loc[nav_fin['len'] != 1]
for i in range(len(len_1_words)):
    len_1_words.iloc[i] = len_1_words.iloc[i].str.replace('儿', '')
    len_1_words.iloc[i] = len_1_words.iloc[i].str.replace('(', '')
    len_1_words.iloc[i] = len_1_words.iloc[i].str.replace(')', '')

len_1_words_word = list(len_1_words['word'])
related_dict = defaultdict(list)
for index, word in enumerate(len_1_words_word):
    rel_id = len_234_words.loc[len_234_words['word'].str.contains(word)].iloc[:, 0]
    if rel_id.any():
        related_dict[index] = list(rel_id.values)
    else:
        related_dict[index] = []

# print(related_dict)
index_num_dict = defaultdict(list)
index_num_dict2 = defaultdict(list)

for key, value in related_dict.items():
    for num in value:
        index_num_dict[num].append(key)

for key, value in index_num_dict.items():
    index_num_dict2[key]=str(value).replace('[', '').replace(']', '')
print(index_num_dict2)
index_num_df=pd.DataFrame.from_dict(index_num_dict2, orient='index')
index_num_df.to_excel('../excel/rel_index3.xlsx')
