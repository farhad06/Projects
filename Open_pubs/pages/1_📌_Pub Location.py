import streamlit as st 
import pandas as pd
import numpy as np

st.title("Pubs Location In Maps")
df=pd.read_csv("./data/Open_Pub.csv")
#st.dataframe(df.head())
location=df[["latitude","longitude"]]
#st.write(location)
st.map(location)
