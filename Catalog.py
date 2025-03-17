"""Catalog file to keep track of library items added

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
import Library_Item
import Pickle_Cat

"""
TODO: 
Add the following features to class Catalog:

    The ability to save to a pickle file - DONE
    The ability to open from a pickle file - DONE

CategoryTag has attributes:
    A "private" class variable that is a list of all CategoryTags that have been created so far
    The name of the tag

Category Tag needs to to implement:
    __init__(self, name)
    __str__(self)
    (class method) all_category_tags() - A properly formatted string with all tags that have been created 
"""


class Catalog:
    """Defining a Catalog Class"""
    def __init__(self):
        # catalog is catalog[], the list of all the Library Items
        self.catalog = list()

    def search(self, string):
        """searches by name"""
        result = []
        for entry in self.catalog:
            if string in entry.name:
                result.append(entry)

        if not result:
            return "No Results Found"
        return result

    def print_add_item(self, item):
        """method to return new library item and print UI"""
        name = input("Enter the name of the item: ")
        isbn = input("Enter the isbn of the item: ")
        genre = input("Enter the genre of the item: ")

        if item == "Book":
            author = input("Enter the author of the item: ")
            pages = input("Enter the number of pages of the item: ")
            cover_type = input("Enter the cover type of the item: ")
            return Library_Item.Book(name, isbn, author, pages, cover_type, genre)

        if item == "Movie":
            director = input("Enter the director of the item: ")
            duration = input("Enter the duration of the item: ")
            return Library_Item.Movie(name, isbn, director, duration, genre)

        if item == "CD":
            artist = input("Enter the artist of the item: ")
            tracks = input("Enter the number of tracks of the item: ")
            length = input("Enter the length of the item in minutes: ")
            return Library_Item.CD(name, isbn, artist, tracks, length, genre)

    def add_item(self, item):
        """calls helper method and adds item to catalog"""
        library_item = self.print_add_item(item)
        self.catalog.append(library_item)

    def sort_by_type(self, type):
        pass

    def sort_by_name(self, name):
        pass

    def remove_item(self, item):
        self.catalog.remove(item)

    def print_items(self):
        """prints entire catalog"""
        for item in self.catalog:
            print(item)


# User Interface
def user_interface(my_catalog):
    """User interface function to loop a text based UI"""
    # User Interface
    main = True

    while main:
        print("Welcome to CSI260 Library")
        print("-----------------------------")
        print("1. Search Catalog")
        print("2. Print entire Catalog")
        print("3. Add item to Catalog")
        print("4. Delete item from Catalog")
        print("5. Exit")

        option = input("Enter (1-5) to select an option: ")

        if option == "1":
            search_string = input("Enter search keyword:")
            results = my_catalog.search(search_string)
            if results:
                for item in results:
                    print(item)
            else:
                print("No results found")

        elif option == "2":
            my_catalog.print_items()

        elif option == "3":
            loop = True
            while loop:
                choice = input("Please enter CD, Book, or Movie: ")
                if choice != "Book" and choice != "Movie" and choice != "CD":
                    print("Invalid Choice")
                    loop = True
                else:
                    my_catalog.add_item(choice)
                    loop = False

        elif option == "4":
            to_remove = input("Enter item to remove:")
            results = my_catalog.search(to_remove)
            if results:
                for item in results:
                    print(item)
                    choice = input("Do you want to remove it? (y/n): ")
                    if choice == "y":
                        my_catalog.remove_item(item)
                    else:
                        continue
            else:
                print("No results found")

        elif option == "5":
            print("Thank you for using CSI260 Library")
            print("Saving...")
            Pickle_Cat.save_catalog(my_catalog)
            print("Exiting...")
            main = False
