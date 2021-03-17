def is_palindrome_iterative(word):
    if (not word or word == ''):
        return False
    for i in range(0, len(word)):
        if (word[len(word) - 1 - i] != word[i]):
            return False
    return True
