def is_palindrome_recursive(word, low=0, high=None):
    if len(word) == 1:
        return True
    if len(word) == 2:
        return True if word[0] == word[1] else False
    if word == '':
        return False
    high = len(word)-1
    if word[high] != word[low]:
        return False
    return is_palindrome_recursive(word[low+1:high])
