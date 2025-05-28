import json

class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def to_dict(self):
        return {
            "title": self.title,
            "genre": self.genre,
            "year": self.year,
            "rating": self.rating
        }

    @staticmethod
    def from_dict(data):
        return Movie(
            data["title"],
            data["genre"],
            data["year"],
            data["rating"]
        )

class MovieCatalog:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def save_to_file(self, filename="movies.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([m.to_dict() for m in self.movies], f, indent=4, ensure_ascii=False)
        print(f"Catalog saved to {filename}")

    def load_from_file(self, filename="movies.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.movies = [Movie.from_dict(m) for m in data]
            print(f"Catalog loaded from {filename}")
        except FileNotFoundError:
            print(f"No file named {filename} found. Starting with empty catalog.")

    def filter_by_genre(self, genre):
        return [m for m in self.movies if m.genre.lower() == genre.lower()]

    def sort_by_year(self, descending=False):
        return sorted(self.movies, key=lambda m: m.year, reverse=descending)

    def sort_by_rating(self, descending=True):
        return sorted(self.movies, key=lambda m: m.rating, reverse=descending)

    def save_favorites(self, favorites, filename="favorites.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([m.to_dict() for m in favorites], f, indent=4, ensure_ascii=False)
        print(f"Favorites saved to {filename}")

if __name__ == "__main__":
    catalog = MovieCatalog()
    catalog.load_from_file()

    # Додаємо кілька фільмів
    catalog.add_movie(Movie("Кіборги", "драма", 2017, 8.1))
    catalog.add_movie(Movie("Віддана", "історичний", 2019, 7.2))
    catalog.add_movie(Movie("Захар Беркут", "історичний", 2019, 7.0))
    catalog.add_movie(Movie("Поводир", "драма", 2014, 7.1))
    catalog.add_movie(Movie("Стрімголов", "драма", 2017, 6.8))

    # Зберігаємо каталог
    catalog.save_to_file()

    # Фільтрація за жанром
    drama_movies = catalog.filter_by_genre("драма")
    print("\nДраматичні фільми:")
    for m in drama_movies:
        print(f"{m.title} ({m.year}) - Рейтинг: {m.rating}")

    # Сортування за рейтингом
    sorted_by_rating = catalog.sort_by_rating()
    print("\nФільми, відсортовані за рейтингом (спадання):")
    for m in sorted_by_rating:
        print(f"{m.title} - Рейтинг: {m.rating}")

    # Збереження обраних (наприклад, драматичних фільмів)
    catalog.save_favorites(drama_movies)
