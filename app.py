import streamlit as st

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
    st.switch_page("formulatory.py")
elif option == "Therapeutic Equivalence Optimization":
    st.switch_page("equivalence.py")
elif option == "Drug Utilization Trend Prediction":
    st.switch_page("trendprediction.py")




