def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for i in second_string:
        first_string = first_string.replace( i, "", 1)

    if len(first_string) != 0:
        return False

    return True
