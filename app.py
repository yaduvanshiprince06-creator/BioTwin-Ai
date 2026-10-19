import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="BioTwin AI",
    page_icon="🧬",
    layout="wide" 
)

# Header
st.title("🧬 BioTwin AI")
st.subheader("Digital Twin for Personalized Health Monitoring")

st.write(
    "A healthcare prototype for exploring patient health "
    "parameters through simulated data."
)

st.info(
    "Educational prototype: all measurements are simulated. "
    "This application does not provide medical diagnoses."
)

# Sidebar
st.sidebar.header("Patient Profile")

patient_id = st.sidebar.selectbox(
    "Select Patient",
    ["BT-001", "BT-002", "BT-003"]
)

patient_age = st.sidebar.slider(
    "Patient Age",
    min_value=18,
    max_value=90,
    value=24
)

st.sidebar.caption("Demo mode: simulated patient data")

# Generate reproducible demo measurements
seed_value = sum(ord(c) for c in patient_id)
random.seed(seed_value)

heart_rate = random.randint(65, 95)
glucose = random.randint(80, 125)
activity = random.randint(30, 95)
sleep = round(random.uniform(5.0, 9.0), 1)

# Patient information
st.header("Patient Digital Twin")

col1, col2, col3 = st.columns(3)

col1.metric("Patient ID", patient_id)
col2.metric("Age", f"{patient_age} years")
col3.metric("Twin Status", "Initialized")

# Health measurements
st.header("Simulated Health Measurements")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Heart Rate", f"{heart_rate} BPM")
c2.metric("Blood Glucose", f"{glucose} mg/dL")
c3.metric("Activity Score", f"{activity}/100")
c4.metric("Sleep Duration", f"{sleep} hours")

# Data table
st.header("Health Data Overview")

data = pd.DataFrame({
    "Parameter": [
        "Heart Rate",
        "Blood Glucose",
        "Activity",
        "Sleep"
    ],
    "Value": [
        heart_rate,
        glucose,
        activity,
        sleep
    ],
    "Unit": [
        "BPM",
        "mg/dL",
        "Score / 100",
        "Hours"
    ]
})

st.dataframe(data, use_container_width=True)

# Visualization
st.header("Measurement Visualization")

chart_data = pd.DataFrame({
    "Measurement": [
        "Heart Rate",
        "Glucose",
        "Activity",
        "Sleep"
    ],
    "Value": [
        heart_rate,
        glucose,
        activity,
        sleep
    ]
})

st.bar_chart(
    chart_data,
    x="Measurement",
    y="Value"
)

# Informational summary
st.header("Digital Twin Summary")

st.write(
    f"The digital twin for {patient_id} currently displays "
    f"a simulated heart rate of {heart_rate} BPM, "
    f"glucose measurement of {glucose} mg/dL, "
    f"activity score of {activity}/100, and "
    f"sleep duration of {sleep} hours."
)

st.warning(
    "These values are randomly generated for demonstration. "
    "They must not be interpreted as real patient measurements "
    "or used to make healthcare decisions."
)

# Future development
with st.expander("Future Development"):
    st.markdown("""
    - Integration with wearable health sensors
    - Historical health data and trend analysis
    - Validated machine-learning models
    - Personalized digital twin simulations
    - Secure patient data management
    """)

st.caption(
    "BioTwin AI | Digital Twin Challenge Project | "
    "Prototype Version 1.0"
)