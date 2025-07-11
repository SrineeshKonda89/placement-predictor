import streamlit as st
import pandas as pd
import joblib

# Load model and training feature list
model = joblib.load("placement_model.pkl")
features = joblib.load("model_features.pkl")

st.title("🎓 Student Placement Predictor")
st.markdown("Fill in the student profile below to predict placement likelihood.")

# --- User Inputs ---
gpa = st.slider("GPA or Score (2.5 to 4.0)", 2.5, 4.0, 3.0)
salary = st.number_input("Expected Starting Salary (USD)", min_value=0, max_value=150000, value=30000)
test_score = st.slider("Language Test Score (0 to 9)", 0.0, 9.0, 6.0)
scholarship = st.selectbox("Scholarship Received?", ["no", "yes"])
visa = st.selectbox("Visa Status", [
    "none", "f1", "study permit", "tier 4", "schengen student visa"
])
field = st.selectbox("Field of Study", [
    "engineering", "business", "arts", "law", "computer science", "medicine",
    "natural sciences", "social sciences"
])
course = st.selectbox("Course Name", [
    "data science", "mba", "law", "computer science", "mechanical engineering",
    "architecture", "biology", "nursing"
])
destination = st.selectbox("Destination Country", [
    "usa", "uk", "germany", "canada", "uae", "finland", "india", "russia", "south africa", "ireland"
])

# --- Initial Inputs ---
input_dict = {
    "gpa_or_score": gpa,
    "starting_salary_usd": salary,
    "test_score": test_score,
}

# --- One-Hot Encoding Logic ---
categorical_values = {
    "scholarship_received": scholarship,
    "visa_status": visa,
    "field_of_study": field,
    "course_name": course,
    "destination_country": destination
}

# Encode using exact match with training features
for col in features:
    if col in input_dict:
        continue
    found = False
    for prefix, value in categorical_values.items():
        if col == f"{prefix}_{value}":
            input_dict[col] = 1
            found = True
            break
    if not found:
        input_dict[col] = 0

# --- Prediction Logic ---
input_df = pd.DataFrame([input_dict])
input_df = input_df[features]  # ensure correct column order

if st.button("Predict Placement"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    result = "✅ Placed" if prediction == 1 else "❌ Not Placed"
    st.subheader(f"Prediction: {result}")
    st.caption(f"Confidence: {probability:.2%}")
