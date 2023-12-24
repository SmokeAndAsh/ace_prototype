# network/src/error_handling/app_error_handler.py
from flask import jsonify
import logging
from src.error_handling.gateway_error_handler import *

def setup_error_handlers(app):
    @app.errorhandler(GatewayError)
    def handle_gateway_error(error):
        logging.error(f"Gateway Error: {error}", exc_info=True)
        return jsonify({"error": str(error)}), 500

    @app.errorhandler(GatewayConnectionError)
    def handle_connection_error(error):
        logging.error(f"Gateway Connection Error: {error}", exc_info=True)
        return jsonify({"error": str(error)}), 500

    @app.errorhandler(GatewayRequestError)
    def handle_gateway_request_error(error):
        logging.error(f"Gateway Request Error: {error}", exc_info=True)
        return jsonify({"error": str(error)}), 400

   @app.errorhandler(GatewayResponseError)
    def handle_gateway_response_error(error):
        logging.error(f"Gateway Response Error: {error}", exc_info=True)
        return jsonify({"error": str(error), "status_code": error.status_code}), 500
