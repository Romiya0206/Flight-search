import requests
import secrets

api_endpoint = "https://api.tequila.kiwi.com/v2"
api_key = secrets.api_key


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.header = {
            "apikey": api_key
        }

        self.url = f"{api_endpoint}/search"

    def search_flight(self, place):
        self.params = {
            "fly_from": "LON",
            "fly_to": place,
            "date_from": "07/03/2024",
            "date_to": "07/09/2024",
            "curr": "GBP",
            "one_per_date": 1,
            "limit": "3",
        }

        search_response = requests.get(url=self.url, params=self.params, headers=self.header)
        flight = search_response.json()
        data_list = flight["data"]
        return data_list
