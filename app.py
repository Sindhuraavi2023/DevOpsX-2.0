
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "1.0.0"

@app.route("/")
def home():
    return jsonify({
        "project": "DevOpsX 2.0",
        "message": "Welcome to DevOpsX Application",
        "status": "Running",
        "version": APP_VERSION
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy"
    }), 200

@app.route("/version")
def version():
    return jsonify({
        "version": APP_VERSION
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
