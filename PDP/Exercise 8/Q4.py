"""
 To do the given exercise using the regular expression concept

Author : Harishraj S
Date : 09-11-2023

"""

import re


def valid_sentence(sentence):
    # Define valid subjects, verbs, and objects
    valid_first_subject = ['I']
    valid_second_subject = ['You']
    valid_third_subject_singular = [
        'He', 'She', 'Ram', 'Mohan', 'child', 'Milk']
    valid_third_subject_plural = ['They']
    valid_verbs_1_2 = ['cut', 'sing', 'dance', 'fell',
                       'eat', 'ate', 'drink', 'beat', 'like', 'sit', 'walk']
    valid_verbs_3 = ['cuts', 'drinks', 'ate']
    valid_objects = ['tree', 'Lollypop', 'Milk', 'Kavin', 'cat']

    # Define regular expression patterns for subjects, verbs, and objects
    verb_pattern_1_2 = f'({"|".join(valid_verbs_1_2)})'
    verb_pattern_3 = f'({"|".join(valid_verbs_3)})'
    object_pattern = f'({"|".join(valid_objects)})'

    sentence_pattern = None
    sentence_list = sentence.split()

    for i in sentence_list:
        if i in valid_first_subject:
            subject_pattern_first = f'({"|".join(valid_first_subject)})'
            sentence_pattern = f'^.({subject_pattern_first}).({verb_pattern_1_2}).*({object_pattern})$'
        elif i in valid_second_subject:
            subject_pattern_second = f'({"|".join(valid_second_subject)})'
            sentence_pattern = f'^.({subject_pattern_second}).({verb_pattern_1_2}).({object_pattern}).$'
        elif i in valid_third_subject_singular:
            subject_pattern_third_singular = f'({"|".join(valid_third_subject_singular)})'
            sentence_pattern = f'^.({subject_pattern_third_singular}).({verb_pattern_3}).({object_pattern}).$'
        elif i in valid_third_subject_plural:
            subject_pattern_third_plural = f'({"|".join(valid_third_subject_plural)})'
            sentence_pattern = f'^.({subject_pattern_third_plural}).({verb_pattern_1_2}).*({object_pattern})$'
        else:
            continue

    if sentence_pattern is not None and re.search(sentence_pattern, sentence):
        return 'Valid Sentence'
    else:
        return 'Invalid Sentence'


if __name__ == "__main__":
    sentence1 = "Ram cuts the tree."
    sentence2 = "Mohan beat Kavin"
    sentence3 = "A child ate Lollypop."
    sentence4 = "Drink milk cat"
    sentence5 = "Milk drinks cat"

    print("1.", valid_sentence(sentence1))
    print("2.", valid_sentence(sentence2))
    print("3.", valid_sentence(sentence3))
    print("4.", valid_sentence(sentence4))
    print("5.", valid_sentence(sentence5))

