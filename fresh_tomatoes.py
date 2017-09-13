import webbrowser
import os
import re
from media import Movie

HTML_NAVBAR_TABS = 8
JQUERY_NAVBAR_TABS = 5

# Styles and scripting for the page
main_page_head_up = '''
<head>
    <meta charset="utf-8">
    <title>My favourite movie trailers</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #eee5da;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        $(document).on('click','.navbar-collapse.in',function(e) {
          if( $(e.target).is('a') ) {
            $(this).collapse('hide');
          }
        });
        function show_genre(key, elem){
          $('li').removeClass("active");
          $(elem).addClass("active");
          $('.movie-tile').css("display","none");
          $('.can-be-disabled').addClass("is-disabled");
          $(key).hide().first().show("fast", function showNext() {
            if(!$(this).nextAll(key).first().hasClass("movie-tile")) {
                $('.can-be-disabled').removeClass("is-disabled");
            } else {
                $(this).nextAll(key).first().show("fast", showNext);
            }
          });
        }
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.can-be-disabled').addClass("is-disabled");
          $('#allMovies').addClass("active");
          $('.movie-tile').hide().first().show("fast", function showNext() {
            if(!$(this).next("div").hasClass("movie-tile")) {
                $('.can-be-disabled').removeClass("is-disabled");
            } else{
                $(this).next("div").show("fast", showNext);
            }
          });'''
main_page_head_down = '''        
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body style="background-color:#fff8e6;">
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container-fluid">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Katalinux Movie Trailers</a>
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
          </div>
          <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
              {navbar_list}
            </ul>
          </div>
        </div>
      </div>
    </div>
    
<div class="container">
    {movie_tiles}
</div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
\t<div title="{movie_storyline}" class="col-md-6 col-lg-4 movie-tile {class_genre} can-be-disabled text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    \t<h2><strong>{movie_title}</strong></h2>
    \t<img src="{poster_image_url}" width="220" height="342">
    \t<p style="margin-top:20px; font-size:25px; color:green;">{movie_stars}</p>
    \t<h3>Director: {movie_director}</h3>
    \t<h3>( {movie_year} )</h3>
\t</div>
'''

def render_movie_stars(movie):
    html_text = ''
    index = 0
    while index < movie.get_rating():
        html_text += '''<span class="glyphicon glyphicon-star" style="margin-left:5px; margin-right:5px;"></span>'''
        index += 1
    while index < Movie.MAX_RATING:
        html_text += '''<span class="glyphicon glyphicon-star-empty" style="margin-left:5px; margin-right:5px;"></span>'''
        index += 1
    return html_text

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for gender in movies:
        for movie in movies[gender]:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                class_genre='genre-'+movie.get_genre().lower(),
                movie_title=movie.title, movie_storyline=movie.storyline,
                poster_image_url=movie.poster_image_url,
                movie_director=movie.director, movie_year=movie.year,
                trailer_youtube_id=trailer_youtube_id,
                movie_stars=render_movie_stars(movie)
            )
    return content

def create_navbar(movies):
    functions=''
    currentt_function='''\n\t$("{aul}").click(function(){\n\t\tshow_genre("{genul}", "{lista}");\n\t});'''
    options='''\t<li id='allMovies' ><a href="movie_trailers.html">All movies</a></li>'''
    for genre in movies:
        line='\n'+HTML_NAVBAR_TABS*'\t'+'''<li id='{id_li}'><a id='{id_a}' href="#" class="can-be-disabled" >{caption}</a></li>'''
        options+=line.format(id_li="nav"+genre,id_a="a"+genre,caption=genre)
        functions+='\n' + JQUERY_NAVBAR_TABS*'\t' + '''$("#a''' + genre + \
            '''").click(function() {\n''' + (JQUERY_NAVBAR_TABS+1)*'\t' + \
            '''if(!$("#a''' + genre + '''").hasClass("is-disabled")) {\n''' + \
            (JQUERY_NAVBAR_TABS+1)*'\t' + '''show_genre(".genre-''' + \
            genre.lower() + '''", "#nav''' + genre + '''");\n''' + \
            (JQUERY_NAVBAR_TABS+1)*'\t' + '}\n' + JQUERY_NAVBAR_TABS*'\t' + \
            '''});'''
    return options, functions

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('movie_trailers.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  navbar_list_content, navbar_behaviour_content = create_navbar(movies)
  print navbar_behaviour_content
  rendered_content = main_page_content.format(
      movie_tiles=create_movie_tiles_content(movies),
      navbar_list = navbar_list_content )

  main_page_head_rendered = main_page_head_up + navbar_behaviour_content + \
                            main_page_head_down

  # Output the file
  output_file.write(main_page_head_rendered + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
