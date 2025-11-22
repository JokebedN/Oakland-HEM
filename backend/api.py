from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import json   # <-- Needed to load GeoJSON

# Load environment variables 
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS(Cross-Origin Resource Sharing) so frontend can connect

# This loads backend/oakland_scores.geojson 
# and stores it in the variable map_data
try:
    with open("backend/oakland_scores.geojson") as f:
        map_data = json.load(f)
except Exception as e:
    print("ERROR loading GeoJSON:", e)
    map_data = {}   # fallback if file is missing
# -------------------------------------------------------


# Basic health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "OK",
        "message": "Flask API is running!",
        "version": "1.0"
    }), 200


# Simple test endpoint for the MVP
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "data_point": "Hello from Flask Backend",
        "timestamp": os.getenv("FLASK_RUN_HOST", "localhost")
    }), 200


# NEW: MAP DATA ENDPOINT (sends GeoJSON to the frontend)
@app.route('/api/map-data', methods=['GET'])
def map_data_endpoint():
    return jsonify(map_data), 200


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

