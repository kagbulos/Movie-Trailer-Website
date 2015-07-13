import webbrowser

# Movie class that will store relevant information pertaining to movies
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #function which uses the webbrowser library to open the youtube trailer in a browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
