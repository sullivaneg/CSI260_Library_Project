#Defining a Catalog Class
class Catalog:
    def __init__(self, catalog):
        #catalog is catalog[], the list of all the Library Items
        self.catalog = catalog

    def search(self, string):
        #How do we want to search?

    def add_item(self, items):
        for item in items:
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
                My_Catalog.add_item(input("Enter item to add:"))
                # NOT YET IMPLEMENTED, I NEED TO FIGURE OUT HOW TO SEARCH FOR
                # AN ITEM. UNLESS IT WILL ONLY BE REMOVABLE BY ID NO,
                # WHICH WE NEED TO DECIDE HOW THOSE WILL BE ASSIGNED

            elif option == "4":
                to_remove = input("Enter item to remove:")
                #Same issue as above

            elif option == "5":
                print("Thank you for using CSI260 Library")
                print("Exiting...")
                main = False


