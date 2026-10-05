import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Gemini key loaded:", bool(api_key))

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {
    "contents": [
        {
            "parts": [
                {"text": "Give a daily astrology insight for Capricorn."}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
print("Status:", response.status_code)
print("Response:", response.text)
