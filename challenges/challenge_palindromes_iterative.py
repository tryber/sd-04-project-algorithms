def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if len(word) <= 1:
        return False
    elif len(word) == 2:
        return [word[1], word[0]]

    # Verifica se o primeiro e último
    # elementos não são iguais
    if word[-1] != word[0]:
        return False

    return word == word[::-1]
