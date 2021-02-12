def is_anagram(first_string, second_string):
    if first_string == '' or second_string:
        return False

    if len(first_string) != second_string:
        return False

    for letter in first_string:
        if letter not in second_string:
            return False

    return True
