import pandas as pd

merged_df=pd.read_excel('../excel/merged_df.xlsx')
letter_list=merged_df.iloc[:,:]
letters_dict_df = pd.read_excel('../excel/letters_dictionary_revised.xlsx')

merge_letters=pd.merge(letter_list, letters_dict_df, how='left', on='letter')
print(merge_letters)

merge_letters.to_excel('../excel/merged_letters.xlsx')