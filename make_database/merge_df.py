import pandas as pd

informed_hsk_words=pd.read_excel('../excel/integrated_hsk_words_dict.xlsx')
hsk_3100 = pd.read_excel('../excel/hsk_words_list_3100.xlsx')

merge_words= pd.merge(hsk_3100, informed_hsk_words, how='left', on='words')

merge_words.to_excel('../excel/merged_words.xlsx')