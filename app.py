import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model and label encoder
model = pickle.load(open("model.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

# Streamlit UI
st.title("🌱 AI-Based Crop Recommendation System")
st.write("Enter the soil and climate conditions to get the best crop suggestion.")

# User Inputs
N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=40)
K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=40)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=70.0)
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=150.0)

# Prediction Button
if st.button("Predict Crop"):
    # Prepare features for prediction
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(features)
    
    # Decode the crop name
    predicted_crop = label_encoder.inverse_transform(prediction)[0]
    
    st.success(f"🌾 Recommended Crop: **{predicted_crop}**")