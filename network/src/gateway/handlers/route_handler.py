# network/src/gateway/handlers/route_handler.py
import logging
from flask import jsonify, request
from src.gateway.registries.route_registry import RouteRegistry
from src.gateway.registries.client_registry import ClientRegistry
from src.error_handling.gateway_error_handler import GatewayRequestError

class RouteHandler:
    def __init__(self, app, client_registry: ClientRegistry):
        self.app = app
        self.client_registry = client_registry
        self.route_registry = RouteRegistry(app)
        self.setup_default_routes()

    def setup_default_routes(self):
        # Define default routes such as the health check
        @self.app.route('/health', methods=['GET'])
        def health_check():
            return jsonify({'status': 'healthy'}), 200

        @self.app.route('/api/request', methods=['POST'])
        def handle_request():
            try:
                data = request.json
                response = {'message': 'Request received', 'data': data}
                return jsonify(response)
            except Exception as e:
                logging.error(f"Error handling request: {e}", exc_info=True)
                raise GatewayError(f"Error processing request: {e}")

    def add_client_routes(self, client):
       # Iterate through each route defined in the client and add it to the Flask app
        for route_def in client.get_routes():
            # Define the route in Flask using the provided details
            self.app.route(route_def['rule'], methods=route_def['methods'])(route_def['endpoint'])
