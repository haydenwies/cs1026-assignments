from movie import Movie

class MovieDatabase:


    def __init__(self):
        self.__movies = list()

    
    def __contains(self, movie):
        """Checks if movie is already inside database. Returns bool value."""

        val = False

        for x in self.__movies:
            if movie.get_title() == x.get_title() and movie.get_year() == x.get_year():
                val = True

        return(val)


    def add_movie(self, title, year):
        """Adds movie to database. Parameters: title (title of movie), year (year of movie as intiger)."""

        movie = Movie(title, year)

        try:
            if self.__contains(movie) == False:
                self.__movies.append(movie)
            else:
                raise KeyError("Movie already exists in database.")
        
        except KeyError:
            pass


    def find_movie(self, title, year):
        """Finds movie in database and returns the movie. Paramters: title (title of movie), year (year of movie as intiger). Returns movie object."""

        for x in self.__movies:
            if title == x.get_title() and year == x.get_year():

                return(x)
        
        return(None)


    def show_all(self):
        """Shows short reviews for all movies in the database."""

        reviews = list()
        
        for x in self.__movies:
            reviews.append(x.short_review())
        
        reviews.sort()
        
        for x in reviews:
            print(x)
