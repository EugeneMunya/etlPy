import pandas as pd

df=pd.read_csv('venv/query2.txt',on_bad_lines='skip', delimiter="\t", encoding='utf-8')
dframe=pd.DataFrame(df)
print(dframe)