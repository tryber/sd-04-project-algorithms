# https://www.sanfoundry.com/python-program-check-string-palindrome/
def is_palindrome_iterative(word):

    if not word:
        return False
    if(word == word[::-1]):
        return True
    else:
        return False

#     rev_word = reversed(word)

#     if len(word) == 0:
#         return False
#     if list(word) == list(rev_word):
#         return True
