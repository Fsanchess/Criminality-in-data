import pandas as pd

path = 'C://Users/flore/OneDrive/Documents/GitHub/Criminality-in-data/Dataset/firearms_trafficking.xlsx'
df = pd.read_excel(path)
df.columns = df.iloc[1]
df = df[2:]
df = df[(df.Year >= 2000) & (df.Year <= 2020)]
guns = df[(df.Country == 'India') |
                (df.Country == 'United States of America') | (df.Country == 'Brazil')]
guns = guns.reset_index()

print(guns)