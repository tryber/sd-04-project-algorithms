def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for i in first_string:
        if i not in second_string:
            return False

    return True
