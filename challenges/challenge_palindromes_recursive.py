def is_palindrome_recursive(word, low, high):
    if not word or word[low] != word[high]:
        return False

    if word[low] == word[high]:
        low += 1
        high -= 1
        if low == high:
            return True
        else:
            return is_palindrome_recursive(word, low, high)
