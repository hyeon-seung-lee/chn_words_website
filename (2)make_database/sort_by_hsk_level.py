from function.make_database_function import get_merged_csv
import pandas as pd

# print(type(get_merged_csv()))
merged_csv = get_merged_csv()
related_hsk_words = merged_csv['rel'].tolist()
# print(related_hsk_words[3].replace("\'", '').replace(' ', '').replace('[', '').replace(']', '').split(','))
# print(type(related_hsk_words[0]))

hsk_words_list = {
    '1급': [],
    '2급': [],
    '3급': [],
    '4급': [],
    '5급': [],
    '6급': []
}


def split_str(row):
    inst_list_ = row.replace("\'", '').replace(' ', '').replace('[', '').replace(']', '').split(',')
    return inst_list_


for i in related_hsk_words:
    if type(i) == str:
        inst_list = split_str(i)
        for j in inst_list:
            print(j)
            if j.find('1급') == 3:
                key = '1급'
                print('key1:',key)
            elif j.find('2급') == 3:
                key = '2급'
                print('key2:', key)
            elif j.find('3급') == 3:
                key = '3급'
                print('key3:', key)
            elif j.find('4급') == 3:
                key = '4급'
                print('key4:', key)
            elif j.find('5급') == 3:
                key = '5급'
                print('key5:', key)
            elif j.find('6급') == 3:
                key = '6급'
                print('key6:', key)
            else:
                print('입력')
                hsk_words_list[key].append(j)
    else:
        pass
print(hsk_words_list['6급'])

df_hsk_words=pd.DataFrame(hsk_words_list.items()).to_csv('../csv/hsk_words_sorted_by_level.csv')
