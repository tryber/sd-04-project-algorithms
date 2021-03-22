def is_palindrome_recursive(word, low, high):

    if word == "":
        return False
    if high == low:
        return True
    if word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False

# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
