import pandas as pd

Criminality = pd.read_csv("Dataset/homicide_intentional_.xlsx",sep=';', on_bad_lines='skip')
Criminality.head(100)

path = 'Dataset/unemployment.csv'
Criminality = pd.read_excel(path)
Criminality = Criminality.drop(axis=1)


print(Criminality)