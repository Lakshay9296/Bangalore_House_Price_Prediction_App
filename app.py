import streamlit as st
import pickle
import json
import numpy as np
import streamlit_lottie as stl
st.set_page_config(page_title="Bangalore House Price Prediction", page_icon=":house:")

@st.cache_resource
def load_model(file):
    with open(file,'rb') as f:
        model = pickle.load(f)
    return model

@st.cache_resource
def load_columns(file):
    with open(file, 'r') as f:
        data = json.load(f)['data_columns']
    return data

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index =-1
    
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    
    return round(model.predict([x])[0],2)

model = load_model("model/bangalore_home_prices_model.pickle")
data_columns = load_columns("model/columns.json")
locations = data_columns[3:] 

st.sidebar.title("About the App")
st.sidebar.write("""
This web application predicts house prices in Bangalore using a pre-trained machine learning model.

The model uses **Linear Regression** to estimate house prices based on the following features:
- Location of the house
- Total square footage (area)
- Number of bedrooms (BHK)
- Number of bathrooms

The app processes the input data and utilizes a trained model to provide an accurate price prediction for homes in different parts of Bangalore.
""")

st.sidebar.write("\n")
st.sidebar.write("Hi, I'm Lakshay Kumar.")
st.sidebar.markdown("[My GitHub](https://github.com/Lakshay9296)", unsafe_allow_html=True)
st.sidebar.markdown("[My LinkedIn](https://www.linkedin.com/in/lakshay9911)", unsafe_allow_html=True)

st.title('Bangalore House Price Prediction',anchor=False)
st.write("\n")

location = st.selectbox(
    "Select a Location:", 
    options=['Other'] + locations, 
    key='location',
    help="Choose the location where the house is situated. If the location is not listed, select 'Other'."
)

area1, area2 = st.columns(2)
with area1:
    sqft = int(st.number_input(
        "Area (Square Feet)", 
        value=0, 
        key='area',
        help="Enter the total area of the house in square feet."
    ))

    bhk = int(st.select_slider(
        'BHK', 
        options=[1, 2, 3, 4, 5], 
        key='bhk',
        help="Choose the number of bedrooms (BHK) the house has."
    ))

    bath = int(st.select_slider(
        'Bathrooms', 
        options=[1, 2, 3, 4, 5], 
        key='bath',
        help="Choose the number of bathrooms in the house."
    ))

with area2:
    stl.st_lottie('https://lottie.host/8dfcb0dd-cf55-47df-9c09-090be8b04628/tBUsZgeQEo.json',width=350,speed=5,quality='high',key='image')

st.markdown("""
    <style>
    div.stButton > button:first-child {
        font-weight: bold;
        display: block;
        margin: 0 auto;
        font-size: 30px;
        padding: 15px 20px;
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

predict = st.button("Predict Price")
if predict:
    price = predict_price(location, sqft, bath, bhk)
    st.title(f"Estimated Price: ₹ {price} lakhs",anchor=False)
    
    



    
