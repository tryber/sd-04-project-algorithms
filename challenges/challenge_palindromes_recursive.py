def is_palindrome_recursive(word, low=0, high=0):
    if word == "" or word[low] != word[high]:
        return False

    if len(word) == 1:
        return True

    return is_palindrome_recursive(word[low + 1: len(word) - 1])
