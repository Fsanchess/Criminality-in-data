import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib
import matplotlib.pyplot as plt

st.title('Evolution de la criminalité par pays selon différents critères sociaux de 2000 à 2020')

lis = ['AUS','BRA','IND','SWE','USA','ZAF']
lis2 = ['AU','BR','IN','SE','US','ZA']

@st.cache
def load_data2(nrows):
    data2 = pd.read_csv('Dataset/world_latitude_and_longitude_values.csv', nrows=nrows)
    data2 = data2[data2['country_code'].isin(lis2)]
    data2.latitude = pd.to_numeric(data2.latitude, errors='coerce')
    data2.longitude = pd.to_numeric(data2.longitude, errors='coerce')
    return data2

latitude_and_longitude = load_data2(2000)

st.subheader('Map')
st.map(latitude_and_longitude)

@st.cache
def load_data(nrows):
    data = pd.read_csv('Dataset/education_tertiary_25-64.csv', nrows=nrows)
    data1 = data[data['LOCATION'].isin(lis)]
    return data1

education_tertiary = load_data(2000)

st.subheader('Tertiary education Data')
st.write(education_tertiary)
#Bar Chart
st.bar_chart(education_tertiary['Value'])


