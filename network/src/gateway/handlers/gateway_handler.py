# network/src/gateway/handlers/gateway_handler.py
from flask import Flask, jsonify
import logging
from src.gateway.handlers.route_handler import RouteHandler
from src.error_handling.gateway_error_handler import GatewayError, GatewayConnectionError, GatewayResponseError, GatewayRequestError

class GatewayHandler:
    def __init__(self, name):
        self.name = name
        self.app = Flask(__name__)
        self.route_handler = RouteHandler(self.app)
        self.setup_error_handlers()

    def setup_error_handlers(self):
        @self.app.errorhandler(GatewayError)
        def handle_gateway_error(error):
            logging.error(f"Gateway Error: {error}", exc_info=True)
            return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
