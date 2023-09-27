'''
The local librarian has asked us to write a new card catalog program because their
ancient DOS based program is ugly and out of date. Catalogs contain lists of books.
People search them to find books on certain subjects, with specific titles, or by a
particular author. Books can be uniquely identified by an International Standard
Book Number (ISBN). Each book has a Dewey Decimal System (DDS) number
assigned to help find it on a particular shelf. The libraries don't serve only books,
they also have DVDs, magazines, and CDs, none of which have an ISBN or DDS
number. All of these types of items can be uniquely identified by a UPC number.
Magazines are organized by title and then refined by volume and issue number.
The CDs are mostly audio books, and they only have a couple dozen in stock, so
they are organized by the author's last name. Contributors are the people who
donate books to the library.

This code represents a library and catalog of items such as Books, DVD, CD, Magazines and such.
Each item is represented a object and classes are given below

New suggestions for the future:
    1. I can make the item objects go inside catalogs automatically, when I create one object.

Modification 1 : Added timedelta function to find the time from checkout and return
Modification 2 : Added some if else in __init__ , and list comprehension in some classes
Modification 3 : Added documentation 
Modification 4 : Updated driver code (added self help books, comics...)
Modification 5 : Formatted document with autopep8

Execution Time : [Done] exited with code=0 in 0.208 seconds

Author : Harishraj S
Date : 06-09-2023

'''

from datetime import datetime, timedelta


class Item:
    def __init__(self, title, item_id, location):
        """
        Initialize an Item object.

        Args:
            title (str): The title of the item.
            item_id (str): The unique identifier of the item.
            location (str): The physical location of the item in the library.
        """
        self.title = title
        self.item_id = item_id
        self.location = location
        self.checked_out = False
        self.due_date = None

    def get_details(self):
        """
        Get details of the item.

        Returns:
            str: A formatted string containing item details.
        """
        details = f"Title: {self.title}\nItem ID: {self.item_id}\nLocation: {self.location}"
        if self.checked_out:
            details += f"\nStatus: Checked Out\nDue Date: {self.due_date}"
        else:
            details += "\nStatus: Available"
        return details

    def check_out(self, days=14):
        """
        Check out the item.

        Args:
            days (int): The number of days until the item is due for return.

        Returns:
            bool: True if the item was successfully checked out, False if it's already checked out.
        """
        if not self.checked_out:
            self.checked_out = True
            self.due_date = datetime.now() + timedelta(days=days)
            return True
        return False

    def check_in(self):
        """
        Check in the item.

        Returns:
            bool: True if the item was successfully checked in, False if it's not checked out.
        """
        if self.checked_out:
            self.checked_out = False
            self.due_date = None
            return True
        return False


class Book(Item):
    def __init__(self, title, item_id, location, author, isbn, dewey_decimal):
        """
        Initialize a Book object.

        Args:
            title (str): The title of the book.
            item_id (str): The unique identifier of the book.
            location (str): The physical location of the book in the library.
            author (str): The author of the book.
            isbn (str): The International Standard Book Number (ISBN) of the book.
            dewey_decimal (str): The Dewey Decimal System (DDS) number of the book.
        """
        super().__init__(title, item_id, location)
        self.author = author
        self.isbn = isbn
        self.dewey_decimal = dewey_decimal

    def get_details(self):
        """
        Get details of the book.

        Returns:
            str: A formatted string containing book details.
        """
        details = super().get_details()
        return f"{details}\nAuthor: {self.author}\nISBN: {self.isbn}\nDewey Decimal: {self.dewey_decimal}"


class DVD(Item):
    def __init__(self, title, item_id, location, director):
        """
        Initialize a DVD object.

        Args:
            title (str): The title of the DVD.
            item_id (str): The unique identifier of the DVD.
            location (str): The physical location of the DVD in the library.
            director (str): The director of the DVD.
        """
        super().__init__(title, item_id, location)
        self.director = director
        self.languages = []

    def get_details(self):
        """
        Get details of the DVD.

        Returns:
            str: A formatted string containing DVD details.
        """
        details = super().get_details()
        if self.languages:
            details += f"\nLanguages: {', '.join(self.languages)}"
        return details

    def set_languages(self, languages):
        """
        Set available languages for the DVD.

        Args:
            languages (list): A list of available languages for the DVD.
        """
        self.languages = languages


class Magazine(Item):
    def __init__(self, title, item_id, location, volume, issue):
        """
        Initialize a Magazine object.

        Args:
            title (str): The title of the magazine.
            item_id (str): The unique identifier of the magazine.
            location (str): The physical location of the magazine in the library.
            volume (str): The volume of the magazine.
            issue (str): The issue number of the magazine.
        """
        super().__init__(title, item_id, location)
        self.volume = volume
        self.issue = issue

    def get_details(self):
        """
        Get details of the magazine.

        Returns:
            str: A formatted string containing magazine details.
        """
        details = super().get_details()
        return f"{details}\nVolume: {self.volume}\nIssue: {self.issue}"


class CD(Item):
    def __init__(self, title, item_id, location, author_last_name):
        """
        Initialize a CD object.

        Args:
            title (str): The title of the CD.
            item_id (str): The unique identifier of the CD.
            location (str): The physical location of the CD in the library.
            author_last_name (str): The last name of the CD's author.
        """
        super().__init__(title, item_id, location)
        self.author_last_name = author_last_name

    def get_details(self):
        """
        Get details of the CD.

        Returns:
            str: A formatted string containing CD details.
        """
        details = super().get_details()
        return f"{details}\nAuthor's Last Name: {self.author_last_name}"


class Contributor:
    def __init__(self, name):
        """
        Initialize a Contributor object.

        Args:
            name (str): The name of the contributor.
        """
        self.name = name
        self.donated_items = []

    def add_donated_item(self, item):
        """
        Add an item to the list of items donated by the contributor.

        Args:
            item (Item): The item donated by the contributor.
        """
        self.donated_items.append(item)


class LibraryCatalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Add an item to the library catalog.

        Args:
            item (Item): The item to be added to the catalog.
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Remove an item from the library catalog.

        Args:
            item (Item): The item to be removed from the catalog.
        """
        if item in self.items:
            self.items.remove(item)

    def search_by_title(self, title):
        """
        Search for items in the catalog by title.

        Args:
            title (str): The title to search for.

        Returns:
            list: A list of items matching the search title.
        """
        return [item for item in self.items if title.lower() in item.title.lower()]

    def search_by_author(self, author):
        """
        Search for books in the catalog by author.

        Args:
            author (str): The author to search for.

        Returns:
            list: A list of books by the specified author.
        """
        return [item for item in self.items if isinstance(item, Book) and author.lower() in item.author.lower()]

    def search_by_item_id(self, item_id):
        """
        Search for an item in the catalog by its unique item ID.

        Args:
            item_id (str): The item ID to search for.

        Returns:
            list: A list of items with the specified item ID.
        """
        return [item for item in self.items if item.item_id == item_id]

    def list_items(self):
        """
        List all items in the library catalog.
        """
        for item in self.items:
            print(item.get_details())
            print()

    def remove_item_by_id(self, item_id):
        """
        Remove an item from the catalog by its item ID.

        Args:
            item_id (str): The item ID to be removed.
        """
        items_to_remove = [
            item for item in self.items if item.item_id == item_id]
        for item in items_to_remove:
            self.items.remove(item)

    def search_by_dds(self, dds):
        """
        Search for books in the catalog by Dewey Decimal System (DDS) number.

        Args:
            dds (str): The DDS number to search for.

        Returns:
            list: A list of books with the specified DDS number.
        """
        return [item for item in self.items if isinstance(item, Book) and dds in item.dewey_decimal]


class Library:
    def __init__(self, Title, Librarian=None, Location=None, Contact=None, Catalogs=None, Contributors=None):
        """
        Initialize a Library object.

        Args:
            Title (str): The title or name of the library.
            Librarian (str, optional): The name of the librarian. Defaults to None.
            Location (str, optional): The physical location of the library. Defaults to None.
            Contact (str, optional): The contact information for the library. Defaults to None.
            Catalogs (list, optional): A list of library catalogs. Defaults to an empty list.
            Contributors (list, optional): A list of contributors to the library. Defaults to an empty list.
        """
        self.title = Title
        self.librarian = Librarian
        self.location = Location
        self.contact = Contact
        self.catalogs = Catalogs if Catalogs is not None else []
        self.contributors = Contributors if Contributors is not None else []

    def catalog_list(self):
        """
        Get a list of library catalogs.

        Returns:
            list: A list of library catalogs.
        """
        return self.catalogs

    def add_catalog(self, catalog):
        """
        Add a library catalog to the library.

        Args:
            catalog (LibraryCatalog): The catalog to be added to the library.
        """
        self.catalogs.append(catalog)

    def remove_catalog(self, catalog):
        """
        Remove a library catalog from the library.

        Args:
            catalog (LibraryCatalog): The catalog to be removed from the library.
        """
        if catalog in self.catalogs:
            self.catalogs.remove(catalog)

#DRIVER CODE:

if __name__ == "__main__":
    # Create a library
    my_library = Library("My Local Library", "Alice Johnson",
                         "123 Main St", "library@example.com")

    # Create catalogs for self-help books and comics
    self_help_catalog = LibraryCatalog()
    comics_catalog = LibraryCatalog()

    my_library.add_catalog(self_help_catalog)
    my_library.add_catalog(comics_catalog)

    # Add self-help books to the self-help catalog
    self_help1 = Book("The 7 Habits of Highly Effective People", "978-0-671-70863-4",
                      "Self-Help Section", "Stephen R. Covey", "9780671708634", "158.1")
    self_help2 = Book("You Are a Badass", "978-0-7624-5290-2",
                      "Self-Help Section", "Jen Sincero", "9780762452902", "158.1")
    self_help3 = Book("Atomic Habits", "978-0-7352-1466-3",
                      "Self-Help Section", "James Clear", "9780735214663", "158")
    self_help_catalog.add_item(self_help1)
    self_help_catalog.add_item(self_help2)
    self_help_catalog.add_item(self_help3)

    # Add comics to the comics catalog
    comic1 = Book("Batman: The Dark Knight Returns", "978-1-56389-342-1",
                  "Comics Section", "Frank Miller", "9781563893421", "741.5")
    comic2 = Book("Spider-Man: The Clone Saga", "978-0-7851-1914-8",
                  "Comics Section", "Various", "9780785119148", "741.5")
    comic3 = Book("Calvin and Hobbes", "978-0-8362-1718-9",
                  "Comics Section", "Bill Watterson", "9780836217189", "741.5")
    comics_catalog.add_item(comic1)
    comics_catalog.add_item(comic2)
    comics_catalog.add_item(comic3)

    # Create contributors
    contributor1 = Contributor("John Doe")
    contributor2 = Contributor("Emily Smith")

    # Add donated items to contributors
    contributor1.add_donated_item(self_help1)
    contributor2.add_donated_item(comic2)

    my_library.contributors.append(contributor1)
    my_library.contributors.append(contributor2)

    # Display library information
    print(f"Welcome to {my_library.title}!")
    print(f"Library Location: {my_library.location}")
    print(f"Contact Email: {my_library.contact}")
    print(f"Librarian: {my_library.librarian}")

    # List all items in the library
    print("\nList of All Items in the Library:")
    my_library.catalog_list()

    # Search for self-help books by title and author
    print("\nSearch for Self-Help Books by Title: 'Atomic Habits'")
    results = self_help_catalog.search_by_title("Atomic Habits")
    for item in results:
        print(item.get_details())

    print("\nSearch for Self-Help Books by Author: 'Stephen R. Covey'")
    results = self_help_catalog.search_by_author("Stephen R. Covey")
    for item in results:
        print(item.get_details())

    # Search for comics by title and author
    print("\nSearch for Comics by Title: 'Batman: The Dark Knight Returns'")
    results = comics_catalog.search_by_title("Batman: The Dark Knight Returns")
    for item in results:
        print(item.get_details())

    print("\nSearch for Comics by Author: 'Bill Watterson'")
    results = comics_catalog.search_by_author("Bill Watterson")
    for item in results:
        print(item.get_details())
