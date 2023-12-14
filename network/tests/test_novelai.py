import requests
import json

def test_novelai_generation():
    url = "http://localhost:5000/api/novelai/generate"
    headers = {'Content-Type': 'application/json'}
    data = {
        "input": "Once upon a time,",
        "model": "kayra-v1",
        "parameters": {
            "temperature": 1,
            "max_length": 100
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Response from NovelAI:", response.text)

if __name__ == "__main__":
    test_novelai_generation()
