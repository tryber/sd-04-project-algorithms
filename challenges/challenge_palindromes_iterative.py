def is_palindrome_iterative(word):
    if word == "":
        return False
    return word == word[::-1]
