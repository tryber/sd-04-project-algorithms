def is_palindrome_recursive(word, low, high):
    if len(word) == 0:
        return False
    elif len(word) == 1 or low >= high:
        return True
    elif word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    else:
        return False
