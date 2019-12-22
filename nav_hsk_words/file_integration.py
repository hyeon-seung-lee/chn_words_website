import os
from make_database import file_integration as fi
import pandas as pd

if __name__ == '__main__':

    folder_path = os.path.join('..', 'csv2')
    csv_file_list = fi.file_list(folder_path, name='letters_list')
    df_list = fi.get_csv_list(csv_file_list)
    integrated_df = df_list[0]
    print('len(df_list):', len(df_list))
    for i in range(1, len(df_list)):
        integrated_df = pd.concat([integrated_df, df_list[i]], axis=0)

    print(integrated_df)
    integrated_df.to_excel('../excel/hsk_words_list_3100.xlsx', index=None, header=['word'])
    # print(integrated_file)