import requests
import secrets

api_endpoint = "https://api.tequila.kiwi.com"
api_key = secrets.api_key


class FlightSearch:
    def __init__(self, city):
        self.header = {
            "apikey": api_key
        }

        self.params = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",

        }

        self.url = f"{api_endpoint}/locations/query"

    def response(self):
        response = requests.get(url=self.url, params=self.params, headers=self.header)
        location_data = response.json()
        location_id = location_data['locations'][0]['code']
        return location_id
