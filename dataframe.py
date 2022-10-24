import pandas as pd
df1=pd.read_csv('file1.csv')
df2=pd.read_csv('file2.csv')
import datacompy
compare = datacompy.Compare(df1,df2,join_columns=’acct_id’, #You can also specify a list of columnsabs_tol=0.0001,rel_tol=0,df1_name=’original’,df2_name=’new’)
print(compare.report())
