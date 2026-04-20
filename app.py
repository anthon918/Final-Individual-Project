import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Page title
st.title("📊 Retail Sales Forecasting App")
st.write("Predict weekly store-level sales using historical data")

# -------------------------
# USER INPUTS
# -------------------------

st.sidebar.header("Input Features")

store = st.sidebar.number_input("Store ID", min_value=1, max_value=50, value=1)

month = st.sidebar.slider("Month", 1, 12, 1)

week = st.sidebar.slider("Week Number", 1, 52, 1)

holiday = st.sidebar.selectbox("Is Holiday?", ["No", "Yes"])
holiday = 1 if holiday == "Yes" else 0

cpi = st.sidebar.number_input("CPI", value=200.0)

unemployment = st.sidebar.number_input("Unemployment Rate", value=7.0)

fuel = st.sidebar.number_input("Fuel Price", value=3.0)

# -------------------------
# CREATE INPUT DATAFRAME
# -------------------------

input_data = pd.DataFrame({
    "Store": [store],
    "Month": [month],
    "Week": [week],
    "IsHoliday": [holiday],
    "CPI": [cpi],
    "Unemployment": [unemployment],
    "Fuel_Price": [fuel]
})

# Show input summary
st.subheader("Input Summary")
st.write(input_data)

# -------------------------
# PREDICTION
# -------------------------

if st.button("Predict Weekly Sales"):
    prediction = model.predict(input_data)

    st.subheader("Prediction Result")
    st.success(f"💰 Predicted Weekly Sales: ${prediction[0]:,.2f}")
