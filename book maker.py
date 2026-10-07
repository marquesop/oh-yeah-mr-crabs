class NameOfBook:
    def __init__(self, title, author, year, Genre):
        self.title = title
        self.author = author
        self.year = year
        self.Genre = Genre

    def get_info(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    Book_1 = NameOfBook("The Adventures of Python", "John Doe", 2021, "Fiction")
    Book_2 = NameOfBook("hunger games", "Suzanne Collins", 2008, "Dystopian")
