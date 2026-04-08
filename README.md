# Oakland-HEM
Web platform using AI to visualize housing bias and simulate homeownership pathways based on user financial profiles.

## What it does

Oakland-HEM uses real geographic data to expose housing inequities in Oakland, CA. Users can:
- View an **interactive map** of Oakland neighborhoods color-coded by bias score (red = high bias, blue =low bias)
- Click on any neighborhood to see its bias **bias score** and details
- Test the live **Flask API connection** through the frontend interface

This project was built to make housing discrimination data more accessible and transparent through technology. 

## Tech Stack 

**Backend**
- Python + Flask (REST API)
- Flask-CORS (cross-origin resource sharing)
- GeoJSON for geographic neighborhood data
- python-dotenv for environment variables

**Frontend**
- HTML, CSS, JavaScript
- Leaflet.js (interactive maps)
- Tailwind CSS (styling)
- ngrok (backend tunneling)

## Project Structure
Oakland-HEM/
├── backend/
│   ├── api.py                  # Flask API with map data endpoints
│   └── oakland_scores.geojson  # Oakland neighborhood bias score data
├── frontend/
│   └── index.html              # Interactive map frontend
└── README.md

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check - confirms API is running |
| GET | `/api/data` | Returns basic API test data |
| GET | `/api/map-data` | Returns full GeoJSON neighborhood data |

## How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/JokebedN/Oakland-HEM.git
cd Oakland-HEM
```

**2. Set up the backend**
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install flask flask-cors python-dotenv
python api.py
```
The Flask server will run on `http://localhost:5001`

**3. Expose backend with ngrok (optional)**
```bash
ngrok http 5001
```
Copy the ngrok URL and update `API_BASE_URL` in `frontend/index.html`

**4. Open the frontend**

Open `frontend/index.html` in your browser directly, or serve it 
with a local server.
