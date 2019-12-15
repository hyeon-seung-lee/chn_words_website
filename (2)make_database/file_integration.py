import os
import pandas as pd
from os import listdir
from os.path import isfile, join


def file_list(path, name=False):  # 파일명 리스트를 가져옴
    files = [f for f in listdir(path) if isfile(join(path, f))]
    if name:
        files = [x for x in files if x.find(name) != -1]
    else:
        pass
    return files


def split_str(row):
    """str로 저장된 리스트를 다시 리스트로 변환함"""
    inst_list_ = row.replace("\'", '').replace(' ', '').replace('[', '').replace(']', '').split(',')
    return inst_list_

def get_csv_list(csv_file_list):
    """csv file list를 받아서 읽어 df로 전환 뒤 리스트에 저장해 return"""
    letters_dictionary = []
    for file_name in csv_file_list:
        df = pd.read_csv(f'../csv/{file_name}', encoding='UTF-8')
        letters_dictionary.append(df.iloc[:, 1])
    # print(letters_dictionary[0].duplicated().iloc[10:15])
    return letters_dictionary


def remove_duplicates(dict):
    """실패로 인해 생성된 중복 row들을 제거한 뒤 그 list를 return"""
    for i in range(len(dict)):
        dict[i] = dict[i].drop_duplicates().tolist()
    return dict


def read_two_lines(p_dict):
    """2줄씩 row를 읽어서 하나의 row로 합친 list를 return"""
    rearranged_dict = []
    for list in p_dict:
        for i in range(0, int(len(list)/2), 2) :
            temp = []
            temp.append(list[i])
            temp.append(list[i+1])
            rearranged_dict.append(temp)
    return rearranged_dict


folder_path = os.path.join('..', 'csv')
csv_file_list = file_list(folder_path, name='letters_dictionary')
# print(csv_file_list)




# dict_df = pd.DataFrame(rearranged_dict)
# dict_df.to_csv('../csv/letters_dictionary_combined.csv')

