import pandas as pd


def split_str(row):
    """str로 저장된 리스트를 다시 리스트로 변환함"""
    inst_list_ = row.replace("\'", '').replace(' ', '').replace('[', '').replace(']', '').split(',')
    return inst_list_


ldc = pd.read_excel('../excel/letters_dictionary_combined.xlsx')
meaning_list=[]
for i in range(len(ldc)):
    temp = [ldc.iloc[i,0]]
    split_list=split_str(ldc.iloc[i, 1])

    for el in split_list:
        temp.append(el)
    meaning_list.append(temp)

let_dic_comb_df = pd.DataFrame(meaning_list)
let_dic_comb_df.to_excel('../excel/letters_dictionary_revised.xlsx')
