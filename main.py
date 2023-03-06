import requests
import json
from dotenv import load_dotenv

# Set up the API endpoint and parameters
endpoint = "https://api.crunchbase.com/v3.1/odm-organizations"
headers = {"User-Agent": "my-app"}
params = {
    "query": "your_query",
    "user_key": "your_api_key"
}

# Make the API request
response = requests.get(endpoint, headers=headers, params=params)

# Parse the JSON response
data = json.loads(response.text)

# Access the company information
companies = data["data"]["items"]
for company in companies:
    print("Company:", company["name"])
    print("Founders:", company["properties"]["founder"])
    print("Finance:", company["properties"]["financial_organization"])
    print("News:", company["properties"]["news"])