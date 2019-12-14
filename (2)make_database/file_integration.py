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
    inst_list_ = row.replace("\'", '').replace(' ', '').replace('[', '').replace(']', '').split(',')
    return inst_list_


folder_path = os.path.join('..', 'csv')
csv_file_list = file_list(folder_path, name='letters_dictionary')
# print(csv_file_list)

letters_dictionary = []
for file_name in csv_file_list:
    df = pd.read_csv(f'../csv/{file_name}', encoding='UTF-8')
    letters_dictionary.append(df.iloc[:, 1])
# print(letters_dictionary[0].duplicated().iloc[10:15])


for i in range(len(letters_dictionary)):
    letters_dictionary[i] = letters_dictionary[i].drop_duplicates().tolist()

rearranged_dict = []
for list in letters_dictionary:
    for i in range(0, int(len(list)/2), 2) :
        temp = []
        temp.append(list[i])
        temp.append(list[i+1])
        rearranged_dict.append(temp)
print(rearranged_dict)
dict_df = pd.DataFrame(rearranged_dict)
dict_df.to_csv('../csv/letters_dictionary_combined.csv')

