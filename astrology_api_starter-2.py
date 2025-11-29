
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '🌟 Astrology API is Live! Ready for chart insights.'

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    # Placeholder response for natal chart analysis
    return jsonify({
        "message": "Natal chart analysis coming soon.",
        "received_data": data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
