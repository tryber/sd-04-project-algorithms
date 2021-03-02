def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if len(word) <= 1:
        return False
    elif len(word) == 2:
        return [word[1], word[0]]

    # https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
    # Verifica se o primeiro e último
    # elementos não são iguais
    if word[low] != word[high]:
        return False

    # Se houver mais de
    # dois caracteres, verifica se
    # substring do meio também é
    # palíndromo ou não.
    if low < high + 1:
        return is_palindrome_recursive(word, low + 1, high - 1)

    return True
