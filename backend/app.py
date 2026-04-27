from flask import Flask, request, jsonify
from flask_cors import CORS
import services

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is running successfully"

@app.route('/analyze', methods=['POST'])
def analyze():
    # 🔴 GET IMAGE
    image = request.files.get("image")

    if not image:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        # Dummy ML (or your service)
        result = services.detect_disease(image)

        # Weather
        weather = services.get_weather("mysore")

        # Decision
        decision = services.get_decision(
            result["disease"], 
            weather["humidity"]
        )

        return jsonify({
            "disease": result["disease"],
            "confidence": result["confidence"],
            "temperature": weather["temp"],
            "humidity": weather["humidity"],
            "risk": decision["risk"],
            "recommendation": decision["recommendation"],
            "timeline": decision["timeline"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)