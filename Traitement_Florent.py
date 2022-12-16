import pandas as pd

path = 'Dataset/homicide_intentional_.xlsx'
crimes = pd.read_excel(path)
crimes.columns = crimes.iloc[1]
crimes = crimes[2:]
crimes = crimes[(crimes.Year >= 2000) & (crimes.Year <= 2020)]
crimes = crimes[(crimes.Indicator == 'Victims of intentional homicide') &
                (crimes.Dimension == 'Total') & (crimes.Category == 'Total')
                & (crimes.Sex == 'Total') & (crimes.Age == 'Total')]
crimes = crimes[crimes['Unit of measurement'] == 'Rate per 100,000 population']
crimes = crimes.dropna()
crimes = crimes.drop(columns=['Dimension','Category','Sex','Age'])
print(crimes)

crimes.to_csv('dataset_clean/homicide_clean.csv', index=False)
