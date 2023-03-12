import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numerize.numerize import numerize
import altair as alt
import warnings

st.set_page_config(page_title="Hospitality Atliq Grand Dashboard",
                   layout='wide',
                   initial_sidebar_state='expanded'
                   )

# Loading Dataframes cache

@st.cache_data
def get_data1():
    df1 = pd.read_csv('Dataset/dim_date.csv') 
    df1['date']= pd.to_datetime(df1['date'])
    return df1
df1 = get_data1()

def get_data2():
    df2 = pd.read_csv('Dataset/dim_hotels.csv')  
    return df2
df2 = get_data2()

def get_data3():
    df3 = pd.read_csv('Dataset/dim_rooms.csv')  
    return df3
df3 = get_data3()

def get_data4():
    df4 = pd.read_csv('Dataset/fact_aggregated_bookings.csv')  
    return df4
df4 = get_data4()

def get_data5():
    df5 = pd.read_csv('Dataset/fact_bookings.csv')  
    return df5
df5 = get_data5()

header_left, header_mid, header_right = st.columns([1, 2, 1], gap='large')

with header_mid:
    st.markdown(
        "<h1 style='text-align: center;'>Hospitality Atliq Dashboard</h1>",
        unsafe_allow_html=True,
    )
df = pd.concat([df1, df2, df3, df4,df5], axis = 0)

df5["revenue_realized"] = df5["revenue_realized"] * 73.9
total_revenue = float(df5['revenue_realized'].sum())
total_bookings = float(df5["booking_id"].nunique())
total_average_ratings = round(df5['ratings_given'].mean(), 2)
total_capacity = float(df4["capacity"].sum())
total_successful_bookings = float(df4["successful_bookings"].sum())
total_occupation = round(100*total_successful_bookings/total_capacity,2) 


total1,total2,total3,total4,total5,total6 = st.columns(6,gap='large')

with total1:
    st.image('images/money-bag.gif',use_column_width='Auto',width=100)
    st.metric(label='Total Revenue', value=numerize(total_revenue))
with total2:
    st.image('images/shopping-cart.gif',use_column_width='Auto',width=100)
    st.metric(label='Total Bookings', value=numerize(total_bookings))

with total3:
    st.image('images/rating.gif',use_column_width='Auto',width=100)
    st.metric(label= 'Total Ratings',value=numerize(total_average_ratings,2))

with total4:
    st.image('images/rate.gif',use_column_width='Auto',width=100)
    st.metric(label='Total Capacity',value=numerize(total_capacity))

with total5:
    st.image('images/analytical-skill.gif',use_column_width='Auto',width=100)
    st.metric(label='Total Successful Bookings',value=numerize(total_successful_bookings))

with total6:
    st.image('images/discount.gif',use_column_width='Auto',width=100)
    st.metric(label='Total Occupancy',value=numerize(total_occupation))


st.markdown('''
<style>
/*center metric label*/
[data-testid="stMetricLabel"] > div:nth-child(1) {
    justify-content: center;
}

/*center metric value*/
[data-testid="stMetricValue"] > div:nth-child(1) {
    justify-content: center;
}
</style>
''', unsafe_allow_html=True)



# Split the page into two columns
Q1, Q2 = st.columns(2)

# First column - Number of Bookings by City
with Q1:
    # Merge the dataframes
    merged_df = pd.merge(df2, df5, on="property_id", validate="one_to_many")





    
    
















