from tkinter import Button
import streamlit as st 
import pandas as pd
import numpy as np

st.title("Nearest Pubs")
df=pd.read_csv("./data/Open_Pub.csv")
location=df[["latitude","longitude"]]
lat=st.number_input("Enter Your Latitude:")
lon=st.number_input("Enter Your Longitude:")
button=st.button("SHOW PUBS")

new_location=np.array([lat,lon])
distances = np.sqrt(np.sum((new_location - location)**2, axis = 1))
n = 5
min_indices = np.argpartition(distances,n-1)[:n]
if button ==True:
    #st.text("The location corresponsing to below minimum distances : ")
    #st.dataframe(df.iloc[min_indices])
    #st.text("The minimum distances are:")
    #st.dataframe(distances.head(5))
    st.markdown("### Nearest Pubs Are")
    st.map(df.iloc[min_indices])