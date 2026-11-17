
from flask import Flask, jsonify, Response, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

APP_VERSION = "1.0.0"

# Prometheus request counter
REQUEST_COUNT = Counter(
    "devopsx_http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "http_status"]
)

@app.after_request
def record_request(response):
    if request.path != "/metrics":
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.path,
            http_status=response.status_code
        ).inc()
    return response

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
    return jsonify({"status": "Healthy"}), 200

@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION})

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
