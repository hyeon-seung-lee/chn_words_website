import pandas as pd

rel_dict = pd.read_csv('../csv2/intg_dict.csv')
# print(rel_dict)
# print('=======')
# print(rel_dict.loc[rel_dict['id'].duplicated()])
nav_fin = pd.read_excel('../excel/nav_final.xlsx')
rel_fin = pd.merge(nav_fin,rel_dict, how='left', on='id')
print(rel_fin)
rel_fin.to_excel('../excel/nav_final_rel.xlsx', index=False)