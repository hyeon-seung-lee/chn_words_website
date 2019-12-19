import pandas as pds

pd = pds.read_excel('../excel/nav_arranged.xlsx')
pd1 = pd.loc[pd['len']==1]
pd2 = pd.loc[pd['len']==2]
pd3 = pd.loc[pd['len']==3]
pd4 = pd.loc[pd['len']==4]


pd1 = pd1.sort_values(by='level')
pd2 = pd2.sort_values(by='level')
pd3 = pd3.sort_values(by='level')
pd4 = pd4.sort_values(by='level')


print(pd1.head(30))

concat_pd=pds.concat([pd1, pd2, pd3, pd4], axis =0)
print(concat_pd)

concat_pd.to_excel('../excel/nav_final.xlsx')