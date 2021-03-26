def is_palindrome_recursive(word, low, high):
    if not word or word[low] != word[high]:
        return False

    if len(word) == 1:
        return True

    if low < high+1:
        return is_palindrome_recursive(word, low + 1, high - 1)

    return True
