import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# App Configuration
st.set_page_config(page_title="PBM Optimization", page_icon="💊", layout="centered")

# Centered Title
st.markdown("<h1 style='text-align:center;'>PBM Optimization</h1>", unsafe_allow_html=True)
st.write("---")

# Dropdown for navigation
option = st.selectbox(
    "Select Option",
    [
        "Choose an option",
        "Real Time Formulary Impact Analysis",
        "Therapeutic Equivalence Optimization",
        "Drug Utilization Trend Prediction"
    ]
)

if option == "Real Time Formulary Impact Analysis":
    switch_page("formulatory")
elif option == "Therapeutic Equivalence Optimization":
    switch_page("equivalence")
elif option == "Drug Utilization Trend Prediction":
    switch_page("trendprediction")





