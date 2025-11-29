
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/natal', methods=['POST'])
def natal_chart():
    data = request.json
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    location = data.get("location")

    # TODO: Replace with real astrology logic using flatlib or Swiss Ephemeris
    mock_result = {
        "name": name,
        "birth_date": birth_date,
        "birth_time": birth_time,
        "location": location,
        "chart": {
            "Sun": {"sign": "Capricorn", "degree": 19.44, "house": 6},
            "Moon": {"sign": "Aquarius", "degree": 19.03, "house": 7},
            "ASC": {"sign": "Leo", "degree": 1.2}
        }
    }
    return jsonify(mock_result)

@app.route('/transit', methods=['POST'])
def transit_chart():
    data = request.json
    natal_chart = data.get("natal_chart")
    transit_date = data.get("transit_date")

    # TODO: Add transit calculation logic here
    mock_transits = {
        "transit_date": transit_date,
        "active_transits": [
            {"planet": "Saturn", "aspect": "Square", "to": "Sun", "orb": 1.2},
            {"planet": "Jupiter", "aspect": "Trine", "to": "Moon", "orb": 0.5}
        ]
    }
    return jsonify(mock_transits)

if __name__ == '__main__':
    app.run(debug=True)
