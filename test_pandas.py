import pandas as pd

df = pd.read_csv('marks_book.csv')
g = df.groupby('id')['mark'].sum()
print(g)

#for index, row in df.iterrows():
#    print(row)

