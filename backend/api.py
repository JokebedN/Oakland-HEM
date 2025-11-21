from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables (currently unused but good practice)
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can connect

# Basic health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "OK",
        "message": "Flask API is running!",
        "version": "1.0"
    }), 200

# Simple endpoint for data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "data_point": "Hello from Flask Backend",
        "timestamp": os.getenv("FLASK_RUN_HOST", "localhost") 
    }), 200

if __name__ == '__main__':
    # Run on port 5001
    app.run(host='0.0.0.0', port=5001, debug=True)

