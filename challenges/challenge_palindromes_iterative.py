def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if word == word[::-1] and word != "":
        return True
    return False
