# Import
import geopandas as gpd
import mapclassify as mc
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
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
#title = st.title('Evolution de la criminalité par pays selon différents critères sociaux de 2000 à 2020')
title = st.markdown("<h1 style='text-align: center; color: dark grey;'>Evolution de la criminalité par pays<br>selon différents critères sociaux de 2000 à 2020<br><br></h1>", unsafe_allow_html=True)

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
                               color_continuous_scale="YlOrRd")

choropleth_map.update_layout(
    title = 'Criminalité par pays',
    height=700,
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
            Organisation des Nations unies</a>',
        showarrow = False
    )]
)

plt.figure(figsize=(7,3))

# Display choropleth map
title_choropleth_map = st.header("Map avec nombre de victimes d'homicide volontaire par pays en 2010 (pour 100 000 habitants)")
plot_choropleth_map = st.plotly_chart(choropleth_map, use_container_width=True)



# Chart with homicide dataset
criminalite = px.scatter(pd1_homicide, x="Country", y="VALUE",marginal_x= False, marginal_y="violin",
                  labels={
                     "VALUE": "Nb crimes pour 100 000 habitants",
                     "Country": "Pays"},
                  title = 'Criminalité par pays',
                  color_continuous_scale=["lightyellow", "orange", "red"]
                 )

# Display charts with unemployment dataset
title_unemployment_chart = st.header("Nombre de victimes d'homicide volontaire par pays en 2010 (pour 100 000 habitants)")
plot_unemployment_chart =st.plotly_chart(criminalite, use_container_width=True)



st.markdown("<p style= color: dark grey><font size='4'><br><br>Pour la suite de l'analyse, 6 pays avec des caractéristiques différents ont été choisis (développés/non développés, nord/sud, de tous les continents) :<br><ul><li>Australia (AUS)</li><li>Brazil (BRA)</li><li>India (IND)</li><li>Sweden (SWE)</li><li>United States of America (USA)</li><li>South Africa (ZAF)</li></ul><br></font></p>", unsafe_allow_html=True)



# Chart with homicide dataset
pd2_homicide = homicide_dataset[homicide_dataset['Iso3_code'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF'])]
pd2_homicide = pd2_homicide.loc[pd2_homicide['Unit of measurement'] == 'Rate per 100,000 population']
pd2_homicide = pd2_homicide[pd2_homicide['Year'].isin([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])]
homicide_chart = px.line(pd2_homicide, x="Year", y="VALUE", color="Iso3_code", markers=True,
                         title = 'Crime par pays',
                         category_orders={"Iso3_code": ["AUS", "BRA", "IND", "SWE","USA","ZAF"]},
                         labels={
                            "Year" : "Année",
                            "VALUE" : "Nb crimes pour 100 000 habitants",
                            "Iso3_code" : "Pays"
                         })

# Display chart with homicide dataset
#title_homicide_chart = st.header('Evolution du taux de criminalité')
#plot_homicide_chart =st.plotly_chart(homicide_chart, use_container_width=True)


# Charts with prison dataset
prison_path = 'dataset_clean/prisons.csv'
prison_dataset = pd.read_csv(prison_path, sep = ';', encoding = "ISO-8859-1")
pd_prison = prison_dataset[prison_dataset['Iso3_code'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]

prison_chart = px.line(pd_prison, x="Year", y="VALUE", color="Iso3_code", markers=True,
                         title = 'Prisonniers par pays',
                         category_orders={"Iso3_code": ["AUS", "BRA", "IND", "SWE","USA","ZAF"]},
                         labels={
                            "Year" : "Année",
                            "VALUE" : "Nb prisonniers pour 100 000 habitants",
                            "Iso3_code" : "Pays"
                         })

# Display charts with prison dataset
#title_prison_chart = st.header("Evolution du nombre de prisonniers (pour 100 000 habitants)")
#plot_prison_chart =st.plotly_chart(prison_chart, use_container_width=True)


col1, col2 = st.columns(2)

with col1:
   st.header('Evolution du nombre de crimes')
   st.plotly_chart(homicide_chart, use_container_width=True)
with col2:
   st.header("Evolution du nombre de prisonniers")
   st.plotly_chart(prison_chart, use_container_width=True)



# Charts with education dataset
tertiary_path = 'Dataset/education_tertiary_25-64.csv'
tertiary_dataset = pd.read_csv(tertiary_path, sep = ',')
pd_tertiary = tertiary_dataset[tertiary_dataset['LOCATION'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]
below_path = 'Dataset/education_below-upper-secondary_25-64.csv'
below_datatset = pd.read_csv(below_path, sep = ',')
pd_below = below_datatset[below_datatset['LOCATION'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]

tertiary_chart = px.line(pd_tertiary, x="TIME", y="Value", color="LOCATION", title="Taux de diplômés d'étude supérieur", markers=True,
                         category_orders={"LOCATION": ["AUS", "BRA", "IND", "SWE","USA","ZAF"]},
                         labels={
                            "TIME" : "Année",
                            "Value" : "Taux de diplômés",
                            "LOCATION" : "Pays"
                         })
below_chart = px.line(pd_below, x="TIME", y="Value", color="LOCATION", title="Taux de diplômés inférieur au niveau bac", markers=True,
                         category_orders={"LOCATION": ["AUS", "BRA", "IND", "SWE","USA","ZAF"]},
                         labels={
                            "TIME" : "Année",
                            "Value" : "Taux de diplômés",
                            "LOCATION" : "Pays"
                         })

# Display charts with education dataset
title_education_chart = st.header("Evolution du taux de diplômés d'étude supérieur VS inférieur au niveau bac parmi la population 25-64 ans")

col_education_1, col_education_2 = st.columns(2)

with col_education_1:
   st.plotly_chart(tertiary_chart, use_container_width=True)
with col_education_2:
   st.plotly_chart(below_chart, use_container_width=True)



# Charts with unemployment dataset
unemployment_path = 'dataset_clean/unemployment_clean.csv'
unemployment_dataset = pd.read_csv(unemployment_path, sep = ';')
pd_unemployment = unemployment_dataset[unemployment_dataset['Country Code'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]
Year=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
unemployment_chart = px.bar(pd_unemployment,
             x=Year,
             y=[pd_unemployment['Value'].loc[pd_unemployment['Country Code'] == 'AUS'],
                pd_unemployment['Value'].loc[pd_unemployment['Country Code'] == 'BRA'],
                pd_unemployment['Value'].loc[pd_unemployment['Country Code'] == 'IND'],
                pd_unemployment['Value'].loc[pd_unemployment['Country Code'] == 'SWE'],
                pd_unemployment['Value'].loc[pd_unemployment['Country Code'] == 'USA'],
                pd_unemployment['Value'].loc[pd_unemployment['Country Code'] == 'ZAF']],
             title="Evolution du taux de chômage",
             labels={"variable": "Pays"},
             )

# Change the bar mode
newnames = {'wide_variable_0':'AUS',
            'wide_variable_1': 'BRA',
           'wide_variable_2': 'IND',
           'wide_variable_3': 'SWE',
           'wide_variable_4': 'USA',
           'wide_variable_5': 'ZAF'}
unemployment_chart.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )
unemployment_chart.update_layout(
    yaxis=dict(
        title_text="Taux de chômages",
        titlefont=dict(size=15)),
    xaxis=dict(
        title_text="Année",
        titlefont=dict(size=15))
)

# Display charts with unemployment dataset
title_unemployment_chart = st.header("Evolution du taux de chômage")
plot_unemployment_chart =st.plotly_chart(unemployment_chart, use_container_width=True)


#------------------ remplissage prison 
df_prison = pd.read_excel("data_cts_prisons_and_prisoners.xlsx")
df_prison = df_prison[(df_prison.Iso3_code == "AUS") | (df_prison.Iso3_code == "BRA") | (df_prison.Iso3_code == "IND") | (df_prison.Iso3_code == "USA") | (df_prison.Iso3_code == "ZAF") | (df_prison.Iso3_code == "SWE")]

df_prison = df_prison[(df_prison.Unit == "Rate per 100,000 population")]
df_prison = df_prison[(df_prison.Dimension == "Total")]
df_prison = df_prison[(df_prison.Category == "Total")]
df_prison = df_prison[(df_prison.Indicator == "Persons held")]

fig = px.line(df_prison, x="Year", y="VALUE", color='Country')
fig.show()