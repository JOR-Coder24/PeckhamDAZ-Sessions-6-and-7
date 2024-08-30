import pandas as pd
df = pd.read_csv('data.csv')
new_df = df.dropna()
#removes duplicates of data
new_df=new_df.drop_duplicates()
print(new_df)
new_df.to_csv('new_data.csv')


