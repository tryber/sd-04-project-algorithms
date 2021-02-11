def is_palindrome_recursive(word, low, high):
    if len(word) == 0:
        return False

    if high == low:
        return True
    if word[high] != word[low]:
        return False

    return is_palindrome_recursive(word, low + 1, high-1)
