import requests
import os

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5000')

def call_api(endpoint, method='GET', data=None):
    url = f"{BACKEND_URL}{endpoint}"
    try:
        if method.upper() == 'POST':
            response = requests.post(url, json=data)
        else:
            response = requests.get(url)

        # Check for backend errors
        if response.status_code != 200:
            return {"error": f"Backend error {response.status_code}: {response.text}"}

        # Try to parse JSON
        try:
            return response.json()
        except ValueError:
            return {"error": "Invalid JSON response", "raw_response": response.text}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
