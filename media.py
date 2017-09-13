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
    #class variables that store information about minimum / maximum
    #movie ratings

    def __init__(self, movie_title, movie_genre, movie_director,
                 movie_storyline, poster_image, trailer_youtube,
                 movie_year, movie_rating):
        #initialize instance of class Movie
        self.title = movie_title
        self.__genre = movie_genre
        self.director = movie_director
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = movie_year
        self.__set_correct_rating(movie_rating)
        self.__comparison_flag = 0

    def __set_correct_rating(self, my_rating):
        #verifies if the movie rating is within the boundaries and sets
        #the rating as an integer
        if (int)(my_rating) > Movie.MAX_RATING:
            self.__rating = Movie.MAX_RATING
        elif (int)(my_rating) < Movie.MIN_RATING:
            self.__rating = Movie.MIN_RATING
        else:
            self.__rating = (int)(my_rating)

    def __compare_by_year(self,other):
        #compare two movies by year ( sort => ascending )
        if self.year > other.year:
            self.__comparison_flag = 1
            return 1
        elif self.year < other.year:
            self.__comparison_flag = -1
            return -1
        else:
            self.__comparison_flag = 0
            return 0

    def __compare_by_title(self,other):
        #compare two movies by year ( sort => ascending )
        if self.title > other.title:
            self.__comparison_flag = 1
            return 1
        elif self.title < other.title:
            self.__comparison_flag = -1
            return -1
        else:
            self.__comparison_flag = 0
            return 0

    def __compare_by_storyline(self,other):
        #compare two movies by year ( sort => ascending )
        if self.storyline > other.storyline:
            self.__comparison_flag = 1
            return 1
        elif self.storyline < other.storyline:
            self.__comparison_flag = -1
            return -1
        else:
            self.__comparison_flag = 0
            return 0

    def __compare_by_rating(self,other):
        #compare two movies by year ( sort => descending )
        if self.__rating > other.get_rating():
            self.__comparison_flag = -1
            return -1
        elif self.__rating < other.get_rating():
            self.__comparison_flag = 1
            return 1
        else:
            self.__comparison_flag = 0
            return 0

    def __cmp__(self, other):
        #compare two movies
        #function is used by sort and sorted methods to sort a list
        #of movies as desired
        if other == None:
            return 1
            #returns 1 because any object is superior to no object 
        if not isinstance(other, Movie):
            return 1
            #returns 1 because any Movie object is superior to other object
        #print 'am comparat ' + str(self.year) + ' - ' + str(other.year)
        if self.__compare_by_rating(other) != 0:
            return self.__comparison_flag
        elif self.__compare_by_title(other) != 0:
            return self.__comparison_flag
        elif self.__compare_by_year(other) != 0:
            return self.__comparison_flag
        else:
            return self.__compare_by_year(storyline)

    def get_genre(self):
        #returns the genre attribute
        return self.__genre

    def get_rating(self):
        #returns the rating attribute
        return self.__rating

    def set_rating(self, my_rating):
        #sets the rating attribute after checking for consistency
        self.__set_correct_rating(my_rating)

    def show_trailer(self):
        #opens a browser an plays a trailer of the current movie
        webbrowser.open(self.trailer_youtube_url)
