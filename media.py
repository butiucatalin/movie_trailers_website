# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    # This class provides a way to store movie related information
    
    MIN_RATING = 0
    MAX_RATING = 5

    def __init__(self, movie_title, movie_genre, movie_director,
                 movie_storyline, poster_image, trailer_youtube,
                 movie_year, movie_rating):
        # initialize instance of class Movie
        self.title = movie_title
        self.__genre = movie_genre
        self.director = movie_director
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = movie_year
        self.__set_correct_rating(movie_rating)

    def __set_correct_rating(self, my_rating):
        if (int)(my_rating) > Movie.MAX_RATING:
            self.__rating = Movie.MAX_RATING
        elif (int)(my_rating) < Movie.MIN_RATING:
            self.__rating = Movie.MIN_RATING
        else:
            self.__rating = (int)(my_rating)

    def get_genre(self):
        return self.__genre

    def get_rating(self):
        return self.__rating

    def set_rating(self, my_rating):
        self.__set_correct_rating(my_rating)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
