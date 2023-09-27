"""
The following code presents a comprehensive solution for managing a catalog of games for a game store, 
including various game categories, game details, and personnel such as owners and employees. 
This system allows for the efficient operation of a game store, enabling tasks like selling games, 
adding inventory, and retrieving top and newly released games from the catalog. The code also defines 
different game categories, each with its unique attributes, making it suitable for a diverse range of games. 

New suggestions for the future :
    1. Add more categories of games
    2. This is a physical store, consider for a online store (STEAM, EPIC GAMES...)

Modification 1 : Completed the rough code 
Modification 2 : Added new functionalities (new games categories) and owner and employees (Updated driver code)
Modification 3 : Added documentation and comments
Modification 4 : Formatted document with autopep8

Execution Time : [Done] exited with code=0 in 0.26 seconds

Author : Harishraj S
Date : 06-09-2023

"""


class Catalogue:
    def __init__(self, games_list):
        """
        Initialize a Catalogue with a list of games.

        Args:
            games_list (list): A list of Game objects to populate the catalogue.
        """
        self.games = games_list

    def add_game(self, game):
        """
        Add a game to the catalogue.

        Args:
            game (Game): A Game object to add to the catalogue.
        """
        self.games.append(game)
        print(f"{game} Game added")

    def remove_game(self, game):
        """
        Remove a game from the catalogue.

        Args:
            game (Game): A Game object to remove from the catalogue.
        """
        self.games.remove(game)
        print(f"{game} Game removed")

    def __len__(self):
        """
        Get the number of games in the catalogue.

        Returns:
            int: The number of games in the catalogue.
        """
        return len(self.games)


class Gamestore:
    def __init__(self, name, address, owner, contact_no, catalogue=None, website=None, employees=[]):
        """
        Initialize a Gamestore with information about the store, owner, and employees.

        Args:
            name (str): The name of the game store.
            address (str): The address of the game store.
            owner (Owner): An Owner object representing the owner of the store.
            contact_no (str): The contact number for the store.
            catalogue (Catalogue): A Catalogue object representing the store's game catalogue.
            website (str): The website URL of the store.
            employees (list): A list of Employee objects representing store employees.
        """
        self.name = name
        self.address = address
        self.owner = owner
        self.contact_no = contact_no
        self.catalogue = catalogue
        self.website = website
        self.employees = employees

    def num_games(self):
        """
        Get the number of games in the store's catalogue.

        Returns:
            int: The number of games in the catalogue.
        """
        return len(self.catalogue)

    def top_games(self, catalogue, num=5):
        """
        Get the top-rated games from the catalogue.

        Args:
            catalogue (Catalogue): The catalogue to search for top games.
            num (int): The number of top games to retrieve.

        Returns:
            list: A list of game titles representing the top-rated games.
        """
        games = catalogue.games
        sorted_games = sorted(
            games, key=lambda x: x.num_purchases(), reverse=True)
        return [game.title for game in sorted_games[:num]]

    def free_games(self, catalogue):
        """
        Get the free games from the catalogue.

        Args:
            catalogue (Catalogue): The catalogue to search for free games.

        Returns:
            list: A list of game titles representing the free games.
        """
        games = catalogue.games
        return [game.title for game in games if (game.price == 0 or game.discount == 100)]

    def newly_released_games(self, catalogue, num=5):
        """
        Get the newly released games from the catalogue.

        Args:
            catalogue (Catalogue): The catalogue to search for newly released games.
            num (int): The number of newly released games to retrieve.

        Returns:
            list: A list of game titles representing the newly released games.
        """
        games = catalogue.games
        sorted_games = sorted(
            games, key=lambda x: x.release_date, reverse=True)
        return [game.title for game in sorted_games[:num]]

    def games_by_category(self, catalogue, category):
        """
        Get games of a specific category from the catalogue.

        Args:
            catalogue (Catalogue): The catalogue to search for games.
            category (type): The category (e.g., Simulation, ActionAdventure, Puzzle) to filter the games.

        Returns:
            list: A list of game titles of the specified category.
        """
        games = catalogue.games
        return [game.title for game in games if isinstance(game, category)]


class Game:
    def __init__(self, title, price, publisher, developer, rating, size, requirements, release_date=None, review=None, discount=None, description=None):
        """
        Initialize a Game with its details.

        Args:
            title (str): The title of the game.
            price (float): The price of the game.
            publisher (str): The publisher of the game.
            developer (str): The developer of the game.
            rating (float): The rating of the game.
            size (str): The size of the game.
            requirements (str): The requirements for playing the game.
            release_date (str): The release date of the game.
            review (str): A review of the game.
            discount (int): The discount percentage for the game.
            description (str): A description of the game.
        """
        self.title = title
        self.price = price
        self.publisher = publisher
        self.developer = developer
        self.rating = rating
        self.release_date = release_date
        self.review = review
        self.discount = discount
        self.description = description
        self.num_purchase = 0
        self.copies = 0
        self.size = size
        self.requirements = requirements

    def num_purchases(self):
        """
        Get the number of times the game has been purchased.

        Returns:
            int: The number of game purchases.
        """
        return self.num_purchase

    def __str__(self):
        """
        Get a string representation of the game.

        Returns:
            str: The title of the game.
        """
        return self.title

    def __len__(self):
        """
        Get the number of copies of the game available in inventory.

        Returns:
            int: The number of game copies in inventory.
        """
        return self.copies

    def sell(self, num=1):
        """
        Sell a specified number of copies of the game.

        Args:
            num (int): The number of copies to sell.
        """
        self.num_purchase += num
        self.copies -= num
        print(f"{self.title} SOLD")

    def add_inventory(self, num=1):
        """
        Add a specified number of copies to the game's inventory.

        Args:
            num (int): The number of copies to add to inventory.
        """
        self.copies += num
        print(f"{num} {self.title} copies are added to inventory")

    def details(self):
        """
        Get the details of the game.

        Returns:
            str: A string containing the game details.
        """
        details_str = f"Title: {self.title}\nPrice: ${self.price}\nPublisher: {self.publisher}\nDeveloper: {self.developer}\n"
        details_str += f"Rating: {self.rating}\nRelease Date: {self.release_date}\nReview: {self.review}\n"
        details_str += f"Discount: {self.discount}%\nDescription: {self.description}\n"
        details_str += f"Inventory: {self.copies} copies\nPurchases: {self.num_purchase} times"
        return details_str


class MMORPG(Game):
    def __init__(self, title, price, publisher, developer, rating, size, requirements, release_date=None, review=None, discount=None, description=None, world_size=None, subscription_fee=None, player_count=None, guilds=None):
        """
        Initialize an MMORPG game with additional details.

        Args:
            title (str): The title of the game.
            price (float): The price of the game.
            publisher (str): The publisher of the game.
            developer (str): The developer of the game.
            rating (float): The rating of the game.
            size (str): The size of the game.
            requirements (str): The requirements for playing the game.
            release_date (str): The release date of the game.
            review (str): A review of the game.
            discount (int): The discount percentage for the game.
            description (str): A description of the game.
            world_size (str): The size of the game world.
            subscription_fee (float): The subscription fee for the game.
            player_count (int): The maximum player count for the game.
            guilds (list): A list of guilds within the game.
        """
        super().__init__(title, price, publisher, developer, rating, size,
                         requirements, release_date, review, discount, description)
        self.world_size = world_size
        self.subscription_fee = subscription_fee
        self.player_count = player_count
        self.guilds = guilds

    def __str__(self):
        """
        Get a string representation of the MMORPG game.

        Returns:
            str: The title of the game.
        """
        return super().__str__()

    def details(self):
        """
        Get the details of the MMORPG game.

        Returns:
            str: A string containing the game details.
        """
        return super().details()

    def add_inventory(self, num=1):
        """
        Add a specified number of copies to the MMORPG game's inventory.

        Args:
            num (int): The number of copies to add to inventory.
        """
        return super().add_inventory(num)

    def sell(self, num=1):
        """
        Sell a specified number of copies of the MMORPG game.

        Args:
            num (int): The number of copies to sell.
        """
        return super().sell(num)

    def __len__(self):
        """
        Get the number of copies of the MMORPG game available in inventory.

        Returns:
            int: The number of game copies in inventory.
        """
        return super().__len()


class Simulation(Game):
    def __init__(self, title, price, publisher, developer, rating, size, requirements, release_date=None, review=None, discount=None, description=None, real_world_simulation=False):
        """
        Initialize a Simulation game with additional details.

        Args:
            title (str): The title of the game.
            price (float): The price of the game.
            publisher (str): The publisher of the game.
            developer (str): The developer of the game.
            rating (float): The rating of the game.
            size (str): The size of the game.
            requirements (str): The requirements for playing the game.
            release_date (str): The release date of the game.
            review (str): A review of the game.
            discount (int): The discount percentage for the game.
            description (str): A description of the game.
            real_world_simulation (bool): Indicates if the game is a real-world simulation.
        """
        super().__init__(title, price, publisher, developer, rating, size,
                         requirements, release_date, review, discount, description)
        self.real_world_simulation = real_world_simulation

    def __str__(self):
        """
        Get a string representation of the Simulation game.

        Returns:
            str: The title of the game.
        """
        return super().__str__()

    def details(self):
        """
        Get the details of the Simulation game.

        Returns:
            str: A string containing the game details.
        """
        return super().details()

    def add_inventory(self, num=1):
        """
        Add a specified number of copies to the Simulation game's inventory.

        Args:
            num (int): The number of copies to add to inventory.
        """
        return super().add_inventory(num)

    def sell(self, num=1):
        """
        Sell a specified number of copies of the Simulation game.

        Args:
            num (int): The number of copies to sell.
        """
        return super().sell(num)

    def __len__(self):
        """
        Get the number of copies of the Simulation game available in inventory.

        Returns:
            int: The number of game copies in inventory.
        """
        return super().__len()


class ActionAdventure(Game):
    def __init__(self, title, price, publisher, developer, rating, size, requirements, release_date=None, review=None, discount=None, description=None, open_world=False, perspective="TPS"):
        """
        Initialize an Action-Adventure game with additional details.

        Args:
            title (str): The title of the game.
            price (float): The price of the game.
            publisher (str): The publisher of the game.
            developer (str): The developer of the game.
            rating (float): The rating of the game.
            size (str): The size of the game.
            requirements (str): The requirements for playing the game.
            release_date (str): The release date of the game.
            review (str): A review of the game.
            discount (int): The discount percentage for the game.
            description (str): A description of the game.
            open_world (bool): Indicates if the game is open-world.
            perspective (str): The game perspective (e.g., TPS, FPS).
        """
        super().__init__(title, price, publisher, developer, rating, size,
                         requirements, release_date, review, discount, description)
        self.open_world = open_world
        self.perspective = perspective

    def __str__(self):
        """
        Get a string representation of the Action-Adventure game.

        Returns:
            str: The title of the game.
        """
        return super().__str__()

    def details(self):
        """
        Get the details of the Action-Adventure game.

        Returns:
            str: A string containing the game details.
        """
        return super().details()

    def add_inventory(self, num=1):
        """
        Add a specified number of copies to the Action-Adventure game's inventory.

        Args:
            num (int): The number of copies to add to inventory.
        """
        return super().add_inventory(num)

    def sell(self, num=1):
        """
        Sell a specified number of copies of the Action-Adventure game.

        Args:
            num (int): The number of copies to sell.
        """
        return super().sell(num)

    def __len__(self):
        """
        Get the number of copies of the Action-Adventure game available in inventory.

        Returns:
            int: The number of game copies in inventory.
        """
        return super().__len()


class Puzzle(Game):
    def __init__(self, title, price, publisher, developer, rating, size, requirements, release_date=None, review=None, discount=None, description=None, complexity_level=None):
        """
        Initialize a Puzzle game with additional details.

        Args:
            title (str): The title of the game.
            price (float): The price of the game.
            publisher (str): The publisher of the game.
            developer (str): The developer of the game.
            rating (float): The rating of the game.
            size (str): The size of the game.
            requirements (str): The requirements for playing the game.
            release_date (str): The release date of the game.
            review (str): A review of the game.
            discount (int): The discount percentage for the game.
            description (str): A description of the game.
            complexity_level (str): The complexity level of the puzzle.
        """
        super().__init__(title, price, publisher, developer, rating, size,
                         requirements, release_date, review, discount, description)
        self.complexity_level = complexity_level

    def __str__(self):
        """
        Get a string representation of the Puzzle game.

        Returns:
            str: The title of the game.
        """
        return super().__str__()

    def details(self):
        """
        Get the details of the Puzzle game.

        Returns:
            str: A string containing the game details.
        """
        return super().details()

    def add_inventory(self, num=1):
        """
        Add a specified number of copies to the Puzzle game's inventory.

        Args:
            num (int): The number of copies to add to inventory.
        """
        return super().add_inventory(num)

    def sell(self, num=1):
        """
        Sell a specified number of copies of the Puzzle game.

        Args:
            num (int): The number of copies to sell.
        """
        return super().sell(num)

    def __len__(self):
        """
        Get the number of copies of the Puzzle game available in inventory.

        Returns:
            int: The number of game copies in inventory.
        """
        return super().__len()


class Sandbox(Game):
    def __init__(self, title, price, publisher, developer, rating, size, requirements, release_date=None, review=None, discount=None, description=None, user_generated_content=False):
        """
        Initialize a Sandbox game with additional details.

        Args:
            title (str): The title of the game.
            price (float): The price of the game.
            publisher (str): The publisher of the game.
            developer (str): The developer of the game.
            rating (float): The rating of the game.
            size (str): The size of the game.
            requirements (str): The requirements for playing the game.
            release_date (str): The release date of the game.
            review (str): A review of the game.
            discount (int): The discount percentage for the game.
            description (str): A description of the game.
            user_generated_content (bool): Indicates if the game supports user-generated content.
        """
        super().__init__(title, price, publisher, developer, rating, size,
                         requirements, release_date, review, discount, description)
        self.user_generated_content = user_generated_content

    def __str__(self):
        """
        Get a string representation of the Sandbox game.

        Returns:
            str: The title of the game.
        """
        return super().__str__()

    def details(self):
        """
        Get the details of the Sandbox game.

        Returns:
            str: A string containing the game details.
        """
        return super().details()

    def add_inventory(self, num=1):
        """
        Add a specified number of copies to the Sandbox game's inventory.

        Args:
            num (int): The number of copies to add to inventory.
        """
        return super().add_inventory(num)

    def sell(self, num=1):
        """
        Sell a specified number of copies of the Sandbox game.

        Args:
            num (int): The number of copies to sell.
        """
        return super().sell(num)

    def __len__(self):
        """
        Get the number of copies of the Sandbox game available in inventory.

        Returns:
            int: The number of game copies in inventory.
        """
        return super().__len()


class Person:
    def __init__(self, first_name, last_name, email, phone_number):
        """
        Initialize a Person with personal information.

        Args:
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.
            email (str): The email address of the person.
            phone_number (str): The phone number of the person.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def get_full_name(self):
        """
        Get the full name of the person.

        Returns:
            str: The full name of the person.
        """
        return f"{self.first_name} {self.last_name}"

    def contact_info(self):
        """
        Get the contact information of the person.

        Returns:
            str: A string containing the email and phone number of the person.
        """
        return f"Email: {self.email}\nPhone: {self.phone_number}"


class Owner(Person):
    def __init__(self, first_name, last_name, email, phone_number, store_name):
        """
        Initialize an Owner with additional information about the store.

        Args:
            first_name (str): The first name of the owner.
            last_name (str): The last name of the owner.
            email (str): The email address of the owner.
            phone_number (str): The phone number of the owner.
            store_name (str): The name of the owner's store.
        """
        super().__init__(first_name, last_name, email, phone_number)
        self.store_name = store_name

    def owner_info(self):
        """
        Get information about the owner and their store.

        Returns:
            str: A string containing owner and store information.
        """
        return f"Store Name: {self.store_name}\nOwner Name: {self.get_full_name()}\n{self.contact_info()}"


class Employee(Person):
    def __init__(self, first_name, last_name, email, phone_number, employee_id, position):
        """
        Initialize an Employee with additional information about their role.

        Args:
            first_name (str): The first name of the employee.
            last_name (str): The last name of the employee.
            email (str): The email address of the employee.
            phone_number (str): The phone number of the employee.
            employee_id (str): The unique employee ID.
            position (str): The position or role of the employee.
        """
        super().__init__(first_name, last_name, email, phone_number)
        self.employee_id = employee_id
        self.position = position

    def employee_info(self):
        """
        Get information about the employee and their role.

        Returns:
            str: A string containing employee information.
        """
        return f"Employee ID: {self.employee_id}\nPosition: {self.position}\nEmployee Name: {self.get_full_name()}\n{self.contact_info()}"


# Driver Code
if __name__ == "__main__":

    # Create a Catalogue and add games of different categories
    modern_simulation_game = Simulation("The Sims 4", 39.99, "EA", "Maxis",
                                        4.6, "10GB", "PC", release_date="2022-03-20", real_world_simulation=True)
    modern_action_adventure_game = ActionAdventure(
        "Cyberpunk 2077", 49.99, "CD Projekt", "CD Projekt Red", 4.1, "70GB", "PC", release_date="2022-09-15", open_world=True)
    modern_puzzle_game = Puzzle("Candy Crush Saga", 0.00, "King", "King", 4.4,
                                "250MB", "Mobile", release_date="2012-11-14", complexity_level="Easy")
    old_sandbox_game = Sandbox("Minecraft", 24.99, "Mojang Studios", "Mojang Studios",
                               4.8, "200MB", "PC", release_date="2011-11-18", user_generated_content=True)

    # Create a Catalogue and add games to it
    catalogue = Catalogue(
        [modern_simulation_game, modern_action_adventure_game, modern_puzzle_game, old_sandbox_game])

    # People working:
    owner = Owner("John", "Doe", "john@example.com", "555-1234", "Game Haven")
    employee1 = Employee("Alice", "Smith", "alice@example.com",
                         "555-5678", "E12345", "Sales Associate")
    employee2 = Employee("Bob", "Johnson", "bob@example.com",
                         "555-9876", "E67890", "Cashier")
    employees = [employee1, employee2]

    # Create a Gamestore with the Catalogue
    gamestore = Gamestore("Game Haven", "123 Main St", owner, "555-1234",
                          catalogue, "www.gamehaven.com", employees=employees)

    # Test selling and adding inventory
    modern_simulation_game.sell(2)
    modern_action_adventure_game.add_inventory(5)
    modern_puzzle_game.sell(1)
    old_sandbox_game.add_inventory(10)

    # Display game details
    print("Modern Simulation Game Details:")
    print(modern_simulation_game.details())
    print()

    print("Modern Action-Adventure Game Details:")
    print(modern_action_adventure_game.details())
    print()

    print("Modern Puzzle Game Details:")
    print(modern_puzzle_game.details())
    print()

    print("Old Sandbox Game Details:")
    print(old_sandbox_game.details())

    # Get the top-rated and newly released games from the catalogue
    print("Top-Rated Games:")
    top_games = gamestore.top_games(catalogue)
    for i, game in enumerate(top_games, start=1):
        print(f"{i}. {game}")

    print("\nNewly Released Games:")
    new_games = gamestore.newly_released_games(catalogue)
    for i, game in enumerate(new_games, start=1):
        print(f"{i}. {game}")
