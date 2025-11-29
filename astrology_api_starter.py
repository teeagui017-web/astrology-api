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

    # Example response — you’ll update this with actual AstroSeek data
    return jsonify({
        "name": name,
        "birth_date": birth_date,
        "birth_time": birth_time,
        "latitude": lat,
        "longitude": lon,
        "city": city,
        "message": "Zodiacal Releasing data will be fetched soon!"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
