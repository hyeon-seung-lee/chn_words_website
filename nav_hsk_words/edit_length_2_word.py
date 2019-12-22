import csv
from collections import defaultdict

import pandas as pd


def find_rel_letter(len_1_words, len_n_words):
    rel_list = defaultdict(list)
    for index, letter in enumerate(len_1_words.iloc[:, 1]):
        print(letter)
        temp = []
        print('letter: ', letter)
        temp.append(letter)
        print('temp: ', temp)
        rel_id = len_n_words.loc[len_n_words['word'].str.contains(letter)]['id'].values
        print('rel_id:', rel_id)
        print('index:', index)
        for ids in rel_id:
            rel_list[ids].append(index)


    print(rel_list)
    return rel_list


def save_list(p_list, file_loc):
    with open(file_loc, "w") as f:
        for s in p_list:
            f.write(str(s) + "\n")


def read_list(p_list, file_loc):
    with open(file_loc, "r") as f:
        for line in f:
            p_list.append(int(line.strip()))

def save_dict(p_dict, file_loc):
    w = csv.writer(open(file_loc, "w"))
    for key, val in p_dict.items():
        w.writerow([key, val])


if __name__ == '__main__':
    dict_list = pd.read_excel('../excel/nav_final.xlsx')
    length_1_words = pd.read_excel('../excel/rel_letter_1.xlsx')
    len = 4
    length_4_words = dict_list.loc[dict_list['len'] == len]
    print(length_1_words.iloc[:30, :])
    print(length_4_words.iloc[:10, :])
    print(length_4_words.iloc[-10:, :])
    rel_len_4_list = find_rel_letter(length_1_words, length_4_words)


    save_dict(rel_len_4_list, '../csv2/rel_len_4_dict.csv')
