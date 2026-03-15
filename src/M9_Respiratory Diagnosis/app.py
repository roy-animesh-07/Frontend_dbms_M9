import streamlit as st

st.set_page_config(page_title="Respiratory Symptom Diagnosis", layout="wide")

st.title("🫁 Respiratory Symptom Diagnosis Portal")

page = st.sidebar.radio("Navigation", ["New Diagnosis", "Past Reports"])

if page == "New Diagnosis":
    st.markdown("Enter patient and clinical encounter details below to calculate the Disease Probability Score.")

elif page == "Past Reports":
    st.header("Past Diagnostic Reports")
    st.info("Reports section coming soon.")