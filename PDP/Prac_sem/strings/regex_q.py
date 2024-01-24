import re


def create_acronym(phrase):
    # Use regex to find the first letter of each word
    acronym_matches = re.findall(r'\b[a-zA-Z]', phrase)

    print(acronym_matches)
    # Join the matched letters to form the acronym
    acronym = ''.join(acronym_matches).upper()

    return acronym


# Example usage
input_phrase = "a small three words"
result_acronym = create_acronym(input_phrase)

print(f"Original Phrase: {input_phrase}")
print(f"Acronym: {result_acronym}")

# -------------------------------------------------------------------------------------------------
print("\n\n")

# sequences of lowercase letters joined by an underscore


def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aab_cbbb"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

# -------------------------------------------------------------------------------------------------
print("\n\n")

# matches a string that has an a followed by zero or more b's


def text_match(text):
    patterns = '^a(b*)$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))


# -------------------------------------------------------------------------------------------------
print("\n\n")

# program that matches a word containing 'z'


def text_match(text):
    patterns = '\w+z.\w*'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))

# -------------------------------------------------------------------------------------------------
print("\n\n")


# program to remove leading zeros from an IP address
ip = "216.008.094.196"
string = re.sub('\.[0]+', '.', ip)
print(string)


# -------------------------------------------------------------------------------------------------
print("\n\n")

# to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9)


def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)


print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))
print(is_allowed_specific_char("Aaaaaaaaaa"))
print(is_allowed_specific_char("aaaaaaaaaa"))
