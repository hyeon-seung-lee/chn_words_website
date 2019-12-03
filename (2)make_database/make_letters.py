
from function.make_database_function import get_letters_df, get_merged_csv
import pandas as pd

"""
dic_link = get_dic_link()  # dic_link.csv
del dic_link['id']
tot_hsk_words = get_total_hsk_words_link()  # total_hsk_words.csv
del tot_hsk_words['id']
merged_df = pd.merge(dic_link, tot_hsk_words, how='left')  # left join(dic_link + total_hsk_words)
merged_df.to_csv('../csv/merged_df.csv', mode='w')"""


merged_csv = get_merged_csv()
print(merged_csv.head())
letters = get_letters_df()  # letters dictionary

for row in merged_csv['id']:
    letters['id'].append(row)
for row in merged_csv['letter']:
    letters['letter'].append(row)
print(letters['id'])
print(letters['letter'])

# letters['id']
