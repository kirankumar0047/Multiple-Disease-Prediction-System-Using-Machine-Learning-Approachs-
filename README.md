Multiple Disease Prediction System using Machine Learning

A unified Streamlit-based web application for predicting -- Diabetes, Heart Disease, Parkinson's Disease, and Breast Cancer -- using trained machine learning models. Enhanced with a Symptom Checker Chatbot and Database Logging for real-time use cases like clinics and remote diagnostics.

Features

✅ Predicts 4 major diseases using ML
✅ Easy-to-use web interface (Streamlit)
✅ Unified layout for seamless disease selection
✅ Chatbot to assist users based on symptoms
✅ Stores all prediction logs with timestamp in SQLite
✅ View prediction history via admin-access panel
✅ Modular codebase for future enhancements

Technologies & Libraries Used

Library	Purpose
streamlit	Web app framework
streamlit-option-menu	Sidebar navigation
pickle	Load saved ML models
scikit-learn	ML model training (offline)
sqlite3	Data storage and logging
datetime	Timestamping predictions
re	Chatbot keyword handling
os	File handling (if needed)
📁 Project Structure

Multiple-Disease-Prediction-System/ │ ├── app.py # Main Streamlit application ├── models/ # Trained .sav files (ML models) │ ├── diabetes_model.sav │ ├── heart_disease_model.sav │ ├── parkinsons_model.sav │ └── breast_cancer_model.sav │ ├── chatbot/ │ ├── init.py │ └── chat.py # Symptom checker chatbot handler │ ├── db.py # SQLite DB connection & logging ├── health_predictions.db # SQLite DB (auto-created) ├── README.md └── requirements.txt

💬 Chatbot Feature

The app includes a lightweight NLP-based chatbot to assist users who are unsure which disease module to use. It guides them based on symptoms like chest pain, tremors, cough, etc.

🏥 Use Cases in Real World

Early disease screening in **rural health clinics
Patient triage in **outpatient departments
Health awareness programs via kiosks
Can evolve into smart EHR (Electronic Health Records) system
🛠 How to Run the App

Install dependencies
pip install -r requirements.txt

Launch the app streamlit run app.py
