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


folder_path = os.path.join('..', 'csv')
csv_file_list = file_list(folder_path, name='letters_dictionary')
# print(csv_file_list)

letters_dictionary = []
for file_name in csv_file_list:
    df = pd.read_csv(f'../csv/{file_name}', encoding='UTF-8')
    letters_dictionary.append(df.iloc[:, 1])
print(letters_dictionary)  # 리스트의 요소가 DataFrame Class의 Series객체임

integrate_dic = []
for dic in letters_dictionary:
    i = 0
    for data in dic:
        temp = []
        if dic.iloc[i] == dic.iloc[i + 1]:
            pass
        else:
            temp.append(data)
        i += 1
    integrate_dic.append(temp)

print(integrate_dic)
