def sort_string(word):
    word_letters = list(word)

    for i in range(0, len(word_letters)):
        current_letter = word_letters[i]
        while i > 0 and word_letters[i - 1] > current_letter:
            word_letters[i] = word_letters[i - 1]
            i -= 1
        word_letters[i] = current_letter
    return word_letters


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string) \
            or first_string == '' or second_string == '':
        return False

    if sort_string(first_string) == sort_string(second_string):
        return True
    else:
        return False

    return False


# first_string = "pedra"
# second_string = "perdaaa"

# first_string = "pedra"
# second_string = "pedro"

first_string = "pedra"
second_string = "perda"

# first_string = ""
# second_string = "perda"

# first_string = "pedra"
# second_string = ""

# print(sort_string(first_string))
# print(sort_string(second_string))
# print(is_anagram(first_string, second_string))
