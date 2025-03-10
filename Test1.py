import Library_Item
import Catalog

songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5"]

Item_01 = Library_Item.Book("Eating the Dinosaur", 9781416544203, "Chuck Klosterman", 281, "soft", "Philosophy")
Item_02 = Library_Item.Book("Braiding Sweetgrass", 9781571313355, "Robin Wall Kimmerer", 384, "soft1", "Nature Writing")
Item_03 = Library_Item.Movie("Totally Real Movie", 9782682424466, "Emma Sullivan", 10700)
Item_04 = Library_Item.CD("Totally Real Music", 9782682424467, "Emma Sullivan", 7, 600)
Item_05 = Library_Item.Movie("Totally Real Movie Two", 9782682424468, "Emma Sullivan", 10700)

library_catalog = [Item_01, Item_02, Item_03, Item_04]
catalog = Catalog.Catalog(library_catalog)

Catalog.user_interface(catalog)
