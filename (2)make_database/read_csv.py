import pandas as pd
def split_str(row):
    """to_csv(dict.items()) 형태로 저장된 csv파일은 str class 형태로 저장되기 때문에 데이터 가공이 필요함"""
    inst_list_ = row.replace("\'", '').replace(' ', '').replace('[', '').replace(']', '').split(',')
    return inst_list_

hsk_words_link=pd.read_csv('../csv/hsk_words_link5.csv', encoding='UTF-8')
# print(hsk_words_link.iloc[:,2])

link_list=[]
for link_row in hsk_words_link.iloc[:,2]:
    link_list.append(split_str(link_row))
list_list=[]
for m in link_list:
    for n in m:
        list_list.append(n)

print(len(set(list_list)))

hsk_words_link = set(list_list)
df_words_list = pd.DataFrame(hsk_words_link)
print(df_words_list)
df_words_list.to_csv('../csv/hsk_words_link6.csv', encoding='UTF-8')