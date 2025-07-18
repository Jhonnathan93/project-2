from flask import request, jsonify
import requests
from .middleware.auth_middleware import token_required
from config import Config

def configure_routes(app):
    @app.route('/auth/register', methods=['POST'])
    def register():
        response = requests.post(
            f"{Config.AUTH_SERVICE_URL}/register",
            json=request.json
        )
        return jsonify(response.json()), response.status_code

    @app.route('/auth/login', methods=['POST'])
    def login():
        response = requests.post(
            f"{Config.AUTH_SERVICE_URL}/login",
            json=request.json
        )
        return jsonify(response.json()), response.status_code

    @app.route('/books', methods=['GET'])
    @token_required
    def get_books():
        response = requests.get(
            f"{Config.CATALOG_SERVICE_URL}/books",
            headers={'Authorization': request.headers.get('Authorization')}
        )
        return jsonify(response.json()), response.status_code

    @app.route('/orders', methods=['POST'])
    @token_required
    def create_order():
        response = requests.post(
            f"{Config.ORDER_SERVICE_URL}/orders",
            json=request.json,
            headers={'Authorization': request.headers.get('Authorization')}
        )
        return jsonify(response.json()), response.status_code

    @app.route('/orders/<order_id>/pay', methods=['POST'])
    @token_required
    def pay_order(order_id):
        response = requests.post(
            f"{Config.ORDER_SERVICE_URL}/orders/{order_id}/pay",
            json=request.json,
            headers={'Authorization': request.headers.get('Authorization')}
        )
        return jsonify(response.json()), response.status_code