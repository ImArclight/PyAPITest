import requests

# URL of the GitHub API endpoint
api_url = "https://api.github.com/repos/wanderer-moe/api"

try:
    # Sending a GET request to the API endpoint
    response = requests.get(api_url)
    
    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()
        
        # Printing the received data (or process it as needed)
        print(data)
    else:
        # Handling the case where the request was not successful
        print(f"Failed to fetch data: HTTP {response.status_code}")
except Exception as e:
    # Handling any exceptions that occur during the request
    print(f"An error occurred: {e}")
