# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

artificial_intelligence = media.Movie("Artificial Intelligence",
                        "Sci-Fi",
                        "Steven Spielberg",
                        "A highly advanced robotic boy longs to become \"real\" so that he can " +
                        "regain the love of his human mother. ",
                        "https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg",
                        "https://www.youtube.com/watch?v=_19pRsZRiz4",
                        2001,
                        5)

avatar = media.Movie("Avatar",
                     "Sci-Fi",
                     "James Cameron",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io",
                     2009,
                     4)

home_alone = media.Movie("Home Alone",
                         "Comedy",
                         "Chris Columbus",
                         "An eight-year-old troublemaker must protect his house from a pair of burglars",
                         "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg",
                         "https://www.youtube.com/watch?v=CK2Btk6Ybm0",
                         1990,
                         3)

nine_eleven = media.Movie("9/11",
                          "Action",
                          "Martin Guigui",
                          "A group of 5 people find themselves trapped in an elevator in the " +
                          "World Trade Center's North Tower on 9/11",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/9_11_%282017_film%29.png",
                          "https://www.youtube.com/watch?v=8rL4xYyaDjU",
                          2017,
                          4)

IT = media.Movie("IT",
                 "Horror",
                 "Andy Muschietti",
                 "A group of bullied kids band together when a shapeshifting demon, taking the appearance " +
                 "of clown, begins hunting children. ",
                 "https://upload.wikimedia.org/wikipedia/en/a/a2/It_%282017%29_logo.jpg",
                 "https://www.youtube.com/watch?v=7no56Zw1e20",
                 2017,
                 3)

the_exorcist = media.Movie("The Exorcist",
                           "Horror",
                           "William Friedkin",
                           "When a teenage girl is possessed by a mysterious entity, her mother seeks the " +
                           "help of two priests to save her daughter. ",
                           "https://upload.wikimedia.org/wikipedia/ro/c/cc/Exorcistul.jpg",
                           "https://www.youtube.com/watch?v=gzFCk_cvmik",
                           1973,
                           1)

i_robot = media.Movie("I, Robot",
                      "Sci-Fi",
                      "Alex Proyas",
                      "In 2035, a technophobic cop investigates a crime that may have been perpetrated " +
                      "by a robot, which leads to a larger threat to humanity.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3b/Movie_poster_i_robot.jpg",
                      "https://www.youtube.com/watch?v=rL6RRIOZyCM",
                      2004,
                      4)

her = media.Movie("Her",
                  "Sci-Fi",
                  "me",
                  "A lonely writer develops an unlikely relationship with an operating system designed " +
                  "to meet his every need.",
                  "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
                  "https://www.youtube.com/watch?v=6QRvTv_tpw0",
                  2013,
                  3)

the_cure = media.Movie("The Cure",
                       "Drama",
                       "Peter Horton",
                       "Erik, a loner, finds a friend in Dexter, an eleven-year-old boy with AIDS.",
                       "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Cure_1995.jpg",
                       "https://www.youtube.com/watch?v=sa1tVnGSbXs",
                        1995,
                        5)

minions = media.Movie("Minions",
                       "Comedy",
                       "Kyle Balda",
                       "Minions Stuart, Kevin, and Bob are recruited by Scarlet Overkill, a " +
                       "supervillain who hatches a plot to take over the world.",
                       "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                       "https://www.youtube.com/watch?v=eisKxhjBnZ0",
                        2015,
                        5)

titanic = media.Movie("Titanic",
                      "Drama",
                      "James Cameron",
                      "A seventeen-year-old aristocrat falls in love with a kind but poor artist " +
                      "aboard the luxurious, ill-fated R.M.S. Titanic.",
                      "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Cure_1995.jpg",
                      "https://www.youtube.com/watch?v=sa1tVnGSbXs",
                      1997,
                      3)

american_pie = media.Movie("American Pie",
                      "Comedy",
                      "Jason Biggs",
                      "Four teenage boys enter a pact to lose their virginity by prom night.",
                      "https://upload.wikimedia.org/wikipedia/en/c/c8/American_Pie1.jpg",
                      "https://www.youtube.com/watch?v=Sithad108Og",
                      1999,
                      2)

the_omen = media.Movie("The Omen",
                      "Horror",
                      "Jason Biggs",
                      "An American official realizes that his young son may literally be the Devil incarnate.",
                      "https://upload.wikimedia.org/wikipedia/en/6/60/The_Omen_2006_poster.gif",
                      "https://www.youtube.com/watch?v=6dxEtoTXZE0",
                      2006,
                      5)

old_school = media.Movie("Old School",
                      "Comedy",
                      "Todd Phillips",
                      "Three friends attempt to recapture their glory days by opening up a fraternity near " +
                      "their alma mater. ",
                      "https://upload.wikimedia.org/wikipedia/en/2/21/Old_s_poster.jpg",
                      "https://www.youtube.com/watch?v=HNyxTUX-9_U",
                      2003,
                      1)

astro_boy = media.Movie("Astro Boy",
                      "Sci-Fi",
                      "David Bowers",
                      "When an android replica of a boy is rejected by his aggrieved creator, he goes off " +
                      "to find his own identity in a great adventure ",
                      "https://upload.wikimedia.org/wikipedia/en/e/e0/Astro_boy_ver7.jpg",
                      "https://www.youtube.com/watch?v=1AhqOHom9BY",
                      2009,
                      5)

movies = {}

def add(movies, movie_list):
    for aMovie in movie_list:
        if isinstance(aMovie, media.Movie):
            if aMovie.get_genre() in movies:
                movies[aMovie.get_genre()].append(aMovie)
            else:
                movies[aMovie.get_genre()] = [aMovie]

def print_filme(filme):
    print 'Filme :'
    for film in filme:
        print film.title + " " + str(film.year)

def sort_by_genres(myDict):
    for key in myDict:
        myDict[key].sort()

def print_dict(myDict):
    for key in myDict:
        print key
        print_filme(myDict[key])

movies_list = [artificial_intelligence, avatar, home_alone, nine_eleven, IT, the_exorcist,
               i_robot, her, the_cure, minions, titanic, american_pie, the_omen, old_school, astro_boy]
movies_list.sort()
print_filme(movies_list)
add(movies, movies_list)
print movies
lista = movies.keys()
lista.sort()
print lista
print '================================='
print_dict(movies)
print '*********************************'
sort_by_genres(movies)
print '*********************************'
print_dict(movies)


    
#print(avatar.storyline)
#avatar.show_trailer()
#print avatar.get_genre()
#print avatar.get_rating()
#avatar.set_rating(5)
#print avatar.get_rating()
#print movies_list
#movies_list.sort()
#print_filme(movies_list)
#print movies

fresh_tomatoes.open_movies_page(movies_list)
