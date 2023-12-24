# network/src/gateway/handlers/gateway_handler.py

from flask import Flask, jsonify
import logging
from src.gateway.handlers.route_handler import RouteHandler
from src.error_handling.gateway_error_handler import GatewayError

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

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/request', methods=['POST'])
def handle_request():
    try:
        data = request.json
        response = {'message': 'Request received', 'data': data}
        return jsonify(response)
    except Exception as e:
        logging.error(f"Error handling request: {e}", exc_info=True)
        raise GatewayError(f"Error processing request: {e}")

@app.errorhandler(404)
def page_not_found(e):
    logging.warning(f"404 error: {e}")
    return jsonify({"error": "page not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    logging.error(f"500 Server Error: {error}", exc_info=True)
    return jsonify({"error": "internal server error"}), 500

@app.errorhandler(GatewayConnectionError)
def handle_gateway_connection_error(error):
    logging.error(f"Gateway Connection Error: {error}", exc_info=True)
    return jsonify({"error": str(error)}), 500

@app.errorhandler(GatewayResponseError)
def handle_gateway_response_error(error):
    logging.error(f"Gateway Response Error: {error}", exc_info=True)
    return jsonify({"error": str(error), "status_code": error.status_code}), 500

@app.errorhandler(GatewayRequestError)
def handle_gateway_request_error(error):
    logging.error(f"Gateway Request Error: {error}", exc_info=True)
    return jsonify({"error": str(error)}), 400

@app.errorhandler(GatewayError)
def handle_general_gateway_error(error):
    logging.error(f"General Gateway Error: {error}", exc_info=True)
    return jsonify({"error": str(error)}), 500

@app.errorhandler(Exception)
def unhandled_exception(e):
    logging.critical(f"Unhandled Exception: {e}", exc_info=True)
    return jsonify({"error": "internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
