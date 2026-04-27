# track1_hexanova

# 🌿 AI Crop Disease Detection & Smart Advisory System

## 📌 Overview

This project is a web-based application that helps farmers and users detect crop diseases and receive actionable recommendations based on environmental conditions.

The system allows users to upload an image of a crop leaf, analyzes it using a backend service, and provides:

- Disease identification
- Weather-based insights
- Risk level assessment
- Treatment recommendations
- Step-by-step action plan

---

## 🎯 Objective

The main goal of this project is to:

- Assist farmers in early detection of crop diseases
- Provide simple, accessible, and real-time agricultural insights
- Reduce dependency on manual inspection and expert availability
- Improve crop productivity through timely decisions

---

## 🚀 Features

- 📷 Upload crop image
- 🔍 Disease detection (currently simulated, extendable to ML models)
- 🌡 Temperature & 💧 Humidity analysis
- ⚠ Risk level prediction
- 💊 Recommendation for treatment
- 📅 Day-wise action plan
- 🖥 Clean and user-friendly interface

---

## 🧱 Project Structure
project/
│
├── backend/
│ ├── app.py
│ ├── services.py
│
└── frontend/
├── index.html
├── upload.html
├── dashboard.html
├── main.js



---

## ⚙️ Technologies Used

### Frontend
- HTML
- CSS (Bootstrap)
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### Others
- LocalStorage (for data transfer between pages)

---




## 🔄 Workflow

1. User opens the application (index.html)
2. Navigates to upload page
3. Uploads crop image
4. Image is sent to backend using POST request
5. Backend processes:
   - Detects disease (dummy logic)
   - Fetches weather data
   - Generates recommendation
6. Response is stored in browser (localStorage)
7. User is redirected to dashboard
8. Dashboard displays results

---
## 🧠 System Architecture
User → Upload Page → JavaScript (Fetch API)
→ Flask Backend → Services Layer
→ Decision Logic → JSON Response
→ Dashboard UI


---

## 🔧 Installation & Setup

### Step 1: Clone the repository
```bash
git clone <your-repo-link>
cd project
Step 2: Install dependencies
pip install flask flask-cors requests


Step 3: Run backend

cd backend
python app.py

Step 4: Open frontend
Open index.html in browser
OR use Live Server

API Endpoint
POST /analyze
Request:
FormData with key: image
Response:
{
  "disease": "Tomato Leaf Curl",
  "confidence": 87,
  "temperature": 34,
  "humidity": 60,
  "risk": "High",
  "recommendation": "Use Neem oil spray",
  "timeline": [
    "Day 1-3: Neem oil spray",
    "Day 4: Monitor plant",
    "Day 5: Apply pesticide"
  ]
}

⚠️ Limitations
Disease detection is currently simulated (not real ML)
Requires internet for backend communication
Limited to predefined conditions

Future Enhancements
Integration of real Machine Learning models (CNN/TensorFlow)
Support for multiple crop types and diseases
Offline functionality for rural areas
Mobile application version
Multilingual support
Real-time weather API integration
Image history tracking

Target Users
Farmers
Agricultural students
Researchers
Agri-tech developers

Acknowledgements
OpenWeather API (optional future integration)
Flask Documentation
Bootstrap Framework


