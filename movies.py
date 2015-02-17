

class Movie():
    """ This class stores movie information."""

    def __init__(self, movie_title, poster_image, trailer_youtube, lead_1, lead_2, lead_3, director, rating):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.lead_1 = lead_1
        self.lead_2 = lead_2
        self.lead_3 = lead_3
        self.director = director
        self.rating = rating