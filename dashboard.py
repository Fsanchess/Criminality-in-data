import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
import mapclassify as mc

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
)

st.title('Evolution de la criminalité par pays selon différents critères sociaux de 2000 à 2020')


###

import plotly.express as px
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
file_name3 = 'dataset_clean/homicide_clean.csv'
crimesA = pd.read_csv(file_name3)
crimes = crimesA.loc[crimesA['Unit of measurement'] == 'Rate per 100,000 population']
crimes = crimes.loc[crimes['Year'] == 2010]

for_plotting2 = world.merge(crimes, left_on = 'iso_a3', right_on = 'Iso3_code')

fig = px.choropleth(for_plotting2, locations="iso_a3",
                    color="VALUE", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale=["lightyellow", "orange", "red"])


fig.update_layout(
    title_text='Victims of intentional homicide by Country (2010)',
    geo=dict(
        showframe=True,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://dataunodc.un.org/dp-intentional-homicide-victims">\
            United Nations</a>',
        showarrow = False
    )]
)


st.subheader('Nombre de victimes de homicides volontaires par pays en 2010 (nb pour 100 000)')

plt.axis("off")
st.plotly_chart(fig, use_container_width=True)


###
st.subheader("Pourcentage de la population ayant un diplôme d'étude supérieur VS inférieur au niveau bac parmi les 25-64 ans")

path_tertiary = 'Dataset/education_tertiary_25-64.csv'
tertiary = pd.read_csv(path_tertiary, sep = ',')
tertiary = tertiary[tertiary['LOCATION'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]
path_below = 'Dataset/education_below-upper-secondary_25-64.csv'
below = pd.read_csv(path_below, sep = ',')
below = below[below['LOCATION'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]


fig2 = px.line(tertiary, x="TIME", y="Value", color="LOCATION", title="Diplôme d'étude supérieur", markers=True)

fig3 = px.line(below, x="TIME", y="Value", color="LOCATION", title="Diplôme inférieur au niveau bac", markers=True)


col1, col2 = st.columns(2)

with col1:
   st.plotly_chart(fig2, use_container_width=True)

with col2:
   st.plotly_chart(fig3, use_container_width=True)





###
st.subheader('Evolution du taux de criminalité')

evol_crime = crimesA[crimesA['Iso3_code'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF'])]
evol_crime = evol_crime.loc[evol_crime['Unit of measurement'] == 'Rate per 100,000 population']
evol_crime = evol_crime[evol_crime['Year'].isin([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])]
fig5 = px.line(evol_crime, x="Year", y="VALUE", color="Country", title="taux crime", markers=True)

st.plotly_chart(fig5, use_container_width=True)