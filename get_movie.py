import httpx
import json
import pprint
import collections



MovieResult = collections.namedtuple("MovieResult", "Title, Poster, Type, imdbID, Year")


class GetMovie:
    def __init__(self):
        self.API_URL: str = "https://www.omdbapi.com/?"

    def get_movie_result(self, movies: json) -> list:
        return [MovieResult(**movie) for movie in movies["Search"]]

    def get_movie_info(self, title) -> list | str:
        try:
            params: dict = {"apikey": "36807d48", "s": title}
            result: list = self.get_movie_result(
                httpx.get(self.API_URL, params=params).json()
            )
            return sorted(result, key=lambda movie: movie.Year, reverse=True)
        except httpx.ConnectError:
            return "There might be a problem with your internet. Please try again later."


if __name__ == "__main__":
    movie = GetMovie()
    pprint.pprint(movie.get_movie_info("batman"))
