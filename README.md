# placement-predictor
Streamlit app to predict student placement outcomes using ML
# 🎓 Student Placement Predictor (Streamlit App)

A full-stack machine learning project that predicts whether a student will get placed based on academic, visa, and test performance data.

🔗 **Live App:** [Launch on Streamlit](https://placement-predictor.streamlit.app)  
📊 **Dashboard:** Tableau visualizations on student migration and placements

---

## 🚀 Features

- Predict student placement outcome (Placed / Not Placed)
- Input fields: GPA, Visa Status, Language Test Score, etc.
- Clean UI powered by Streamlit
- Model trained on 5,000 realistic student records (2019–2023)

---

## 📁 Tech Stack

- **Python** (pandas, scikit-learn, joblib)
- **Machine Learning:** Random Forest Classifier
- **App:** Streamlit
- **Deployment:** Streamlit Cloud
- **Data Visualization:** Tableau
- **Version Control:** Git + GitHub

---

## 🧠 Model Performance

- Accuracy: ~85%
- Confusion Matrix & Feature Importance included
- Balanced dataset with equal "Placed" and "Not Placed" classes

---

## 📦 Files

| File                  | Description                         |
|-----------------------|-------------------------------------|
| `app.py`              | Streamlit application code          |
| `placement_model.pkl` | Trained Random Forest model         |
| `model_features.pkl`  | Feature order for prediction input  |
| `clean_data.csv`      | Cleaned dataset                     |
| `requirements.txt`    | Python dependencies                 |

---

## 📌 Try It Yourself

1. Clone this repo  
2. Install requirements: `pip install -r requirements.txt`  
3. Run the app locally: `streamlit run app.py`

---

## 🤝 Credits

- Data: Synthetic student migration data (2019–2023)
- Developed by: **Srineesh Konda**
