import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import os
import joblib
import time
import datetime
import base64
from PIL import Image

st.set_page_config(layout="wide", page_title="Wildfire_Ca") #sets the page to a wide layout and adds title to the app 
                      
#Add sidebar to the app
st.sidebar.markdown("### My first Awesome App")
st.sidebar.markdown("Welcome to my first app. This app is built using Streamlit and uses data source from Athletic.net. I hope you enjoy!")

#Add title and subtitle to the main interface of the app
st.title("")
st.markdown("")

# add two tabs for different purposes
tab1, tab2 = st.tabs(["",""])

#start of tab 1
with tab1:
    
    #Create two columns/filters
    col1, col2= st.columns(2)
    with col1:
        
    with col2:
           
    col3, col4 = st.columns(2)
            
    with col3: 
        
with tab2:
    
    col5, col6 = st.columns(2)
    
    with col5:         
            
    with col6: