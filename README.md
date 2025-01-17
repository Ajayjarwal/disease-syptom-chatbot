# 🩺 Disease Prediction Chatbot

A user-friendly, AI-powered chatbot for predicting diseases based on user-inputted symptoms. It utilizes Google Gemini for extracting key health indicators and a machine learning model for disease prediction, providing detailed explanations and health guidance.

---

## 🚀 Features
- **Symptom Analysis**: Extracts key health indicators from user input.  
- **Disease Prediction**: Predicts diseases using a trained KNN model.  
- **Detailed Explanation**: Provides symptoms, causes, and treatment suggestions for predicted diseases.  
- **Interactive UI**: Chat-based interface for seamless user interaction.

---

## 📖 Table of Contents
1. [API Endpoints](#api-endpoints)  
2. [Deployment Instructions](#deployment-instructions)  
3. [Usage Guidelines](#usage-guidelines)  
4. [Tech Stack](#tech-stack)  
5. [Contributing](#contributing)

---

## 📡 API Endpoints

### 1. **Home Page**
- **Endpoint:** `/`  
- **Method:** `GET`  
- **Description:** Renders the chatbot user interface.  
- **Response:** Chat interface for user input.

### 2. **Prediction Endpoint**
- **Endpoint:** `/predict`  
- **Method:** `POST`  
- **Description:** Accepts user input, extracts key values using Gemini, predicts the disease, and returns an explanation.  
- **Request Body:**

```json
{
  "message": "I have a severe headache and dizziness."
}
```
## Run Locally

Clone the project

```bash
 git clone https://github.com/your-username/disease-prediction-chatbot.git 
 cd disease-prediction-chatbot
```

Install Dependencies

```bash
  pip install -r requirements.txt
```

Set Up Environment Variables

Create a .env file to store your Google Gemini API key:
```bash
  GEMINI_API_KEY=your_google_gemini_api_key
```

Run the Application

```bash
  python app.py
```

Access the Chatbot

Visit http://127.0.0.1:5000 in your browser.


## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Machine Learning:** KNN Model (Scikit-learn)
- **AI Integration:** Google Gemini API
- **Model Serialization:** Pickle


## 🔗 Links
Ajay Jarwal
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ajay-jarwal/)


