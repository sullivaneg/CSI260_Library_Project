#Defining a Catalog Class
import Library_Item

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
            return Library_Item.Book(name, isbn, author, pages, cover_type, genre)

        if item == "Movie":
            director = input("Enter the director of the item: ")
            duration = input("Enter the duration of the item: ")
            return Library_Item.Movie(name, isbn, director, duration, genre)

        if item == "CD":
            artist = input("Enter the artist of the item: ")
            tracks = input("Enter the number of tracks of the item: ")
            length = input("Enter the length of the item: ")
            return Library_Item.CD(name, isbn, artist, tracks, length, genre)

    def add_item(self, item):
        library_item = self.print_add_item(item)
        self.catalog.append(library_item)

    def sort_by_type(self, type):
        pass

    def sort_by_name(self, name):
        pass

    def remove_item(self, item):
            self.catalog.remove(item)

    def print_items(self):
        for item in self.catalog:
            print(item.to_short_string())


#User Interface
def user_interface(my_catalog):
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
                while loop == True:
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
                print("Exiting...")
                main = False


