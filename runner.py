from src.user import User


u = User("asdf")
u.save_movie()
u.saved_movies.show_movies()
movie_id = int(input("-> "))
u.watch_saved_movie(movie_id)
u.saved_movies.show_movies()

