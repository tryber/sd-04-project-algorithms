def is_palindrome_recursive(word, low, high):
    if not word or word[low] != word[high]:
        return False
    else:
        low += 1
        high -= 1
        if low <= high:
            return is_palindrome_recursive(word, low, high)
        else:
            return True
