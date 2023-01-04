from get_movie import GetMovie


def main():
    print_header()
    search_movie()


def print_header():
    print("-" * 16)
    print("MOVIE SEARCH APP")
    print("-" * 16)


def print_result(movies: GetMovie, title: str) -> None:
    print("Printing Results:")

    movies: list = movies.get_movie_info(title)
    if isinstance(movies, str):
        print(movies)
        return

    for movie in movies:
        print(f"{movie.Year}, {movie.Title}")


def check_title(title: str) -> bool:
    return True if title.strip() else False


def search_movie():
    movie_title = ""

    while movie_title != "x":

        movie_title: str = input("Enter title to search: ").lower()
        if movie_title == "x":
            break

        if check_title(movie_title):
            movies = GetMovie()
            print_result(movies, movie_title)
        else:
            print("Please enter a valid movie title.")

    print("DONE!")


if __name__ == "__main__":
    main()
