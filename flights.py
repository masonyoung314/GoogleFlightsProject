import time
import requests
from serpapi import GoogleSearch
import json
import os
from dotenv import load_dotenv

load_dotenv()

params = {
    "api_key": os.getenv("API_KEY"),
    "engine": "google_flights",
    "hl": "en",
    "gl": "us",
    "departure_id": "AMS",
    "arrival_id": "TFS",
    "outbound_date": "2025-12-12",
    "return_date": "2026-01-06",
    "currency": "USD",
    "deep_search": "true",
    "no_cache": "true"
}

class BestFlight:
       def __init__(self, price, airline, departure_time, arrival_time, flight_number):
              self.price = price
              self.airline = airline
              self.departure_time = departure_time
              self.arrival_time = arrival_time
              self.flight_number = flight_number

dailyBestFlights = []

running = True

def printFlight(flight):
      print(f"Price: {flight.price} \nAirline: {flight.airline}\nDeparture Time: {flight.departure_time}\nArrival Time: {flight.arrival_time}\nFlight Number: {flight.flight_number}")

def searchFlights():
    search = GoogleSearch(params)
    results = search.get_dict()
    price = results["best_flights"][0]["price"]
    airline = results["best_flights"][0]["flights"][0]["airline"]
    departure_time = results["best_flights"][0]["flights"][0]["departure_airport"]["time"]
    arrival_time = results["best_flights"][0]["flights"][0]["arrival_airport"]["time"]
    flight_number = results["best_flights"][0]["flights"][0]["flight_number"]
    file_name = str(time.localtime().tm_mon) + "-" + str(time.localtime().tm_mday) + "-" + str(time.localtime().tm_year) + "_" + str(time.localtime().tm_hour) +  ".json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


    # with open("output.json", "r", encoding="utf-8") as file:
    #     flights_info = json.load(file)
    currentBest = BestFlight(price, airline, departure_time, arrival_time, flight_number)
    printFlight(currentBest)
    dailyBestFlights.append(currentBest)
    


while running:
    current_time = time.localtime()
    if ((current_time.tm_hour == 6 and current_time.tm_min == 0 and current_time.tm_sec == 0) 
       or (current_time.tm_hour == 14 and current_time.tm_min == 0 and current_time.tm_sec == 0) 
       or (current_time.tm_hour == 22 and current_time.tm_min == 0 and current_time.tm_sec == 0)):
            searchFlights()
            print("")
    elif (current_time.tm_hour == 23 and current_time.tm_min == 59 and current_time.tm_sec == 59):
          best = dailyBestFlights[0]
          for flight in dailyBestFlights:
                if (flight.price < best.price):
                      best = flight
          print("Best flight of the day:")
          printFlight(best)
          print("")
          dailyBestFlights = []

