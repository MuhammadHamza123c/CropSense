import streamlit as st
import joblib
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_model = os.path.join(script_dir, "crops_pred.joblib")
file_path_scaler=os.path.join(script_dir,'scaler.joblib')

model = joblib.load(file_path_model)
scaler = joblib.load(file_path_scaler)

st.set_page_config(page_title="CropSense 🌱", page_icon="🌾", layout="centered")
st.title("🌱 CropSense – Smart Crop Recommendation")

N = st.number_input("Nitrogen (mg/kg)", min_value=0.0, max_value=150.0, value=90.0)
P = st.number_input("Phosphorus (mg/kg)", min_value=5.0, max_value=100.0, value=40.0)
K = st.number_input("Potassium (mg/kg)", min_value=5.0, max_value=90.0, value=45.0)
temperature = st.number_input("Temperature (°C)", min_value=10.0, max_value=45.0, value=30.0)
humidity = st.number_input("Humidity (%)", min_value=10.0, max_value=100.0, value=25.0)
ph = st.number_input("Soil pH", min_value=4.0, max_value=10.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=20.0, max_value=280.0, value=120.0)

if st.button("🌾 Recommend Crop"):
    data_raw = {
        'Nitrogen': N,
        'Phosphorus': P,
        'Potassium': K,
        'temperature': temperature,
        'humidity': humidity,
        'pH': ph,
        'rainfall': rainfall
    }
    data_raw = pd.DataFrame([data_raw])
    scaler_raw = scaler.transform(data_raw)
    predict_it = model.predict(scaler_raw)[0]
    st.success(f"✅ Recommended Crop: **{predict_it.capitalize()}**")

st.markdown("---")
st.sidebar.title(" 🌿 Crops List")

crops = [
    "Rice", "Maize", "Jute", "Cotton", "Coconut", "Papaya", "Orange",
    "Apple", "Muskmelon", "Watermelon", "Grapes", "Mango", "Banana",
    "Pomegranate", "Lentil", "Blackgram", "Mungbean", "Mothbeans",
    "Pigeonpeas", "Kidneybeans", "Chickpea", "Coffee"
]

for crop in crops:
    st.sidebar.markdown(f"# ✅ **{crop}**")

st.markdown("---")
st.markdown(" #### **Made with 💕👨🏻‍💻 by Hamza**")
