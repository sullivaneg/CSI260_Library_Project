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
from abc import ABC, abstractmethod
from Category_Tag import CategoryTag


class LibraryItem(ABC):
    """Abstract Base Class for library items"""

    def __init__(self, name, isbn, category, resource_type):
        """init method for parent class which sets shared member vars"""
        self.name = name
        self.isbn = isbn
        self.category = category if category else []
        self.resource_type = resource_type

    @abstractmethod
    def match(self, filter_text):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def to_short_string(self):
        pass


# Class 1 of 3
class Book(LibraryItem):
    """Book class is a subclass of the abstract base class LibraryItem"""

    def __init__(self, name, isbn, author, pages, cover_type, category):
        """init method for subclass which calls super"""
        super().__init__(name, isbn, category, resource_type="Book")
        self.author = author
        self.pages = pages
        self.cover_type = cover_type

    def __str__(self):
        """full string dunder method"""
        return f'Book: {self.name} by {self.author}, {self.pages} pages, {self.cover_type} (ISBN: {self.isbn})\n' \
               f'Tags {self.category}'

    def to_short_string(self):
        """returns a short string of book item"""
        return f'Book: {self.name} - {self.author} - (ISBN: {self.isbn})'

    def match(self, filter_text):
        """Match method for searching which includes all member vars of subclass"""
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            filter_text.lower() == self.resource_type.lower() or \
            any(filter_text.lower() in str(c).lower() for c in self.category) or \
            filter_text.lower() in self.author.lower() or filter_text == self.pages or \
            filter_text.lower() in self.cover_type.lower()


# Class 2 of 3
class Movie(LibraryItem):
    """Movie class is a subclass of the abstract base class LibraryItem"""

    def __init__(self, name, isbn, director, duration, category):
        """init method for subclass which calls super"""
        super().__init__(name, isbn, category, resource_type="Movie")
        self.director = director
        self.duration = duration

    def __str__(self):
        """full string dunder method"""
        return f'Movie: {self.name}, directed by {self.director}, {self.duration} min (ISBN: {self.isbn})\n' \
               f'Tags {self.category}'

    def to_short_string(self):
        """returns a short string of movie item"""
        return f'Movie: {self.name} - {self.director} - (ISBN: {self.isbn})'

    def match(self, filter_text):
        """Match method for searching which includes all member vars of subclass"""
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            filter_text.lower() == self.resource_type.lower() or \
            any(filter_text.lower() in str(c).lower() for c in self.category) or \
            filter_text.lower() in self.director.lower() or filter_text == self.duration


# Class 3 of 3
class CD(LibraryItem):
    """CD class is a subclass of LibraryItem"""

    def __init__(self, name, isbn, artist, tracks, length, category):
        """init method for subclass which calls super"""
        super().__init__(name, isbn, category, resource_type="CD")
        self.artist = artist
        self.tracks = tracks
        self.length = length

    def __str__(self):
        """full string dunder method"""
        return f'CD: {self.name} by {self.artist}, {self.tracks} tracks, {self.length} minutes (ISBN: {self.isbn})\n' \
               f'Tags {self.category}'

    def to_short_string(self):
        """returns a short string of CD item"""
        return f'CD: {self.name} - {self.artist} - (ISBN: {self.isbn})'

    def match(self, filter_text):
        """Match method for searching which includes all member vars of subclass"""
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            filter_text.lower() == self.resource_type.lower() or \
            any(filter_text.lower() in str(c).lower() for c in self.category) or \
            filter_text.lower() in self.artist.lower() or filter_text == self.tracks or filter_text == self.length
