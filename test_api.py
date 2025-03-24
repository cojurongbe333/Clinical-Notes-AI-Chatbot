
import requests

url = "http://localhost:8000/predict"
sample_payload = {
    "note": "Patient is stable. Continued treatment includes antibiotics and monitoring.",
    "question": "What is the treatment plan?"
}

resp = requests.post(url, json=sample_payload)
print(resp.status_code)
print(resp.json())
