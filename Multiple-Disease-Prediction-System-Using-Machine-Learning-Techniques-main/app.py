import streamlit as st
from streamlit_option_menu import option_menu
import pickle

# Importing chatbot and database functions
from chatbot.chat import chatbot_response
from database.db import store_prediction, fetch_all_predictions

# Load models
diabetes_model = pickle.load(open('models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('models/parkinsons_model.sav', 'rb'))
breast_cancer_model = pickle.load(open('models/breast_cancer_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction',
                            'Symptom Checker Chatbot',
                            'View Prediction History'],
                           icons=['activity', 'heart', 'person', 'gender-female', 'chat', 'table'],
                           default_index=0)

# ==============================
# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            diab_prediction = diabetes_model.predict([input_data])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic.\nVisit Apollo Hospital, Madurai: Dr. PG Raman (Diabetologist)'
            else:
                diab_diagnosis = 'The person is not diabetic. Stay healthy and eat well.'

            st.success(diab_diagnosis)
            store_prediction('Diabetes', input_data, diab_diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

# ==============================
# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Type')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting ECG results')
    with col2:
        thalach = st.text_input('Max Heart Rate')
    with col3:
        exang = st.text_input('Exercise induced angina')
    with col1:
        oldpeak = st.text_input('Oldpeak')
    with col2:
        slope = st.text_input('Slope')
    with col3:
        ca = st.text_input('Number of major vessels (0-3)')
    with col1:
        thal = st.text_input('Thal')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [float(age), float(sex), float(cp), float(trestbps),
                          float(chol), float(fbs), float(restecg), float(thalach),
                          float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
            heart_prediction = heart_disease_model.predict([input_data])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease. Visit Dr. Selvamani at Meenakshi Mission Hospital.'
            else:
                heart_diagnosis = 'No signs of heart disease detected. Stay active and healthy.'

            st.success(heart_diagnosis)
            store_prediction('Heart Disease', input_data, heart_diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

# ==============================
# Parkinson’s Disease Prediction
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    features = [
        'fo', 'fhi', 'flo', 'Jitter_percent', 'Jitter_Abs', 'RAP', 'PPQ', 'DDP',
        'Shimmer', 'Shimmer_dB', 'APQ3', 'APQ5', 'APQ', 'DDA', 'NHR', 'HNR',
        'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]
    values = []
    for i in range(0, len(features), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(features):
                with cols[j]:
                    val = st.text_input(features[i + j])
                    values.append(val)

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        try:
            input_data = [float(x) for x in values]
            parkinsons_prediction = parkinsons_model.predict([input_data])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "Possible Parkinson’s detected. Please consult Dr. Justin (Neurologist), Madurai."
            else:
                parkinsons_diagnosis = "No signs of Parkinson’s. Stay safe and well."

            st.success(parkinsons_diagnosis)
            store_prediction('Parkinsons', input_data, parkinsons_diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

# ==============================
# Breast Cancer Prediction
if selected == "Breast Cancer Prediction":
    st.title("Breast Cancer Prediction using ML")
    features = [
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
        'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
        'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
        'compactness_se', 'concavity_se', 'concave_points_se', 'symmetry_se', 'fractal_dimension_se',
        'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst'
    ]
    values = []
    for i in range(0, len(features), 5):
        cols = st.columns(5)
        for j in range(5):
            if i + j < len(features):
                with cols[j]:
                    val = st.text_input(features[i + j])
                    values.append(val)

    breast_cancer_diagnosis = ''
    if st.button("Breast Cancer Test Result"):
        try:
            input_data = [float(x) for x in values]
            breast_cancer_prediction = breast_cancer_model.predict([input_data])
            if breast_cancer_prediction[0] == 1:
                breast_cancer_diagnosis = "Warning: Breast cancer signs detected. Visit Dr. S.G. Balamurugan, Madurai."
            else:
                breast_cancer_diagnosis = "No signs of breast cancer detected. Stay healthy."

            st.success(breast_cancer_diagnosis)
            store_prediction('Breast Cancer', input_data, breast_cancer_diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

# ==============================
# Chatbot Symptom Checker
if selected == "Symptom Checker Chatbot":
    st.title("🩺 Symptom Checker Chatbot")
    st.write("Describe your symptoms and I'll suggest possible health insights:")

    user_input = st.text_input("Enter your symptoms (e.g., 'I have chest pain and fatigue')")
    if st.button("Get Response"):
        response = chatbot_response(user_input)
        st.success(response)

# ==============================
# View Prediction History
if selected == "View Prediction History":
    st.title("📊 Prediction History")
    data = fetch_all_predictions()
    if data:
        st.write("Here are your past predictions:")
        st.dataframe(data, use_container_width=True)
    else:
        st.info("No predictions stored yet.")