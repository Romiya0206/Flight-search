import requests
import secrets

sheety_endpoint = secrets.sheety_endpoint


class DataManager:
    def __init__(self):
        self.city = input("Enter the name of the city").title()
        self.user = secrets.user
        self.header = secrets.header
        self.price = input("Enter the lowest amount")
        self.passwd = secrets.passwd

    def sheet_data_post(self, iata):
        self.body = {
            "price": {
                "city": self.city,
                "iataCode": iata,
                "lowestPrice": self.price,
            }
        }

        self.sheety_header = {
            "Authorization": self.header
        }
        sheet_response = requests.post(url=sheety_endpoint, json=self.body, auth=(self.user, self.passwd))
        print(sheet_response.json())

    def get_city_name(self):
        sheet_city = requests.get(url=sheety_endpoint)
        data = sheet_city.json()
        city = data['prices']
        return city
