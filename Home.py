import streamlit as st
st.set_page_config(
    page_title="Price Predictor",
    page_icon="💻",
)
st.write("# Welcome to Laptop Price Predictor 👨‍💻")
st.markdown(
    """
    Are you tired of browsing endless pages online trying to find the perfect laptop that fits your budget? Look no further! Our price predictor will help you find the best laptop for your budget.

    Simply enter your favourite brand and desired specifications, such as screen size, RAM, storage, and processor speed, and our algorithm will predict the best laptop for you.

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



