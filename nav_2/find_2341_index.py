import pandas as pd

nav_fin = pd.read_excel('../excel/nav_final.xlsx')
len_1_words = nav_fin.loc[nav_fin['len'] == 1]
len_234_words = nav_fin.loc[nav_fin['len'] != 1]
len_234_rel_excel = pd.read_excel('../excel/rel_index3.xlsx')

len_234_words_word = len_234_words['id']
print(len_234_words_word)
merged_df=pd.merge(len_234_words_word, len_234_rel_excel, on='id', how='left')
merged_df.to_excel('../excel/rel_index4.xlsx')