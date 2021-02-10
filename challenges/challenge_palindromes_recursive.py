def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if (high == 0):
        return 0
    if (low == high):
        return True
    if (word[low] != word[high]):
        return False
    if (low < high + 1):
        return is_palindrome_recursive(word, low + 1, high - 1);
  
    return True
