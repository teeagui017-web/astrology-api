from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '🔭 Astrology API is running!'

if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🔭 Astrology API is running!"

@app.route("/analyze", methods=["GET"])
def analyze():
    # Placeholder response
    return jsonify({
        "message": "This endpoint will analyze natal and transit data in future updates."
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
