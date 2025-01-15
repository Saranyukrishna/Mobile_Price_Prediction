import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('stacking_regressor_model.pkl')

expected_columns = ['RAM', 'ROM', 'Back Camera', 'Front_Camera', 'Battery', 'Processor_Brand', 'Phone Name']

st.title('Flagship Mobile Price Prediction')

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

st.subheader('Please enter the details of the flagship mobile to predict the price:')

phone_name = st.text_input('Phone Name')
ram = st.number_input('RAM (in GB)')
rom = st.number_input('ROM (in GB)')
back_camera = st.number_input('Back Camera (in MP)')
front_camera = st.number_input('Front Camera (in MP)')
battery = st.number_input('Battery (in mAh)')
processor_brand = st.text_input('Processor Brand (Qualcomm, MediaTek, Exynos, Unisoc, Generic (Unbranded), Google Tensor, Kirin)')

if st.button('Predict Price'):
    if not phone_name or not processor_brand:
        st.warning('Please fill in all fields before submitting.')
    elif ram <= 0 or rom <= 0 or back_camera <= 0 or front_camera <= 0 or battery <= 0:
        st.warning('Please ensure all numerical values are positive.')
    else:
        input_data = pd.DataFrame({
            'Phone Name': [phone_name],
            'RAM': [ram],
            'ROM': [rom],
            'Back Camera': [back_camera],
            'Front_Camera': [front_camera],
            'Battery': [battery],
            'Processor_Brand': [processor_brand]
        })

        prediction = model.predict(input_data)

        st.subheader(f'Phone Name: {phone_name}')
        st.subheader(f'Predicted Price: ₹{prediction[0]:,.2f}')
