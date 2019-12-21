from collections import defaultdict

import pandas as pd


def find_rel_letter(len_1_words, len_n_words, n):
    rel_list = defaultdict(list)
    for index, letter in enumerate(len_1_words.iloc[:, 1]):
        print(letter)
        temp = []
        print('letter: ', letter)
        temp.append(letter)
        print('temp: ', temp)
        rel_id = len_n_words.loc[len_n_words['word'].str.contains(letter)]['id'].values
        print('rel_id:',rel_id)
        print('index:',index)
        rel_list[rel_id].append(index)

    print(rel_list)
    rel_list_df = pd.DataFrame(rel_list)
    print(rel_list_df)
    rel_list_df.to_excel(f'../excel/lel_retter{n}.xlsx')


if __name__ == '__main__':
    dict_list = pd.read_excel('../excel/nav_final.xlsx')
    lenth_1_words = pd.read_excel('../excel/rel_letter_1.xlsx')
    len = 2
    lenth_2_words = dict_list.loc[dict_list['len'] == len]
    print(lenth_1_words.iloc[:30, :])
    print(lenth_2_words.iloc[:10, :])
    print(lenth_2_words.iloc[-10:, :])
    find_rel_letter(lenth_1_words, lenth_2_words, 2)
