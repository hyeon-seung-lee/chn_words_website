import pandas as pd

def split_str(row):
    """to_csv(dict.items()) 형태로 저장된 csv파일은 str class 형태로 저장되기 때문에 데이터 가공이 필요함"""
    inst_list_ = row.replace(' ', '').replace('[', '').replace(']', '').split(',')
    return inst_list_

nav_list = pd.read_excel('../excel/rel_letter_1.xlsx', index_col='id')

print(nav_list)
print(nav_list.iloc[1])
# print(nav_list[1].str.strip.split('\t'))

for row in nav_list.iloc[:,1]:
    print(split_str(row))