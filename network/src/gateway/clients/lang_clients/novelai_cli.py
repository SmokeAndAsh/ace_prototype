# network/src/gateway/clients/novelai_cli.py
import requests
from src.gateway.clients.lang_clients.lang_cli import LanguageClient
from src.error_handling.client_error_handler import ClientCredentialsError, ClientRequestError

class NovelAIClient(LanguageClient):
    def __init__(self, api_key=None):
        super().__init__("NovelAIClient")
        self.api_key = api_key or os.getenv('NOVELAI_API_KEY')
        self.base_url = "https://api.novelai.net"
        if not self.api_key:
            raise ClientCredentialsError(self.name, "API key is missing or invalid")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def test_connection(self):
        try:
            test_url = "https://api.novelai.net/ai/generate"
            test_headers = {"Authorization": f"Bearer {self.api_key}"}
            test_param = {
                "use_string": True,
                "temperature": 1,
                "min_length": 1,
                "max_length": 100
            }
            test_data = {
                "input": "This is a test. Thank you for your cooperation.",
                "model": "kayra-v1",
                "parameters": test_param
            }

            response = requests.post(test_url, json=test_data, headers=test_headers)
            if response.status_code != 201 or 'output' not in response.json():
                raise ClientRequestError("NovelAI", f"Status Code: {response.status_code}, Response: {response.text}")
            return True
        except Exception as e:
            raise ClientRequestError("NovelAI", f"Exception: {e}")

    def test_client(self):
        return self.test_connection()

    def start_client(self):
        print(f"Starting {self.name}...")
        # Implement NovelAI-specific startup logic
        return True

    def get_routes(self):
        # Define specific routes for NovelAI Client
        return [
            {
                'rule': '/api/novelai/generate',
                'methods': ['POST'],
                'endpoint': self.generate_text_endpoint,
            },
        ]

    def generate_text_endpoint(self):
        # Flask view function for handling generation requests
        try:
            data = request.json
            response = self.generate_text(data['input'], data.get('model'), data.get('parameters'))
            return jsonify(response)
        except GatewayRequestError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "An unexpected error occurred"}), 500

    def generate_text(self, input_text, model='kayra-v1', parameters=None):
        parameters = parameters or {
            "use_string": True,
            "temperature": 1,
            "min_length": 1,
            "max_length": 100
        }
        url = f"{self.base_url}/ai/generate"
        data = {
            "input": input_text,
            "model": model,
            "parameters": parameters
        }
        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request Exception in NovelAI Client: {e}")
            return {"error": str(e)}
