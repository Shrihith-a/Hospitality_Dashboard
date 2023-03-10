import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
st.set_option('deprecation.showPyplotGlobalUse', False) ## Streamlit prompts an error when i insert my barchart. This removes the error

# Initialize a session state variable that tracks the sidebar state (either 'expanded' or 'collapsed').
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'expanded'

# Streamlit set_page_config method has a 'initial_sidebar_state' argument that controls sidebar state.
# Basic Page Configurations to to make GUI a little better
# Set the page title and icon
st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state,
                   page_title="Hospitality Dashboard",
                   page_icon="🎪",
                   layout="wide"
                    )

# Hide the menu button
# While this menu does contain all sorts of top-notch stuff, you might want to hide it when you deploy your app to users.
st.markdown(""" <style>
MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

# Condense the layout
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

# Custom color palette
# add .streamlit folder and add config.toml file

# Show title and description of the app.
st.title('Click the sidebar')
st.sidebar.markdown('This is an example Streamlit app to show how to expand and collapse the sidebar programmatically.')

# Toggle sidebar state between 'expanded' and 'collapsed'.
if st.button('Click to toggle sidebar state'):
    st.session_state.sidebar_state = 'collapsed' if st.session_state.sidebar_state == 'expanded' else 'expanded'
    # Force an app rerun after switching the sidebar state.
    st.experimental_rerun()

# Adding Header
st.markdown("<hr/>",unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Atliq Grands Hotel's Hospitality Data Visualization</h1>", unsafe_allow_html=True)


