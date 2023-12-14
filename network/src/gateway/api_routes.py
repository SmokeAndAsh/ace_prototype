# network/src/gateway/api_routes.py
import os
from flask import request, jsonify
from network.src.clients.novelai_cli import NovelAIClient

def add_novelai_routes(app, novelai_client: NovelAIClient):
    @app.route('/api/novelai/generate', methods=['POST'])
    def generate_text():
        data = request.json
        response = novelai_client.generate_text(data['input'], data['model'], data['parameters'])
        return jsonify(response)

def add_routes(app):
    novelai_api_key = os.getenv('NOVELAI_API_KEY')
    novelai_client = NovelAIClient(api_key=novelai_api_key)
    add_novelai_routes(app, novelai_client)
