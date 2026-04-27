import requests

# 🔹 Dummy disease detection (replace later if needed)
import random

def detect_disease(image):
    diseases = ["Leaf Curl", "Blight", "Healthy"]
    return {
        "disease": random.choice(diseases),
        "confidence": random.randint(75, 95)
    }

# 🔹 Weather API
import requests

def get_weather(city):
    API_KEY = "1f995627c8180764d5ebf130591a65f7"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    if "main" not in res:
        return {
            "temp": 0,
            "humidity": 0,
            "condition": "Unknown"
        }

    return {
        "temp": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "condition": res["weather"][0]["main"]
    }

# 🔹 Decision Engine (MOST IMPORTANT)
def get_decision(disease, humidity):
    if humidity > 70:
        return {
            "risk": "High",
            "recommendation": "Start Neem Oil spray",
            "timeline": [
                "Day 1–3: Neem oil",
                "Day 4: Monitor",
                "Day 5: Switch to chemical"
            ]
        }
    else:
        return {
            "risk": "Moderate",
            "recommendation": "Spray neem oil and control whiteflies. Remove infected leaves",
            "timeline": [
                "Day 1–3: Basic care",
                "Day 4: Observe",
                "Day 5: Re-evaluate"
            ]
        }