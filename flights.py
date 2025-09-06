import time
import requests
from serpapi import GoogleSearch
import json


params = {
    "api_key": "5691d533a6653d970357220a5267f9d4b268c56910eb3875c9331043aa3f4bcf",
    "engine": "google_flights",
    "hl": "en",
    "gl": "us",
    "departure_id": "AMS",
    "arrival_id": "TFS",
    "outbound_date": "2025-12-12",
    "return_date": "2026-01-07",
    "currency": "USD",
    "deep_search": "true"
}

search = GoogleSearch(params)
results = search.get_dict()
price = results["best_flights"][0]["price"]
airline = results["best_flights"][0]["flights"][0]["airline"]
departure_time = results["best_flights"][0]["flights"][0]["departure_airport"]["time"]
arrival_time = results["best_flights"][0]["flights"][0]["arrival_airport"]["time"]
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)


# with open("output.json", "r", encoding="utf-8") as file:
#     flights_info = json.load(file)
print(f"Price: {price} \nAirline: {airline}\nDeparture Time: {departure_time}\nArrival Time: {arrival_time}")

