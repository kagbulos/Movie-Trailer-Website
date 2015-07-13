import media
import fresh_tomatoes

#create 3 instances of our movie class to be displayed on our webpage
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A story about a marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                     "A teacher forms a band with the students",
                     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

#store the instances of our movies inside an array to be passed to the open movies function
movies = [toy_story, avatar, school_of_rock]
#run the open movies page function on our list of movies to generate the web page
fresh_tomatoes.open_movies_page(movies)

