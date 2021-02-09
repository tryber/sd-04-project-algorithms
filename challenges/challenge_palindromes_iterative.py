def is_palindrome_iterative(word):
    if word == word[::-1] and word != "":
        return True
    return False
