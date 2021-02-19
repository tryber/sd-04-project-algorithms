def is_anagram(first_string, second_string):
    """ Faça o código aqui. """

    if sorted(first_string) == sorted(second_string):
        return True
    return False
