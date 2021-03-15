def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False

    if word == word[::-1]:
        return True
    else:
        return False
