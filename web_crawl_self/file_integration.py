import os
import pandas as pd


file_path = []
df = []

for i in range(4):
    file_path.append(os.path.join('..', 'csv', f'hsk_words_link{i+1}.csv'))
    df.append(pd.read_csv(file_path[i])[-0])

print(df)

total_hsk_words = pd.merge(pd.merge(pd.merge(df[0], df[1]), df[2]), df[3])
print(total_hsk_words)
# total_hsk_words.to_csv('../csv/total_hsk_words', mode='w')