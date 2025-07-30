from flask import jsonify
from app.utils import get_status

def configure_routes(app):
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the secure app!"})

    @app.route('/status')
    def status():
        return jsonify(get_status())
