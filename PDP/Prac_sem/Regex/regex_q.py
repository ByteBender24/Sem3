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

