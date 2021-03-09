# def is_anagram(first_string, second_string):

#     if sorted(first_string) == sorted(second_string):
#         return True
#     return False

def get_dict_from_word(word):
    word_dict = {}

    for character in word:
        if character not in word_dict:
            word_dict[character] = 1
        else:
            word_dict[character] += 1

    return word_dict


def is_anagram(first_string, second_string):
    if get_dict_from_word(first_string) == get_dict_from_word(second_string):
        return True
    return False
