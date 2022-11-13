import streamlit as st
import pandas as pd
import numpy as np
import math
import statistics

st.set_page_config(
    page_title="Home Page",
    page_icon="🟢"
)
#st.title("")
#st.sidebar.success("Choose a page")

st.markdown("## Basic Information of our data Set")
st.markdown("#### Head of our Dataset")
df=pd.read_csv("data/Open_Pub.csv")
st.dataframe(df.head())
st.markdown("#### Tail of our Dataset")
st.dataframe(df.tail())
st.markdown("#### Shape of our Dataset")
st.dataframe(df.shape)
st.markdown("#### Columns of our Dataset")
st.dataframe(df.columns)
st.markdown("#### Correlation of our Dataset")
st.dataframe(df.corr())
st.markdown("#### Covarience of our Dataset")
st.dataframe(df.cov())