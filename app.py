import streamlit as st

# App Configuration
st.set_page_config(page_title="Pharmacy Benefit Management Optimization", page_icon="💊", layout="centered")

# Centered Title
st.markdown("<h1 style='text-align:center;'>Pharmacy Benefit Management Optimization(PBM)</h1>", unsafe_allow_html=True)
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
    st.switch_page("pages/formulatory.py")
elif option == "Therapeutic Equivalence Optimization":
    st.switch_page("pages/equivalence.py")
elif option == "Drug Utilization Trend Prediction":
    st.switch_page("pages/trendprediction.py")


