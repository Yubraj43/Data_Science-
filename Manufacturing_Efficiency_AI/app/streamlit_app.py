import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="AI Manufacturing Dashboard", layout="wide")

st.title("🏭 AI Manufacturing Efficiency Dashboard")

# -------------------------
# Load Model
# -------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "efficiency_model.pkl")

model = joblib.load(model_path)

st.success("Model loaded successfully")

# -------------------------
# Load Dataset
# -------------------------

data_path = os.path.join(BASE_DIR, "data", "Thales_Group_Manufacturing.csv")

df = pd.read_csv(data_path)

# -------------------------
# Sidebar Filters
# -------------------------

st.sidebar.header("Dashboard Filters")

machine = st.sidebar.selectbox(
    "Select Machine ID",
    df["Machine_ID"].unique()
)

filtered_df = df[df["Machine_ID"] == machine]

# -------------------------
# Dataset Overview
# -------------------------

st.header("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Machines", df["Machine_ID"].nunique())
col3.metric("Avg Temperature", round(df["Temperature_C"].mean(),2))

# -------------------------
# Sensor Analytics
# -------------------------

st.header("📈 Sensor Analytics")

fig, ax = plt.subplots()

sns.scatterplot(
    x="Temperature_C",
    y="Error_Rate_%",
    hue="Efficiency_Status",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# -------------------------
# Feature Importance
# -------------------------

st.header("⚙ Feature Importance")

importance = model.feature_importances_
features = [
"Temperature_C",
"Vibration_Hz",
"Power_Consumption_kW",
"Network_Latency_ms",
"Packet_Loss_%",
"Quality_Control_Defect_Rate_%",
"Production_Speed_units_per_hr",
"Predictive_Maintenance_Score",
"Error_Rate_%"
]

fig2, ax2 = plt.subplots()

sns.barplot(x=importance, y=features, ax=ax2)

st.pyplot(fig2)

# -------------------------
# Efficiency Prediction
# -------------------------

st.header("🤖 Efficiency Prediction")

col1, col2, col3 = st.columns(3)

temperature = col1.slider("Temperature",20,120,60)
vibration = col2.slider("Vibration",0,100,30)
power = col3.slider("Power Consumption",0,200,80)

latency = col1.slider("Network Latency",0,100,20)
packet = col2.slider("Packet Loss",0.0,10.0,1.0)
defect = col3.slider("Defect Rate",0.0,10.0,1.0)

speed = col1.slider("Production Speed",0,500,200)
maintenance = col2.slider("Maintenance Score",0,100,50)
error = col3.slider("Error Rate",0.0,10.0,1.0)

if st.button("Predict Efficiency"):

    input_data = np.array([[
        temperature,
        vibration,
        power,
        latency,
        packet,
        defect,
        speed,
        maintenance,
        error
    ]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Efficiency: {prediction[0]}")

    st.header("📡 Real-Time Efficiency Monitoring")

df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Timestamp"])

time_df = df.sort_values("Datetime")

chart_data = time_df.groupby("Datetime")["Error_Rate_%"].mean()

st.line_chart(chart_data)

st.header("🏆 Machine Efficiency Leaderboard")

leaderboard = df.groupby("Machine_ID")["Production_Speed_units_per_hr"].mean().sort_values(ascending=False)

leaderboard_df = leaderboard.reset_index()

st.dataframe(leaderboard_df.head(10))

fig, ax = plt.subplots()

leaderboard.head(10).plot(kind="bar", ax=ax)

st.pyplot(fig)

st.header("🌐 Network Reliability Analytics")

fig, ax = plt.subplots()

sns.scatterplot(
    x="Network_Latency_ms",
    y="Packet_Loss_%",
    hue="Efficiency_Status",
    data=df,
    ax=ax
)

st.pyplot(fig)

import shap

st.header("🔍 Model Explainability (SHAP)")

explainer = shap.TreeExplainer(model)

sample = X_test.iloc[:100]

shap_values = explainer.shap_values(sample)

fig = shap.summary_plot(shap_values, sample, show=False)

st.pyplot(fig)
