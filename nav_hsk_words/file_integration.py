import os
import numpy as np
import pandas as pd
import pickle
from os import listdir
from os.path import isfile, join


def get_csv_list(csv_file_list, folderpath):
    """csv file list를 받아서 읽어 df로 전환 뒤 리스트에 저장해 return"""
    letters_dictionary = []
    for file_name in csv_file_list:
        df = pd.read_csv(f'{folderpath}/{file_name}', encoding='UTF-8')
        # print(np.isnan(df.iloc[1,0]))
        df = df.loc[~np.isnan(df.iloc[:, 0])]
        print(df.head())
        letters_dictionary.append(df)
    # print(letters_dictionary[0].duplicated().iloc[10:15])
    return letters_dictionary


def file_list(path, name=False):  # 파일명 리스트를 가져옴
    files = [f for f in listdir(path) if isfile(join(path, f))]
    if name:
        files = [x for x in files if x.find(name) != -1]
    else:
        pass
    return files


if __name__ == '__main__':
    folder_path = os.path.join('..', 'csv2')
    csv_file_list = file_list(folder_path, name='rel_len')
    print(csv_file_list)
    df_list = get_csv_list(csv_file_list, folder_path)

    df_list[0].to_csv('../csv2/len_1_dict.csv', index=False)
    df_list[1].to_csv('../csv2/len_2_dict.csv', index=False)
    df_list[2].to_csv('../csv2/len_3_dict.csv', index=False)
    df_list[3].to_csv('../csv2/len_4_dict.csv', index=False)

