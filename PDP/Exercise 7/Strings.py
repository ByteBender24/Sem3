'''
   *** Create a string made of the first, middle and last character 
   *** Create a string made of the middle three characters 
   *** Append new string in the middle of a given string 
   *** Create a new string made of the first, middle, and last characters of each input string 
   *** Arrange string characters such that lowercase letters should come first 
   *** Count all letters, digits, and special symbols from a given string 
   *** String characters balance Test: For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character's position doesn't matter. 
   *** Find all occurrences of a substring in a given string by ignoring the case 
   *** Calculate the sum and average of the digits present in a string 
   *** Find the last position of a given substring 
   *** Split a string on hyphens 
   *** Remove empty strings from a list of strings 
   *** Remove special symbols /, punctuation from a string and replace each special symbol with # in the string 
   *** Removal all characters from a string except integers 
   *** Find words with both alphabets and numbers 

Author : Harishraj S
Roll_No : 3122 22 5002 042
Date : 08-11-2023
'''


import string


def first_middle_last(sentence):
    '''Function to return the first, middle, and last characters of a sentence'''
    # Calculate the middle position
    middle = len(sentence) // 2
    return sentence[0] + sentence[middle] + sentence[-1]


def middle_three(sentence):
    '''Function to return the middle three characters of a sentence'''
    middle = len(sentence) // 2
    return sentence[middle - 1: middle + 2]


def append_middle(sentence, new_string):
    '''Function to insert a new string in the middle of the original sentence'''
    middle = len(sentence) // 2
    return sentence[:middle] + new_string + sentence[middle:]


def first_middle_last_of_each(string1, string2):
    '''Function to return the first, middle, and last characters of two strings'''
    middle1 = len(string1) // 2
    middle2 = len(string2) // 2
    return string1[0] + string1[middle1] + string1[-1] + string2[0] + string2[middle2] + string2[-1]


def arrange_lowercase_first(sentence):
    '''Function to arrange lowercase characters before uppercase characters'''
    lower = "".join(char for char in sentence if char.islower())
    upper = "".join(char for char in sentence if char.isupper())
    return lower + upper


def count_characters(sentence):
    '''Function to count the number of letters, digits, and special characters'''
    letters = sum(char.isalpha() for char in sentence)
    digits = sum(char.isdigit() for char in sentence)
    special_char = len(sentence) - letters - digits
    return f"Letters: {letters}, Digits: {digits}, Special Characters: {special_char}"


def is_balanced(string1, string2):
    '''Function to check if all characters in string1 are present in string2'''
    return all(char in string2 for char in string1)


def find_substring_ignore_case(sentence, substring):
    '''Function to find positions of a substring in a case-insensitive manner'''
    sentence_lower = sentence.lower()
    substring_lower = substring.lower()
    return [i for i in range(len(sentence_lower)) if sentence_lower.startswith(substring_lower, i)]


def sum_and_average_of_digits(sentence):
    '''Function to calculate the sum and average of digits in a sentence'''
    digits = [int(i) for i in sentence if i.isdigit()]
    sum_digits = sum(digits)
    average = sum_digits / len(digits) if digits else 0
    return f"Sum: {sum_digits}, Average: {average}"


def last_position_of_substring(sentence, substring):
    '''Function to find the last position of a substring in a sentence'''
    return sentence.rfind(substring)


def split_on_hyphens(sentence):
    '''Function to split a sentence on hyphens'''
    return sentence.split('-')


def remove_empty_strings(input_list):
    '''Function to remove empty strings from a list'''
    return [i for i in input_list if i]


def remove_special_symbols(sentence):
    '''Function to replace special symbols with '#' in a sentence'''
    symbols = string.punctuation
    for symbol in symbols:
        sentence = sentence.replace(symbol, '#')
    return sentence


def remove_non_digits(sentence):
    '''Function to remove non-digit characters from a sentence'''
    return ''.join(char for char in sentence if char.isdigit())


def find_words_with_alphabets_and_numbers(sentence):
    '''Function to find words with both alphabets and numbers'''
    sentence_list = sentence.split()
    return [word for word in sentence_list if any(char.isalpha() for char in word) and any(char.isdigit() for char in word)]


if __name__ == "__main__":
    input_string = "Hello, 123 World3!"
    substring_to_find = "world"
    list_of_strings = ["", "Hello", "", "World", "Test", ""]
    input_with_symbols = "Th1s 1s @ Str!ng"
    s1 = "abcde"
    s2 = "deabc"

    print("1. First, middle, and last characters:",
          first_middle_last(input_string))
    print("2. Middle three characters:", middle_three(input_string))
    print("3. Append in the middle:", append_middle(input_string, "Inserted"))
    print("4. First, middle, and last of each string:",
          first_middle_last_of_each(input_string, "OpenAI"))
    print("5. Arrange lowercase first:", arrange_lowercase_first(input_string))
    print("6. Count characters:", count_characters(input_string))
    print("7. String characters balance test:", is_balanced(s1, s2))
    print("8. Find substring ignoring case:",
          find_substring_ignore_case(input_string, substring_to_find))
    print("9. Sum and average of digits:",
          sum_and_average_of_digits(input_string))
    print("10. Last position of substring:",
          last_position_of_substring(input_string, substring_to_find))
    print("11. Split on hyphens:", split_on_hyphens(input_string))
    print("12. Remove empty strings:", remove_empty_strings(list_of_strings))
    print("13. Remove special symbols:",
          remove_special_symbols(input_with_symbols))
    print("14. Remove non-digits:", remove_non_digits(input_string))
    print("15. Find words with alphabets and numbers:",
          find_words_with_alphabets_and_numbers(input_string))
