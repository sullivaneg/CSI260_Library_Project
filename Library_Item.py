#We're not using this anymore, but we are keeping it for posterity.
class LibraryItem:
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
    def __init__(self, name, isbn, author, pages, cover_type, genre=None):
        super().__init__(name, isbn, genre, resource_type="Book")  
        self.author = author
        self.pages = pages
        self.cover_type = cover_type

    def __str__(self):
        return f'Book: {self.name} by {self.author}, {self.pages} pages, {self.cover_type} cover (ISBN: {self.isbn})'


# Class 2 of 3
class Movie(LibraryItem):
    def __init__(self, name, isbn, director, duration, genre=None):
        super().__init__(name, isbn, genre, resource_type="Movie")  
        self.director = director
        self.duration = duration

    def __str__(self):
        return f'Movie: {self.name}, directed by {self.director}, {self.duration} min (ISBN: {self.isbn})'


# Class 3 of 3
class CD(LibraryItem):
    def __init__(self, name, isbn, artist, tracks, length, genre=None):
        super().__init__(name, isbn, genre, resource_type="CD")  
        self.artist = artist
        self.tracks = tracks
        self.length = length

    def __str__(self):
        return f'CD: {self.name} by {self.artist}, {self.tracks} tracks, {self.length} minutes (ISBN: {self.isbn})'
