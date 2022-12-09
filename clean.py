import pandas as pd

Chomage = pd.read_csv("unemployment.csv",sep=';', on_bad_lines='skip')
Chomage.head(100)

path = 'Dataset/unemployment.csv'
Chomage = pd.read_excel(path)
Chomage = Chomage.drop(axis=1)


print(Chomage)

Chomage.to_csv('dataset_clean/Chomage_clean.csv', index=False)