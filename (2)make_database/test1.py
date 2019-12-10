# import pandas as pd
# data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#         'year': [2012, 2012, 2013, 2014, 2014],
#         'reports': [4, 24, 31, 2, 3],
#         'coverage': [25, 94, 57, 62, 70]}
#
# df0 = pd.DataFrame(data, index=['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
# print(df0)
#

# text = 'HSK1급단어'
# print(text.find('1급'))
# for index in range(0, 713, 100):
#     print(index)
import os

import pandas as pd

folder_path = os.path.join('..', 'csv', 'letters_dictionary0.csv')
df = pd.read_csv(folder_path, encoding='UTF-8')
df = df.iloc[:, 1]
print(df)
for row in range(len(df)-1):
    if df.iloc[row].item==df.iloc[row+1].item:
        pass

