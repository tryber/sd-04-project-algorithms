def is_palindrome_iterative(word):
    if len(word) < 1:
        return False

    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True
