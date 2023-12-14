# network/src/gateway/gateway_main.py

from flask import Flask, request, jsonify
from api_routes import add_routes

app = Flask(__name__)

@app.route('/api/request', methods=['POST'])
def handle_request():
    data = request.json
    # Process the data and decide the action
    response = {'message': 'Request received', 'data': data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
