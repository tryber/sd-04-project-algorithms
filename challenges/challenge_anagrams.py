def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False

    for index in first_string:
        if index not in second_string:
            return False

    return True
