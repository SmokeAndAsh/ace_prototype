import requests
from src.error_handling.network_error_handler import NetworkTimeoutError, NetworkConfigurationError

class HttpConnection:
    def __init__(self, base_url):
        self.base_url = base_url

    def test_connection(self):
        return HttpConnection.health_check()

    def make_request(self, endpoint, method="GET", data=None, headers=None, params=None, timeout=10):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, json=data, headers=headers, params=params, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise NetworkTimeoutError(endpoint, timeout)
        except requests.exceptions.HTTPError as e:
            error_info = {"status_code": e.response.status_code, "error": str(e)}
            return {"error": error_info}
        except requests.exceptions.RequestException as e:
            raise NetworkConfigurationError(message=str(e))

    def health_check(self):
        try:
            response = self.make_request('health', method='GET')
            if response and response.get('status') == 'healthy':
                return True
            return False
        except NetworkTimeoutError as e:
            print(f"HTTP Connection timeout: {e}")
            return False
        except NetworkConfigurationError as e:
            print(f"HTTP Connection configuration error: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error in health check: {e}")
            return False

    def start_http(self):
        # Placeholder start script
        print("HTTP Connection started.")
        return True