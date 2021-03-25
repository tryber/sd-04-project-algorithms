def is_palindrome_recursive(word, low=0, high=0):
    """ Faça o código aqui. """
    if len(word) == 1:
        return True

    if word == "" or word[low] != word[high]:
        return False

    return is_palindrome_recursive(word[low + 1: len(word) - 1])

    # usando a recursividade os campos, chamamos o a função novamente em loop
    # com valores diferentes
