# Import
import geopandas as gpd
import mapclassify as mc
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st


# Configuration of the page title and size
confi = st.set_page_config(
      page_title="Dashboard",
      layout="wide")

# Dashboard title
title = st.title('Evolution de la criminalité par pays selon différents critères sociaux de 2000 à 2020')


# Choropleth map with homicide dataset
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
homicide_datapath = 'dataset_clean/homicide_clean.csv'
homicide_dataset = pd.read_csv(homicide_datapath)
pd1_homicide = homicide_dataset.loc[homicide_dataset['Unit of measurement'] == 'Rate per 100,000 population']
pd1_homicide = pd1_homicide.loc[pd1_homicide['Year'] == 2010]

plotting_choropleth_map = world.merge(pd1_homicide, left_on = 'iso_a3', right_on = 'Iso3_code')

choropleth_map = px.choropleth(plotting_choropleth_map,
                               locations="iso_a3",
                               color="VALUE",
                               hover_name="Country",
                               color_continuous_scale=["lightyellow", "orange", "red"])

choropleth_map.update_layout(
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

# Display choropleth map
title_choropleth_map = st.subheader("Nombre de victimes d'homicides volontaires par pays en 2010 (nb pour 100 000)")
plot_choropleth_map = st.plotly_chart(choropleth_map, use_container_width=True)



# Charts with education dataset
tertiary_path = 'Dataset/education_tertiary_25-64.csv'
tertiary_dataset = pd.read_csv(tertiary_path, sep = ',')
pd_tertiary = tertiary_dataset[tertiary_dataset['LOCATION'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]
below_path = 'Dataset/education_below-upper-secondary_25-64.csv'
below_datatset = pd.read_csv(below_path, sep = ',')
pd_below = below_datatset[below_datatset['LOCATION'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]

tertiary_chart = px.line(pd_tertiary, x="TIME", y="Value", color="LOCATION", title="Diplôme d'étude supérieur", markers=True)
below_chart = px.line(pd_below, x="TIME", y="Value", color="LOCATION", title="Diplôme inférieur au niveau bac", markers=True)

# Display charts with education dataset
title_education_chart = st.subheader("Pourcentage de la population ayant un diplôme d'étude supérieur VS inférieur au niveau bac parmi les 25-64 ans")

col1, col2 = st.columns(2)

with col1:
   st.plotly_chart(tertiary_chart, use_container_width=True)
with col2:
   st.plotly_chart(below_chart, use_container_width=True)



# Chart with homicide dataset
pd2_homicide = homicide_dataset[homicide_dataset['Iso3_code'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF'])]
pd2_homicide = pd2_homicide.loc[pd2_homicide['Unit of measurement'] == 'Rate per 100,000 population']
pd2_homicide = pd2_homicide[pd2_homicide['Year'].isin([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])]
homicide_chart = px.line(pd2_homicide, x="Year", y="VALUE", color="Country", title="taux crime", markers=True)

# Display chart with homicide dataset
title_homicide_chart = st.subheader('Evolution du taux de criminalité')
plot_homicide_chart =st.plotly_chart(homicide_chart, use_container_width=True)