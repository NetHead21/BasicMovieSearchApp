import httpx
from pprint import pprint

movie = input("Enter the movie to search: ")
API_URL: str = "https://www.omdbapi.com/?"
params: dict = {
    "apikey": "36807d48",
    "s": movie
}


resp = httpx.get(API_URL, params=params).json()

pprint(resp)