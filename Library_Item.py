"""LibraryItem class structure to organize library items such as books, movies, an CDs

Authors: Abigail Gehlbach, Charles Justus, Emma Sullivan, Sebastian Dominguez
Class: CSI-260-01
Assignment: Library Project
Due Date: 2/27/2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

"""
TODO:   make LibraryItem an abstract base class
"""
class LibraryItem:
    """library item class to create items"""
    def __init__(self, name, isbn, genre=None, resource_type=None):
        self.name = name
        self.isbn = isbn
        self.genre = genre if genre else []
        self.resource_type = resource_type  

    def match(self, filter_text):
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            any(filter_text.lower() in str(g).lower() for g in self.genre)  

    def __str__(self):
        genre_display = ", ".join(self.genre) if self.genre else "No genres available"
        return f'{self.name}\n{self.isbn}\n{self.resource_type}\n{genre_display}'

    def to_short_string(self):
        return f'{self.name} - {self.isbn}'


# Class 1 of 3
class Book(LibraryItem):
    """Book class is a subclass of LibraryItem"""
    def __init__(self, name, isbn, author, pages, cover_type, genre=None):
        super().__init__(name, isbn, genre, resource_type="Book")  
        self.author = author
        self.pages = pages
        self.cover_type = cover_type

    def __str__(self):
        return f'Book: {self.name} by {self.author}, {self.pages} pages, {self.cover_type}cover (ISBN: {self.isbn})'


# Class 2 of 3
class Movie(LibraryItem):
    """Movie class is a subclass of LibraryItem"""
    def __init__(self, name, isbn, director, duration, genre=None):
        super().__init__(name, isbn, genre, resource_type="Movie")  
        self.director = director
        self.duration = duration

    def __str__(self):
        return f'Movie: {self.name}, directed by {self.director}, {self.duration} min (ISBN: {self.isbn})'


# Class 3 of 3
class CD(LibraryItem):
    """CD class is a subclass of LibraryItem"""
    def __init__(self, name, isbn, artist, tracks, length, genre=None):
        super().__init__(name, isbn, genre, resource_type="CD")  
        self.artist = artist
        self.tracks = tracks
        self.length = length

    def __str__(self):
        return f'CD: {self.name} by {self.artist}, {self.tracks} tracks, {self.length} minutes (ISBN: {self.isbn})'
