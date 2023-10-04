'''
Create a movie catalog system. 
You have a base class called Movie and a derived class called MovieList.
You need to implement method overriding for displaying movie information. 

Create a base class Movie with the following attributes and methods:
    Attributes: title (string), director (string), year (integer), and genre (string).
    A constructor to initialize these attributes. 
    A method called get_info that returns a formatted string with movie information in the following format: 
        "Title: [title], Director: [director], Year: [year], Genre: [genre]".

Create a derived class MovieList that inherits from Movie. This class should include the following:
    An additional attribute movies which is a list of Movie objects.
        A constructor that accepts a list of Movie objects and initializes the movies attribute. 
        Override the get_info method to return information about all the movies in the list based on the genre of the
    movie.

Create instances of the Movie class to represent individual movies. Then, create a list of these
movies and use it to create an instance of the MovieList class. Ensure that the get_info method is
correctly overridden to display movie information specific to genres

Author : Harishraj S
Date : 04-10-2023
'''


class Movie:

    def __init__(self, title: str, director: str, year: int, genre: str):
        """
        Initialize a Movie object.

        Args:
        title (str): The title of the movie.
        director (str): The director of the movie.
        year (int): The year of release.
        genre (str): The genre of the movie.
        """
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre

    def get_info(self, genre=None):
        """
        Get information about the movie.

        Args:
        genre (str, optional): Filter movies by genre. If None, all movies are included.

        Returns:
        str: A formatted string containing movie information.
        """
        return f"Title: {self.title}, Director: {self.director}, Year: {self.year}, Genre: {self.genre}"

class MovieList(Movie):

    def __init__(self, movies: list):
        """
        Initialize a MovieList object.

        Args:
        movies (list): A list of Movie objects.
        """
        self.movies = movies
    
    def get_info(self, genre=None):
        """
        Get information about the movies in the list based on the genre.

        Args:
        genre (str, optional): Filter movies by genre. If None, all movies are included.

        Returns:
        str: A formatted string containing movie information based on the genre filter.
        """
        movie_info = []
        for movie in self.movies:
            if movie.genre == genre or genre is None:
                movie_info.append(f"Title: {movie.title}, Director: {movie.director}, Year: {movie.year}, Genre: {movie.genre}")
        if movie_info != []:
            return "\n".join(movie_info)
        return "Movie genre not found"

if __name__ == "__main__":
    # Create individual Movie objects
    movie1 = Movie("Inception", "Christopher Nolan", 2010, "Science Fiction")
    movie2 = Movie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama")
    movie3 = Movie("The Dark Knight", "Christopher Nolan", 2008, "Action")
    movie4 = Movie("Forrest Gump", "Robert Zemeckis", 1994, "Drama")
    movie5 = Movie("Pulp Fiction", "Quentin Tarantino", 1994, "Crime")
    movie6 = Movie("The Godfather", "Francis Ford Coppola", 1972, "Crime")
    movie7 = Movie("The Matrix", "Lana Wachowski", 1999, "Science Fiction")
    movie8 = Movie("Gladiator", "Ridley Scott", 2000, "Action")
    movie9 = Movie("Eternal Sunshine of the Spotless Mind", "Michel Gondry", 2004, "Romance")
    movie10 = Movie("The Silence of the Lambs", "Jonathan Demme", 1991, "Crime")
    movie11 = Movie("Schindler's List", "Steven Spielberg", 1993, "Drama")
    movie12 = Movie("The Avengers", "Joss Whedon", 2012, "Action")
    movie13 = Movie("The Lord of the Rings: The Fellowship of the Ring", "Peter Jackson", 2001, "Fantasy")
    movie14 = Movie("Jurassic Park", "Steven Spielberg", 1993, "Science Fiction")
    movie15 = Movie("Titanic", "James Cameron", 1997, "Romance")
    movie16 = Movie("Fight Club", "David Fincher", 1999, "Drama")
    movie17 = Movie("The Revenant", "Alejandro González Iñárritu", 2015, "Adventure")
    movie18 = Movie("The Social Network", "David Fincher", 2010, "Drama")
    movie19 = Movie("Avatar", "James Cameron", 2009, "Science Fiction")

    # Create a list of Movie objects
    movies_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10,
                   movie11, movie12, movie13, movie14, movie15, movie16, movie17, movie18, movie19]

    # Create a MovieList instance
    movie_catalog = MovieList(movies_list)

    # Test cases
    # Test Case 1: No genre filter
    print("\nTest Case 1 - No genre filter:")
    print(movie_catalog.get_info())

    # Test Case 2: Filter by Drama genre
    print("\nTest Case 2 - Filter by Drama genre:")
    print(movie_catalog.get_info("Drama"))

    # Test Case 3: Filter by Science Fiction genre
    print("\nTest Case 3 - Filter by Science Fiction genre:")
    print(movie_catalog.get_info("Science Fiction"))

    # Test Case 4: Filter by an unknown genre
    print("\nTest Case 4 - Filter by an unknown genre (e.g., Horror):")
    print(movie_catalog.get_info("Horror"))

    # Test Case 5: Empty MovieList
    empty_movie_list = MovieList([])
    print("\nTest Case 5 - Empty MovieList:")
    print(empty_movie_list.get_info())
