# network/src/gateway/clients/web_clients/web_cli.py
from flask import render_template
from src.gateway.clients.web_clients.web_cli import WebClient

class DashboardClient(WebClient):
    def __init__(self, name):
        super().__init__(name)
        self.setup_routes()

    def setup_routes(self):
        @self.web_app.route('/')
        def home():
            return "Network Module Dashboard"

        @self.web_app.route('/chat')
        def chat():
            return render_template('chat.html')

        @self.web_app.route('/send', methods=['POST'])
        def send_message():
            message = request.form['message']
            # Process and respond to the message here
            return f"ACE Agent received: {message}"

    def test_web(self):
        # Implement meaningful test for web client
        # This could include making a test HTTP request or checking server status
        raise ClientImplementationError(self.name, "test_web", self.__class__.__name__)

    def test_client(self):
        # Implement web client specific test logic
        print(f"Testing {self.name}...")
        return self.test_web()

    def start_web(self):
        # Implement meaningful start for web client
        # This could include setting up web server, defining routes, etc.
        raise ClientImplementationError(self.name, "start_web", self.__class__.__name__)

    def start_client(self):
        # Implement web client specific start logic
        print(f"Starting {self.name}...")
        return self.start_web()

if __name__ == '__main__':
    app.run(debug=True, port=5000)