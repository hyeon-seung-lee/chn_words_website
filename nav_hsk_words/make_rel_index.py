import pandas as pd

nav_list = pd.read_excel('../excel/nav_final.xlsx')
# print(nav_list)

len1_list = nav_list.loc[nav_list['len']==1]['word']
len1_list=pd.DataFrame(len1_list)

for i in range(len(len1_list)):
    len1_list.iloc[i] = len1_list.iloc[i].str.replace('儿', '')
    len1_list.iloc[i] = len1_list.iloc[i].str.replace('(', '')
    len1_list.iloc[i] = len1_list.iloc[i].str.replace(')', '')
rel_letter = []
# print(nav_list.loc[nav_list['word'].str.contains('爱')]['id'])

for letter in len1_list.iloc[:,0]:
    print(letter)
    temp = []
    print('letter: ', letter)
    temp.append(letter)
    print('temp: ',temp)
    lists = nav_list.loc[nav_list['word'].str.contains(letter)]['id'].values
    # temp2 = []
    # for ele in lists:
    #     temp2.append(ele)
    # temp.append(temp2)
    temp.append(lists)
    rel_letter.append(temp)

rel_letter_df=pd.DataFrame(rel_letter)
# print('rel_letter_df[0,1]: ',rel_letter_df.iloc[1,1])
# for i in range(len(rel_letter_df)):
#     rel_letter_df.iloc[i] = rel_letter_df.iloc[i].str.replace('Name: id, dtype: int64', '')

rel_letter_df.to_excel('../excel/rel_retter2.xlsx')