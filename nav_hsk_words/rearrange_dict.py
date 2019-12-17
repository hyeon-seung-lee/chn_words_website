import pandas as pd


def split_str(row):
    """str로 저장된 리스트를 다시 리스트로 변환함"""
    inst_list_ = row.replace("\'", '').replace(' ', '').replace('[', '').replace(']', '').split(',')
    return inst_list_


df = pd.read_csv('../csv/nav_level6.csv', index_col='index')
# print(df.shape)
word_list = []

for i in range(252):
    for j in range(20):
        word = split_str(str(df.iloc[i, j]))
        word_list.append(word)

words_list = pd.DataFrame(word_list).iloc[:, :-2]
words_list.to_excel('../excel/nav_dict_list.xlsx')
print(words_list.iloc[1, :])
