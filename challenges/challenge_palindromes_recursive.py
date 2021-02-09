def is_palindrome_recursive(word, low, high):
    if not word:
        return False

    if word[high] != word[low]:
        return False

    if len(word) // 2 == high:
        if word[high] == word[low]:
            return True
        else:
            return False

    return is_palindrome_recursive(word, low + 1, high - 1)
