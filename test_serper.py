import os
import requests
from dotenv import load_dotenv
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

api_key = os.getenv("SERPER_API_KEY")
print(f"Using API key: {api_key}")


if not api_key:
    print("❌ SERPER_API_KEY not found in environment.")
else:
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "q": "OpenAI"  # You can change this to any search term
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        print("✅ Success!")
        print(data)

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")