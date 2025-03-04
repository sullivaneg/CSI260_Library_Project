#Defining a Catalog Class
import Libary_Item

class Catalog:
    def __init__(self, catalog):
        #catalog is catalog[], the list of all the Library Items
        self.catalog = catalog

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
        name = input("Enter the name of the item: ")
        isbn = input("Enter the isbn of the item: ")
        genre = input("Enter the genre of the item: ")

        if item == "Book":
            author = input("Enter the author of the item: ")
            pages = input("Enter the number of pages of the item: ")
            cover_type = input("Enter the cover type of the item: ")
            return Libary_Item.Book(name, isbn, genre, item, author, pages, cover_type)
        if item == "Movie":
            director = input("Enter the director of the item: ")
            duration = input("Enter the duration of the item: ")
            return Libary_Item.Movie(name, isbn, genre, item, director, duration)
        if item == "CD":
            artist = input("Enter the artist of the item: ")
            tracks = input("Enter the number of tracks of the item: ")
            length = input("Enter the length of the item: ")
            return Libary_Item.CD(name, isbn, genre, item, artist, tracks, length)
    def add_item(self, item):
        item = self.print_add_item(self)
        self.catalog.append(item)

    def sort_by_type(self, type):
        pass

    def sort_by_name(self, name):
        pass

    def remove_item(self, items):
        for item in items:
            self.catalog.remove(item)

    def print_items(self):
        for item in self.catalog:
            print(item.to_short_string())



def user_interface(self, My_Catalog):
        # User Interface
        main = True

        while main == True:
            print("Welcome to CSI260 Library")
            print("-----------------------------")
            print("1. Search Catalog")
            print("2. Print entire Catalog")
            print("3. Add item to Catalog")
            print("4. Delete item from Catalog")
            print("5. Exit")

            option = input("Enter the number of your choice:")

            if option == "1":
                search_string = input("Enter search keyword:")
                results = My_Catalog.search(search_string)
                if results:
                    for item in results:
                        print(item)
                else:
                    print("No results found")

            elif option == "2":
                My_Catalog.print_items()

            elif option == "3":

                My_Catalog.add_item(input())


            elif option == "4":
                to_remove = input("Enter item to remove:")
                #Same issue as above

            elif option == "5":
                print("Thank you for using CSI260 Library")
                print("Exiting...")
                main = False


