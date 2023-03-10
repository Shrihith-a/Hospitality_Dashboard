import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numerize.numerize import numerize

st.set_page_config(page_title="Hospitality Atliq Grand Dashboard",
                   layout='wide',
                   initial_sidebar_state='expanded'
                   )

# Loading Dataframes cache

@st.cache_data
def get_data():
    df = pd.read_csv('Dataset/dim_date.csv') 
    df['date']= pd.to_datetime(df['date'])
    return df
df = get_data()

def get_data1():
    df = pd.read_csv('Dataset/dim_hotels.csv')  
    return df
df1 = get_data1()

header_left,header_mid,header_right = st.columns([1,2,1],gap='large')

with header_mid:
    st.title('Hospitality Atliq Dashboard')


