import streamlit as st

st.set_page_config(page_title="Respiratory Symptom Diagnosis", layout="wide")

st.title("🫁 Respiratory Symptom Diagnosis Portal")

page = st.sidebar.radio("Navigation", ["New Diagnosis", "Past Reports"])

if page == "New Diagnosis":
    st.markdown("Enter patient and clinical encounter details below to calculate the Disease Probability Score.")

    tab1, tab2, tab3, tab4 = st.tabs([
        "Patient & Encounter",
        "Symptoms & Cough",
        "Breath Sounds",
        "History & Exposure"
    ])

    with tab1:
        st.header("Patient Information")
        col1, col2 = st.columns(2)
        with col1:
            patient_name = st.text_input("Name")
            patient_dob = st.date_input("Date of Birth")
        with col2:
            patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        st.header("Clinical Encounter")
        encounter_type = st.selectbox("Encounter Type", ["Initial Visit", "Follow-up", "Emergency"])
        encounter_date = st.date_input("Encounter Date")

    with tab2:
        st.header("Respiratory Symptoms")
        symptom_type = st.text_input("Symptom Type (e.g., Shortness of breath, Chest pain)")

        st.header("Cough Characteristics")
        cough_type = st.selectbox("Cough Type", ["None", "Dry", "Productive", "Chronic", "Barking"])

    with tab3:
        st.header("Breath Sounds Assessment")
        col1, col2 = st.columns(2)
        with col1:
            sound_location = st.text_input("Location (e.g., Left lower lobe)")
            sound_type = st.selectbox("Sound Type", ["Normal", "Wheeze", "Crackle", "Stridor", "Rhonchi"])
        with col2:
            intensity = st.selectbox("Intensity", ["Normal", "Decreased", "Absent"])
            pitch = st.selectbox("Pitch", ["Low", "Medium", "High"])

    with tab4:
        st.header("Smoking History")
        col1, col2 = st.columns(2)
        with col1:
            smoking_status = st.selectbox("Smoking Status", ["Never", "Current", "Former"])
            packs_per_day = st.number_input("Packs per Day", min_value=0.0, step=0.5)
        with col2:
            years_smoked = st.number_input("Years Smoked", min_value=0.0, step=1.0)
            quit_date = st.date_input("Quit Date (if applicable)", value=None)

        st.header("Environmental Exposure")
        col3, col4 = st.columns(2)
        with col3:
            exposure_type = st.text_input("Exposure Type (e.g., Dust, Chemicals, None)")
            setting = st.text_input("Setting (e.g., Workplace, Home)")
        with col4:
            duration = st.text_input("Duration (e.g., 5 years, 2 months)")

    st.divider()
    st.button("Submit Encounter & Calculate Score", type="primary")

elif page == "Past Reports":
    st.header("Past Diagnostic Reports")
    st.info("Reports section coming soon.")