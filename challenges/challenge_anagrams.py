def is_anagram(first_string, second_string):
    if sorted(first_string) == sorted(second_string):
        return True
    else:
        return False
