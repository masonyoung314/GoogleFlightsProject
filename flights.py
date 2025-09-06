import time
import requests
from serpapi import GoogleSearch


params = {
    "api_key": "5691d533a6653d970357220a5267f9d4b268c56910eb3875c9331043aa3f4bcf",
    "engine": "google_flights",
    "hl": "en",
    "gl": "us",
    "departure_id": "AMS",
    "arrival_id": "TFS",
    "outbound_date": "2025-12-12",
    "return_date": "2026-01-07",
    "currency": "USD"
}

search = GoogleSearch(params)
results = search.get_dict()
