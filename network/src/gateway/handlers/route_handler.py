# network/src/gateway/handlers/route_handler.py

from flask import jsonify
from src.error_handling.gateway_error_handler import GatewayRequestError

class RouteHandler:
    def __init__(self, app):
        self.app = app
        self.setup_default_routes()

    def setup_default_routes(self):
        @self.app.route('/health', methods=['GET'])
        def health_check():
            return jsonify({'status': 'healthy'}), 200

        # ... [Add other default or common routes]

    def add_client_routes(self, client):
        # Implement logic to add routes based on client type
        pass

# Replace `add_novelai_routes` with `add_language_routes` logic
def add_novelai_routes(app, novelai_client: NovelAIClient):
    @app.route('/api/novelai/generate', methods=['POST'])
    def generate_text():
        try:
            data = request.json
            if not data or 'input' not in data or 'model' not in data or 'parameters' not in data:
                raise GatewayRequestError(request_info=request.full_path,
                                          message="Missing required fields in request")

            response = novelai_client.generate_text(data['input'], data['model'], data['parameters'])
            return jsonify(response)
        except GatewayRequestError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            # Log and handle generic exceptions
            return jsonify({"error": "An unexpected error occurred"}), 500

def add_language_routes(app, language_client):
    # Placeholder for future language model routes
    pass

def add_communication_routes(app, communication_client):
    # Placeholder for future communication client routes
    pass

def add_routes(app):
    communication_client = CommunicationClient()
    add_communication_routes(app, communication_client)
    novelai_client = NovelAIClient() # replace with `language_client` logic
    add_novelai_routes(app, novelai_client) # replace with `add_language_routes`
