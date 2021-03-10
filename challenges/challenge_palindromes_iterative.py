# https://www.sanfoundry.com/python-program-check-string-palindrome/

def is_palindrome_iterative(word):

    if not word:
        return False
    if(word == word[::-1]):
        return True
    else:
        return False

# ::-1 são os itens do array de maneira reversa
# OVO === OVO
