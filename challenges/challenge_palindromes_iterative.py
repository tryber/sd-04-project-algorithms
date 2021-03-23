def is_palindrome_iterative(word):
    if word == '':
        return False

    mirrowed = word[::-1]
    if word == mirrowed:
        return True
    else:
        return False
