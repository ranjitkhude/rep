import streamlit as st
st.set_page_config(
    page_title="Price Predictor",
    page_icon="💻",
)
st.write("# Welcome to Laptop Price Predictor 👨‍💻")
st.markdown(
    """
    Are you tired of browsing endless pages online trying to find the perfect laptop that fits your budget? Look no further! Our price predictor will help you find the best laptop for your budget.

    Simply enter your budget and desired specifications, such as screen size, RAM, storage, and processor speed, and our algorithm will predict the best laptop for you.

    We constantly update our database with the latest laptops on the market, so you can be sure that our predictions are accurate and up-to-date.

    Our goal is to help you save time and money by providing you with personalized recommendations based on your preferences and budget.

    Start predicting now and find your dream laptop!

    Note :- This prediction is purely based on various Data and Algorithms
"""
)


import pandas as pd
import streamlit as st
import pickle
import numpy as np



page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=820&q=80");
background-size: 150%;

background-repeat: no-repeat;
background-attachment: local;
}}
</style>

"""




st.markdown(page_bg_img, unsafe_allow_html=True)
# Define the main function


# Security
#passlib,hashlib,bcrypt,scrypt


# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))




st.title("Laptop Predictor")

# brand
company = st.selectbox('Brand',df['Company'].unique())

# type of laptop
type = st.selectbox('Type',df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
ips = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',df['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))

