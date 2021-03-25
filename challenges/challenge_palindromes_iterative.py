# https://codereview.stackexchange.com/questions/179150/python-3-palindrome-checker


def is_palindrome_iterative(word):
    return word == word[::-1] and word != ''
