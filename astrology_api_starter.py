from flask import Flask, request, jsonify
from astroseek_scraper import fetch_zodiacal_releasing
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '🔭 Astrology API is running!'

@app.route('/analyze', methods=['GET'])
def analyze():
    return jsonify({
        "message": "This endpoint will analyze natal and transit data in future updates."
    })

@app.route('/zr', methods=['GET'])
def get_zr():
    # Collect query params
    name = request.args.get('name', 'Unknown')
    birth_date = request.args.get('birth_date')  # Format: YYYY-MM-DD
    birth_time = request.args.get('birth_time')  # Format: HH:MM
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    city = request.args.get('city', 'Los Angeles')

     return jsonify({
        "message": f"Zodiacal Releasing request received for {name} on {birth_date} at {birth_time} in {city} (Lat: {lat}, Lon: {lon})"
    })
