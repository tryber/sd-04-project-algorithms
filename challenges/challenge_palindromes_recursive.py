def is_palindrome_recursive(word, low, high):
    if low >= high:
        return len(word) > 0
    is_palindrome = is_palindrome_recursive(word, low + 1, high - 1)
    return word[low] == word[high] and is_palindrome
