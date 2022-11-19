import requests
from src.movie import Movie

class MoviesAPI:

    def fetch_movie(self):
  
        beers_url = "https://random-data-api.com/api/v2/beers"
        appliances_url = "https://random-data-api.com/api/v2/appliances"

        beers_response = requests.get(beers_url)
        beer_name = beers_response.json()["name"]

        appliances_response = requests.get(appliances_url)
        equipment_name = appliances_response.json()["equipment"]
        movie_id = appliances_response.json()["id"]

        return Movie(f"{beer_name} {equipment_name}", movie_id)


if __name__ == "__main__":
    m = MoviesAPI()
    m.fetch_movie()
