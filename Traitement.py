import pandas as pd
import geopandas as gpd

path = 'dataset_clean/homicide_clean.csv'
crimes = pd.read_csv(path)

print(crimes)

