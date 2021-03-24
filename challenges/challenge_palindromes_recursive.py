def is_palindrome_recursive(word, low, high):
   
    if low >= high:
        return len(word) > 0
        line_was_too_long = is_palindrome_recursive(word, low + 1, high - 1)
        return word[low] == word[high] and line_was_too_long
