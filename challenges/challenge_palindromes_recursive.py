def is_palindrome_recursive(word, low, high):
    if high <= low:
        return True

    if word == "":
        return False

    if word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)

    return False
