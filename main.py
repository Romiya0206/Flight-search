#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to bbbbbbbbbbbhtbjjjjjjjjj iu21=yyyyyyyy= achieve the program requirements.=======================================================8fg
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
global CITY

data_manager = DataManager()
flight_search =FlightSearch(data_manager.city)
iata = flight_search.response()
city_name = data_manager.get_city_name()
print(city_name)
#data_manager.sheet_data_post(iata)
flight_data = FlightData()
#flight_data.search_flight(city_name)

for n in city_name:
    name = n['iataCode']
    list = flight_data.search_flight(name)
    for i in list:
        price = i['price']