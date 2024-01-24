from abc import ABC, abstractmethod


class Baking_Cake(ABC):
    @abstractmethod
    def get_ingredients(self):
        pass

    @abstractmethod
    def mix_all(self):
        pass

    @abstractmethod
    def baking(self):
        pass

    def process_cake_making(self):
        print("Preparing a Cake")
        self.get_ingredients()
        self.mix_all()
        self.baking()
        print("Serve the Cake")


class FruitCake(Baking_Cake):

    def get_ingredients(self):
        print("Collect nuts, dry fruits, egg, refined flour, butter, sugar")

    def mix_all(self):
        print("Add one item at a time. Egg should be added in the last")

    def baking(self):
        print("Bake at 325 F")


class Eggless_BlackForest(Baking_Cake):

    def get_ingredients(self):
        print("Collect cocoa powder, baking soda, milk, refined flour, butter, sugar")

    def mix_all(self):
        print("Add all items at the same time")

    def baking(self):
        print("Bake at 475 F")


choice = input("What type of cake you want? ")

if choice == 'fruit':
    cake = FruitCake()
    cake.process_cake_making()
if choice == 'eggless':
    cake = Eggless_BlackForest()
    cake.process_cake_making()
else:
    print("No cake")
