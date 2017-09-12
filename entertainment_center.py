# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "action",
                        "me",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        2007,
                        2)

avatar = media.Movie("Avatar",
                     "comedy",
                     "me",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io",
                     2009,
                     2)

school_of_rock = media.Movie("School of Rock",
                             "thriller",
                             "me",
                             "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74",
                             2010,
                             2)

ratatouille = media.Movie("Ratatouille",
                          "action",
                          "me",
                          "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          2012,
                          2)

midnight_in_paris = media.Movie("Midnight in Paris",
                                "drama",
                                "me",
                                "Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2WQQxvU",
                                2011,
                                2)

hunger_games = media.Movie("Hunger Games",
                           "sci-fi",
                           "me",
                           "Storyline",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "http://www.youtube.com/watch?v=-PbA63a7H0bo",
                           2015,
                           3)

#print(avatar.storyline)
#avatar.show_trailer()
print avatar.get_genre()
print avatar.get_rating()
avatar.set_rating(5)
print avatar.get_rating()
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
