import os
import pandas as pd


file_path = []
df = []

for i in range(4):
    file_path.append(os.path.join('..', 'csv', f'hsk_words_link{i+1}.csv'))
    df.append(pd.read_csv(file_path[i]))

print(type(df[0]), type(df[1]), type(df[2]), type(df[3]))
# print('df!!\n',df)
total_hsk_words = pd.concat([df[0], df[1], df[2], df[3]])
# total_hsk_words.drop([[0]], axis='columns', inplace=True)
del total_hsk_words['Unnamed: 0']
del total_hsk_words['']
print(total_hsk_words.tail())
total_hsk_words.to_csv('../csv/total_hsk_words.csv', mode='w')