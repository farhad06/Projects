import streamlit as st 
import pickle
from base64 import standard_b64decode
import numpy as np
import sklearn

carat = st.number_input("Enter the carat of the diamond: ", min_value=0.2, max_value=5.01)
cut = st.number_input("Enter the cut details of the diamond:" , min_value= 1, max_value=5)
color = st.number_input("Enter the color details of the diamond:" , min_value= 1, max_value= 7)
clarity = st.number_input("Enter the clarity details of the diamond:" , min_value= 1, max_value= 8)

depth = st.number_input("enter the depth of the diamond: ", min_value= 43, max_value= 79)

table = st.number_input("Enter the table dimmension of the diamond: ", min_value= 43, max_value= 95)

x = st.number_input("Enter the x dimension of the diamond in mm: ", min_value= 0.0, max_value= 10.74)

y = st.number_input("Enter the y dimmensions of the diamond in mm: ", min_value= 0.0, max_value= 58.9)

z = st.number_input("Enter the z dimmensions of the diamond in mm: ", min_value= 0.0, max_value= 31.8)
click = st.button("Predict")

#rfr_model = pickle.load(open("models/random_forest_regression_model.pkl", "rb"))
rfr_model=pickle.load(open("models/linear_regression_model.pkl","rb"))
standard_scaler = pickle.load(open("models/standard_scaler.pkl", "rb"))

if click == True:
    if carat and cut and color and clarity and depth and table and x and y and z:
        categorical_data = [[cut, color, clarity]]
        numerical_data = [[carat, depth, table, x, y, z]]
        standard_data = standard_scaler.transform(numerical_data)
        final_data = np.concatenate((standard_data, categorical_data), axis=1)
        prediction = rfr_model.predict(final_data)
        st.success("The price of the diamond in USD  is: " + str(prediction[0]))
    else:
        st.error("Enter the values properly.")