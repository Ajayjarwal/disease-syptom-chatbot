from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import pickle
import numpy as np
import json

app = Flask(__name__)

with open('best_knn_model.pkl', 'rb') as file:
    knn_model = pickle.load(file)

with open('disease_mapping.json', 'r') as file:
    disease_mapping = json.load(file)

genai.configure(api_key="YOUR_API_KEY")
model_gemini = genai.GenerativeModel("gemini-pro")

features_list = ["Fever", "Cough", "Fatigue", "Difficulty Breathing", "Blood Pressure", "Cholesterol Level"]
additional_info = ["Age", "Gender"]

def extract_key_info(user_input):
    prompt = f"""
    Extract the following details in JSON format:
    {features_list + additional_info}.
    Set missing values to null. Output only JSON.

    Input: "{user_input}"
    """
    response = model_gemini.generate_content(prompt)
    response_text = response.text.strip()

    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "").replace("```", "").strip()

    try:
        extracted_data = json.loads(response_text)
    except json.JSONDecodeError:
        return None

    for feature in features_list + additional_info:
        if feature not in extracted_data:
            extracted_data[feature] = None

    return extracted_data

def prepare_model_input(extracted_data):
    input_features = [float(extracted_data.get(feature, 0) or 0) for feature in features_list + additional_info]
    return np.array(input_features).reshape(1, -1)

def explain_disease(disease_name):
    prompt = f"""
    Provide a detailed explanation about {disease_name}, covering:
    1. Common symptoms
    2. Possible causes
    3. Recommended treatments
    4. Next steps
    """
    response = model_gemini.generate_content(prompt)
    return response.text.strip()

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.json['message']
    extracted_data = extract_key_info(user_input)

    if not extracted_data:
        return jsonify({"error": "Could not extract information. Please try again."})

    input_array = prepare_model_input(extracted_data)
    prediction = knn_model.predict(input_array)
    disease_name = disease_mapping.get(str(prediction[0]), "Unknown Disease")
    explanation = explain_disease(disease_name)

    return jsonify({
        "disease": disease_name,
        "explanation": explanation
    })

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
