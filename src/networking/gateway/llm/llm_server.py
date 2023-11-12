# src/networking/gateway/client/llm_server.py
from flask import Flask, request, jsonify
from llm_client import HuggingFaceClient

app = Flask(__name__)
model_client = HuggingFaceClient("TheBloke/Llama-2-7B-Chat-GGUF")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]
    prediction = model_client.predict(text)
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(debug=True)
