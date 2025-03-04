"""
This file is not in use anymore but we wanted to keep it so you can see everyone did work if you look in our github
"""
#These will be the three subclasses that we came up with during class:
#This is the main class
class LibraryItem:
#Placeholder because I am not working on this part
'''
def __init__(self, name, isbn):
    self.name = name
    self.isbn = isbn
'''
#Class 1 of 3
class Book(LibraryItem):
    def __init__(self, name, isbn, author, pages, cover_type):
        super().__init__(name, isbn)
        self.author = author
        self.pages = pages
        self.cover_type = cover_type
        self.resource_type = 'Book'

    def __str__(self):
        return f'Book: {self.name} by {self.author}, {self.pages} pages, {self.cover_type} cover (ISBN: {self.isbn})'

#Class 2 of 3
class Movie(LibraryItem):
    def __init__(self, name, isbn, director, duration):
        super().__init__(name, isbn)
        self.director = director
        self.duration = duration
        self.resource_type = 'Movie'

    def __str__(self):
        return f'Movie: {self.name}, directed by {self.director}, {self.duration} min (ISBN: {self.isbn})'

#Class 3 of 3
class CD(LibraryItem):
    def __init__(self, name, isbn, artist, tracks, length):
        super().__init__(name, isbn)
        self.artist = artist
        self.tracks = tracks
        self.length = length
        self.resource_type = 'CD'

    def __str__(self):
        return f'CD: {self.name} by {self.artist}, {self.tracks} tracks, {self.length} minutes (ISBN: {self.isbn})'
