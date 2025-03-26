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
import Category_Tag
import Library_Item
import Pickle_Cat
from Category_Tag import CategoryTag


class Catalog:
    """Defining a Catalog Class"""
    def __init__(self):
        # catalog is catalog[], the list of all the Library Items
        self.catalog = list()

    def search(self, string):
        """searches by attribute"""
        result = []
        for entry in self.catalog:
            if entry.match(string):
                result.append(entry)

        if not result:
            return ["No Results Found"]
        return result

    def print_add_item(self, item):
        """method to return new library item and print UI"""
        name = input("Enter the name of the item: ")
        isbn = input("Enter the isbn of the item: ")

        category = set_category()

        if item == "Book":
            author = input("Enter the author of the item: ")
            pages = input("Enter the number of pages of the item: ")
            cover_type = input("Enter the cover type of the item: ")
            return Library_Item.Book(name, isbn, author, pages, cover_type, category)

        if item == "Movie":
            director = input("Enter the director of the item: ")
            duration = input("Enter the duration of the item: ")
            return Library_Item.Movie(name, isbn, director, duration, category)

        if item == "CD":
            artist = input("Enter the artist of the item: ")
            tracks = input("Enter the number of tracks of the item: ")
            length = input("Enter the length of the item in minutes: ")
            return Library_Item.CD(name, isbn, artist, tracks, length, category)

    def add_item(self, item):
        """calls helper method and adds item to catalog"""
        library_item = self.print_add_item(item)
        self.catalog.append(library_item)

    def remove_item(self, item):
        """removes item"""
        self.catalog.remove(item)

    def print_items(self):
        """prints entire catalog"""
        for item in self.catalog:
            print(item.to_short_string())


def set_category():
    category_arr = []
    while True:
        category = input(f"Enter a category tag for this item or 0 to exit: ")
        if category != '0':
            category_arr.append(category)
        else:
            return category_arr


# User Interface
def user_interface(my_catalog):
    """User interface function to loop a text based UI"""
    # User Interface
    main = True

    while main:
        print("-----------------------------")
        print("Welcome to CSI260 Library")
        print("-----------------------------")
        print("1. Search Catalog")
        print("2. Print entire Catalog")
        print("3. Add item to Catalog")
        print("4. Delete item from Catalog")
        print("5. Exit")

        option = input("Enter (1-5) to select an option: ")

        if option == "1":
            search_string = input("Enter search keyword (Artist, Movie, Title, etc):")
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
            Pickle_Cat.save_catalog(my_catalog, Category_Tag.CategoryTag.get_all_tags())
            print("Exiting...")
            main = False
