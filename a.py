import streamlit as st
import joblib
import numpy as np
import pandas as pd
model = joblib.load('stacking_regressor_model.pkl')
expected_columns = ['RAM', 'ROM', 'Back Camera', 'Front_Camera', 'Battery', 'Processor_Brand', 'Phone Name']

st.title('Mobile Price Prediction')

st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;
        }
        .title {
            color: #0e4b6e;
            text-align: center;
        }
        .stTextInput, .stNumberInput {
            background-color: #e7f7f8;
        }
        .stButton>button {
            background-color: #005fa3;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.subheader('Please enter the details of the mobile to predict the price:')
phone_name = st.text_input('Phone Name')  # Input field for Phone Name
ram = st.number_input('RAM (in GB)', min_value=1)
rom = st.number_input('ROM (in GB)', min_value=8)
back_camera = st.number_input('Back Camera (in MP)', min_value=1)
front_camera = st.number_input('Front Camera (in MP)', min_value=1)
battery = st.number_input('Battery (in mAh)', min_value=1000)
processor_brand = st.text_input('Processor Brand (Qualcomm, MediaTek, Exynos, Unisoc, Generic (Unbranded), Google Tensor, Kirin)')
input_data = pd.DataFrame({
    'Phone Name': [phone_name],  # Include 'Phone Name' as part of the input
    'RAM': [ram],
    'ROM': [rom],
    'Back Camera': [back_camera],
    'Front_Camera': [front_camera],
    'Battery': [battery],
    'Processor_Brand': [processor_brand]  # Only Processor Brand here
})
if st.button('Predict Price'):
    prediction = model.predict(input_data)  # The model expects the processor brand and phone name as categorical features
    st.subheader(f'Phone Name: {phone_name}')  # Display the Phone Name
    st.subheader(f'Predicted Price: ₹{prediction[0]:,.2f}')
