import requests

api_url = "https://api.github.com/repos/wanderer-moe/api"

try:
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to fetch data: HTTP {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
