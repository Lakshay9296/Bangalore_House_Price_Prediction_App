# Bangalore House Price Prediction

This project provides a web application for predicting house prices in Bangalore using a pre-trained machine learning model. The application is built with **Streamlit** and offers an interactive interface for users to estimate house prices based on input features such as location, area, number of bedrooms (BHK), and number of bathrooms.

## Table of Contents
- [Project Overview](#project-overview)
- [Model](#model)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)

## Project Overview
The purpose of this project is to create a web application that predicts house prices in Bangalore. The app uses a machine learning model to provide accurate price estimates based on various input parameters. Users can interact with the app to input data and receive predictions in real-time.

## Model
- The model used in this project is a **Linear Regression** model trained on a dataset of house prices in Bangalore.
- The model predicts the price based on the following features:
  - **Location**: The location of the house.
  - **Area (sqft)**: Total square feet of the house.
  - **BHK**: Number of bedrooms.
  - **Bathrooms**: Number of bathrooms.

## Demo
A live demo of the application can be found [here](https://housepricebangalore.streamlit.app/). 

You can interact with the application by selecting a location, entering the area, number of bedrooms (BHK), and number of bathrooms. The app will provide an estimated price for the house based on your inputs.

## Tech Stack
- **Backend**: Python, Linear Regression model (with `pickle`)
- **Frontend**: Streamlit
- **Libraries**:
  - `numpy` - For numerical operations.
  - `pandas` - For data handling.
  - `streamlit` - For building the web app.
  - `streamlit-lottie` - For adding Lottie animations.
  - `pickle` - For loading the pre-trained model.
  - `json` - For handling the column data.

## Project Structure
```plaintext
.
├── app.py                 # Main Streamlit app
├── bangalore_home_prices_model.pickle   # Pre-trained model
├── columns.json           # JSON file containing the columns and locations
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
