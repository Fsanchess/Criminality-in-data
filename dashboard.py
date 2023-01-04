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


# Definition 'Number of victims of intentional homicide'
st.markdown("<p style= color: dark grey><font size='4'>L'indicateur est défini comme le nombre total de victimes d'homicide intentionnel divisé par la population totale, exprimé pour 100 000 habitants.<br>L'homicide intentionnel est défini comme la mort illégale infligée à une personne avec l'intention de causer la mort ou des blessures graves (Source : Classification internationale des crimes à des fins statistiques, CIEC 2015).<br>La population fait référence à la population résidente totale dans un pays donné au cours d'une année donnée.<br><br></font></p>", unsafe_allow_html=True)


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


st.markdown("<p style= color: dark grey><font size='4'><br><br>Les nombres d'homicides volontaires pour 100 000 habitants varient considérablement d'un pays à l'autre. Bien qu'il y ait rarement une raison claire pour laquelle des crimes sont commis, de nombreux facteurs peuvent affecter les taux de criminalité.</font></p>", unsafe_allow_html=True)

st.markdown("<p style= color: dark grey><font size='4'>Les pays ayant des taux de criminalité élevés ont généralement des niveaux de pauvreté élevés et une faible disponibilité d'emplois, des conditions susceptibles de forcer les gens à adopter des solutions plus risquées, plus désespérées et moralement discutables (qui sont souvent rendues possibles par des organismes d'application de la loi sous-développés). Les taux de criminalité ont tendance à être plus faibles dans les pays où les conditions de vie sont favorables (riches), l'application de la loi par la police et des peines sévères pour les crimes.</font></p>", unsafe_allow_html=True)


st.markdown("<p style= color: dark grey><font size='4'><br>Ces taux de criminalité seront comparés avec divers paramètres sociaux et 6 pays avec des caractéristiques différents ont été choisis pour la suite de l'analyse (développés/non développés, nord/sud, de tous les continents) : Australia (AUS), Brazil (BRA), India (IND), Sweden (SWE), United States of America (USA), South Africa (ZAF).<br></font></p>", unsafe_allow_html=True)



# Chart with homicide dataset
pd2_homicide = homicide_dataset[homicide_dataset['Iso3_code'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF'])]
pd2_homicide = pd2_homicide.loc[pd2_homicide['Unit of measurement'] == 'Rate per 100,000 population']
pd2_homicide = pd2_homicide[pd2_homicide['Year'].isin([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])]
homicide_chart = px.bar(pd2_homicide, x="Year", y="VALUE", color="Iso3_code",
                         title = 'Crime par pays',
                         category_orders={"Iso3_code": ["AUS", "BRA", "IND", "SWE","USA","ZAF"]},
                         labels={
                            "Year" : "Année",
                            "VALUE" : "Nb crimes pour 100 000 habitants",
                            "Iso3_code" : "Pays"
                         })

# Display chart with homicide dataset
title_homicide_chart = st.header('Evolution du taux de criminalité')
plot_homicide_chart =st.plotly_chart(homicide_chart, use_container_width=True)



# Charts with unemployment dataset
unemployment_path = 'dataset_clean/unemployment_clean.csv'
unemployment_dataset = pd.read_csv(unemployment_path, sep = ';')
pd_unemployment = unemployment_dataset[unemployment_dataset['Country Code'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]
unemployment_chart = px.line(pd_unemployment, x="Year", y="Value", color="Country Code", markers=True,
                         title = 'Chômage par pays',
                         category_orders={"Country Code": ["AUS", "BRA", "IND", "SWE","USA","ZAF"]},
                         labels={
                            "Year" : "Année",
                            "Value" : "Taux de chômage",
                            "Country Code" : "Pays"
                         })

# Display charts with unemployment dataset
#title_unemployment_chart = st.header("Evolution du taux de chômage")
#plot_unemployment_chart =st.plotly_chart(unemployment_chart, use_container_width=True)



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
   st.header("Evolution du taux de chômage")
   st.plotly_chart(unemployment_chart, use_container_width=True)
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



# Charts with happiness dataset
happiness_path = 'dataset_clean/happiness-cantril-ladder.csv'
happiness_dataset = pd.read_csv(happiness_path, sep = ',')
pd_happiness = happiness_dataset[happiness_dataset['Code'].isin(['AUS', 'BRA', 'IND', 'SWE', 'USA', 'ZAF']) ]

happiness_chart = px.line(pd_happiness, x="Year", y="Life satisfaction in Cantril Ladder (World Happiness Report 2022)", color="Code", markers=True,
                         title = 'Bonheur et satisfaction',
                         category_orders={"Code": ["AUS", "BRA", "IND", "SWE","USA","ZAF"]},
                         labels={
                            "Year" : "Année",
                            "Life satisfaction in Cantril Ladder (World Happiness Report 2022)" : "Score de bonheur",
                            "Code" : "Pays"
                         })

# Display charts with happiness dataset
title_happiness_chart = st.header("Score de bonheur et satisfaction de vie, de 0 à 10")
plot_happiness_chart =st.plotly_chart(happiness_chart, use_container_width=True)



# Sources
st.markdown("<p style= color: dark grey><font size='5'>Sources</font></p>", unsafe_allow_html=True)
st.write("1. [Nombre de victimes d'homicide volontaire](https://dataunodc.un.org/dp-intentional-homicide-victims)")
st.write("2. [Nombre de personnes détenues](https://dataunodc.un.org/dp-prisons-persons-held)")
st.write("3. [Niveau d'éducation des adultes](https://data.oecd.org/eduatt/adult-education-level.htm#:~:text=There%20are%20three%20levels%3A%20below,and%20with%20more%20specialised%20teachers)")
st.write("4. [Chômage, total (% de la population active totale)](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS)")
st.write("5. [Bonheur et satisfaction](https://worldhappiness.report/ed/2022/#appendices-and-data)")



