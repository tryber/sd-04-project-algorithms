def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if first_string == second_string:
        return True
    else:
        return False
