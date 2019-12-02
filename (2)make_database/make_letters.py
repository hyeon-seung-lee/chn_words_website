
from function.make_database_function import get_dic_link, get_letters_df
import pandas as pd


df = get_dic_link()  # dic_link.csv
letters = get_letters_df()  # letters dictionary

for row in df['id']:
    letters['id'].append(row)
for row in df['letter']:
    letters['letter'].append(row)
print(letters['id'])
print(letters['letter'])

# letters['id']=
