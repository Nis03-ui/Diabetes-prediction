import streamlit as st
import requests

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺")

st.title("🩺 Diabetes Prediction System")
st.write("Fill in the patient details below")

# ---------------- UI ONLY (Not used in prediction) ----------------
st.subheader("Personal Information (Not used for prediction)")

gender = st.selectbox("Gender", ["Male", "Female"])
smoking_status = st.selectbox(
    "Smoking Status",
    ["never", "current", "no info", "not current", "former"]
)

st.divider()

# ---------------- Model Inputs ----------------
st.subheader("Medical Information")

age = st.number_input("Age", min_value=1, max_value=120, step=1)

hypertension = st.selectbox(
    "Hypertension",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

heart_disease = st.checkbox("Heart Disease")

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0)
hba1c = st.number_input("HbA1c Level", min_value=0.0, max_value=20.0)
blood_glucose = st.number_input(
    "Blood Glucose Level",
    min_value=50,
    max_value=400
)

# ---------------- Prediction ----------------
if st.button("Predict Diabetes"):
    payload = {
        "age": age,
        "hypertension": float(hypertension),
        "heart_disease": heart_disease,
        "bmi": bmi,
        "HbA1c_level": hba1c,
        "blood_glucose_level": blood_glucose
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            if result["Prediction"] == 1:
                st.error(f"🧪 Result: {result['result']}")
            else:
                st.success(f"🧪 Result: {result['result']}")
        else:
            st.warning("API Error: Unable to get prediction")

    except Exception as e:
        st.error(f"Connection Error: {e}")
