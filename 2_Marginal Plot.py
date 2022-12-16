import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('dataset_clean/homicide_clean.csv')
df = df[df.Year == '2010']

sns.jointplot(x=df["Country"], y=df["VALUE"], kind='scatter')
print(df[0:1])
