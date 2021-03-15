def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) == len(second_string):
        first_letter = [letter for letter in first_string]
        second_letter = [letter for letter in second_string]
        return set(first_letter) == set(second_letter)

    return False
