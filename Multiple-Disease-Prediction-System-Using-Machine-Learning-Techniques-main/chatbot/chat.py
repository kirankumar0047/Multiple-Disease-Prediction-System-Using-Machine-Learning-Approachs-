import re

# Dummy symptom-to-disease mapping
SYMPTOM_DISEASE_MAP = {
    'fever': 'You might be having a viral infection. Please monitor your temperature.',
    'headache': 'Persistent headache could be a sign of migraine or stress.',
    'cough': 'It might be a common cold, but if it persists, consult a doctor.',
    'chest pain': 'Chest pain can indicate heart issues. Visit a cardiologist immediately.',
    'tremor': "Tremors can be a symptom of Parkinson's. Please get checked.",
    'weight loss': 'Sudden weight loss may relate to diabetes or thyroid issues.',
    'fatigue': 'This may be due to anemia, diabetes, or lifestyle factors.',
    'throat pain': 'This could be a throat infection or early flu symptom.',
}

def chatbot_response(user_input: str) -> str:
    user_input = user_input.lower()

    # Search for known symptoms
    for symptom, response in SYMPTOM_DISEASE_MAP.items():
        if re.search(r'\b' + re.escape(symptom) + r'\b', user_input):
            return response

    return "I'm not sure about that symptom. Please provide more details or consult a medical professional."