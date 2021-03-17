# Ref:
# https://pt.stackoverflow.com/questions/120421/como-identificar-se-uma-string-%C3%A9-um-pal%C3%ADndromo

def is_palindrome_iterative(word):
    size = len(word)
    if size == 0:
        return False
    if word == word[::-1]:
        return True
    return False
