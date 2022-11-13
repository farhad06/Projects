from enum import auto
from token import N_TOKENS
import streamlit as st 
import pandas as pd
import numpy as np
import math,statistics
#import seaborn as sns
import base64

st.title("Welcome to Dimmond Price Prediction Website")
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://wallpaperaccess.com/full/2464096.jpg")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnzGpD8ph5T6HGTChXoNs5_LA60Wf7mgenTQ&usqp=CAU",width=700)

##import dataset
df=pd.read_csv("./data/diamonds.csv")

##st.write("Show Your Dataset")

data=st.radio('Show Your Dataset',('Head','Tail'),horizontal=True)
if data=='Head':
    st.write(df.head())
elif data=='Tail':
    st.write(df.tail())
else:
    st.write("Select Any Radio Button To Show Data")
sta=st.selectbox("Show Some Information of Our Dataset",('Shape','Data Types','Statical Description','Correlation','Covariance','Columns'))
if sta=='Shape':
    st.write(df.shape)
elif sta== 'Data Types':
    st.write(df.info())
elif sta=='Statical Description':
    st.write(df.describe())
elif sta=='Correlation':
    st.write(df.corr())
elif sta=='Covariance':
    st.write(df.cov())
elif sta=='Columns':
    st.write(df.columns)                              
st.subheader("Some Bar Plot for Our Dataset")
plot=st.radio('Choose Any Button To Show Bar Plot',('Cut','Clarity','Color'),horizontal=True)
if plot=='Cut':
    st.bar_chart(df['cut'].value_counts())
elif plot=='Clarity':
    st.bar_chart(df['clarity'].value_counts())
elif plot=='Color':
    st.bar_chart(df['color'].value_counts())        