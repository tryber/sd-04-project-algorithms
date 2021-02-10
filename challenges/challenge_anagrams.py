def is_anagram(first_string, second_string):
    if ''.join(sorted(first_string)) == ''.join(sorted(second_string)):
        return True
    else:
        return False
