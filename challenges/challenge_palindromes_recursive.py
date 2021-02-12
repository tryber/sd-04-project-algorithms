def is_palindrome_recursive(word, low=0, high=None):
    if len(word) == 1:
        return True

    if word == '':
        return False

    if len(word) == 2:
        return True if word[0] == word[1] else False

    high = len(word) - 1
    if word[low] == word[high]:
        return is_palindrome_recursive(word[low+1:high])
    else:
        return False
