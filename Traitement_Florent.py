import pandas as pd

path = 'C://Users/flore/OneDrive/Documents/GitHub/Criminality-in-data/Dataset/homicide_intentional_.xlsx'
crimes = pd.read_excel(path)
crimes.columns = crimes.iloc[1]
crimes = crimes[2:]
crimes = crimes[(crimes.Year >= 2000) & (crimes.Year <= 2020)]
crimes = crimes[(crimes.Country == 'India') |
                (crimes.Country == 'United States of America') | (crimes.Country == 'Brazil')]
crimes = crimes.reset_index()

print(crimes)