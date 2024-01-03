'''
The Strategy Pattern is a behavioral design pattern that defines a family of algorithms, encapsulates each algorithm, 
and makes them interchangeable. The pattern allows the client to choose the appropriate algorithm at runtime without 
altering the client's code. 
It promotes the definition of a family of algorithms, encapsulation of each algorithm, and making them interchangeable.
'''
from abc import ABC, abstractmethod
from typing import List

# Strategy Interface


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass

# Concrete Strategies


class BubbleSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        # Using Python's built-in sorted function for simplicity
        return sorted(data)


class QuickSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        # Using Python's built-in sorted function for simplicity
        return sorted(data)

# Context


class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def perform_sort(self, data: List[int]) -> List[int]:
        return self._strategy.sort(data)


# Client Code
data_to_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorter = Sorter(BubbleSortStrategy())

print("Original Data:", data_to_sort)
print("Sorted Data (using Bubble Sort):", sorter.perform_sort(data_to_sort))

sorter.set_strategy(QuickSortStrategy())
print("Sorted Data (using Quick Sort):", sorter.perform_sort(data_to_sort))
