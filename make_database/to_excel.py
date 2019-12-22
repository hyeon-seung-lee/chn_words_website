import os
import pandas as pd

file_path1 = os.path.join('..', 'csv','letters_dictionary_combined.csv')
file_path2 = os.path.join('..', 'csv','merged_df.csv')
df1 = pd.read_csv(f'../csv/{file_path1}', encoding='UTF-8')
df2 = pd.read_csv(f'../csv/{file_path2}', encoding='UTF-8')
df1.to_excel('../csv/letters_dictionary_combined.xlsx', index=False)
df2.to_excel('../csv/merged_df.xlsx', index=False)