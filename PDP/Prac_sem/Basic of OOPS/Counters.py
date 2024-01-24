import re
from collections import Counter

# Example: Counting the occurrences of characters in a string


def letter_frequency(sentence: str) -> Counter[str]:
    return Counter(sentence)


# Using the Counter object
sentence = "programming is fun"
frequency_counter = letter_frequency(sentence)

# Accessing counts for individual characters
print(frequency_counter['g'])  # Output: 2
print(frequency_counter['z'])  # Output: 0 (if the character is not present)

# Most common elements
most_common_elements = frequency_counter.most_common(2)
print(most_common_elements)
# Output: [('g', 2), ('m', 2)] (in descending order of frequency)

# Polling application example
responses = [
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "vanilla"
]

favorites = Counter(responses).most_common(1)
if favorites:
    name, frequency = favorites[0]
    print(
        f"The most popular flavor is '{name}' with a frequency of {frequency}.")
else:
    print("No responses recorded.")

# Note: The Counter object returns a dictionary-like interface with additional functionalities.

# -------------------------------------------------------------------------------------------------
print("\n\n")
