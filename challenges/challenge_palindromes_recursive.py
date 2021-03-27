def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    if low < high and word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    elif low >= high:
        return True
    else:
        return False
