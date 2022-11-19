

class Movie:

    def __init__(self, title, id):
        self.title = title
        self.id = id

    def __str__(self):
        return f"Movie({self.title}, {self.id})"