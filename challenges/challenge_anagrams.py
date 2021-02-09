"""
3 - Anagramas (Algoritmo de ordenação)
"""


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False
