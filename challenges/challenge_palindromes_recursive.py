def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    if (low >= high):
        return True
    if (word[low] == word[high]):
        return is_palindrome_recursive(word, low + 1, high - 1)
    else:
        return False
