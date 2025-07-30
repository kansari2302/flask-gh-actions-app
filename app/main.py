# app/main.py
from flask import Flask, request, jsonify, abort
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/api/data', methods=['POST'])
def process_data():
    if not request.is_json:
        abort(400, description="Invalid Content-Type")

    data = request.get_json()
    if "value" not in data:
        abort(400, description="Missing 'value' field")

    result = data["value"].upper()
    return jsonify({"result": result})

if __name__ == '__main__':
    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    app.run(host=host, port=port)
