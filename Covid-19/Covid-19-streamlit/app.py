import streamlit as st 
import base64
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt 
import tensorflow as tf 
import keras
from keras_preprocessing import image
#from tf.keras.utils import load_img, img_to_array 
#from keras.preprocessing import image


st.header("Upload Your's X-Ray Image To Detect Covid-19")
image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
def load_image(image_file):
    img = Image.open(image_file)
    return img
if image_file is not None:
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    file_name=list(file_details.values())
    img_name=file_name[0]
    img = load_image(image_file)
    with open(os.path.join("./images/",image_file.name),"wb") as f: 
      f.write(image_file.getbuffer())         
    st.success("Saved")

clk=st.button("Predict")
model=tf.keras.models.load_model('./models/covid_19.h5') 

if clk: 
    path = "./images/{}".format(img_name)
    img = keras.utils.load_img(path, target_size=(224,224))
    #imgplot = plt.imshow(img)
    x = image.img_to_array(img)
    img_test = np.expand_dims(x, axis=0)
    classes = model.predict(img_test, batch_size=10)
    if (int(classes[0][0]) == 0):
        st.write(" You are Covid +ve 🤔")
    elif (int(classes[0][0]) == 1):
        st.write(" You are Normal 🤗")
    else:
        st.write("Can't Recognize")
    st.image(img)    

