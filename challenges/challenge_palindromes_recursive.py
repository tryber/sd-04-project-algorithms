def is_palindrome_recursive(word, low, high):
    if word == "" or word[low] != word[high]:
        return False

    if high == low:
        return True

    return is_palindrome_recursive(word, low+1, high-1)
