"""
Zadanie 10: Klasa Movie i Cinema
Stwórz klasę Movie, która przechowuje tytuł filmu, reżysera i czas trwania.
Następnie stwórz klasę Cinema, która przechowuje nazwę kina i listę filmów w repertuarze.
Dodaj metody do dodawania filmów do repertuaru oraz wyświetlania listy filmów.
"""

class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    def __str__(self):
        return f"Movie(title={self.title}, director={self.director}, duration={self.duration} minutes)"


class Cinema:
    def __init__(self, cinema_name):
        self.cinema_name = cinema_name
        self.movie_list = []

    def add_movie(self, title):
        if title not in self.movie_list:
            self.movie_list.append(title)
            return f'Movie was added.'
        else:
            return f'Movie on the list.'

    def display(self):
        if self.movie_list:
            print(f"Movies in {self.cinema_name} cinema:")
            for movie in self.movie_list:
                print (f"- {movie.title} by {movie.director}, {movie.duration} minutes")
        else:
            print (f"No movies currently in the repertoire for {self.name} cinema.")

movie1 = Movie("Inception", "Christopher Nolan", 148)
movie2 = Movie("The Matrix", "Lana Wachowski, Lilly Wachowski", 136)
movie3 = Movie("Interstellar", "Christopher Nolan", 169)

cinema = Cinema('Helios')

print(cinema.add_movie(movie1))
print(cinema.add_movie(movie2))
cinema.display()
print(cinema.add_movie(movie3))
cinema.display()



print(cinema.display())

