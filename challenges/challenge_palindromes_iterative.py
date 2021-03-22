def is_palindrome_iterative(word):
    if word == "":
        return False
    # https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
    # retorna o reverso da "word" comparando se são iguais
    return word == word[::-1]


# print(is_palindrome_iterative("trybe"))
# print(is_palindrome_iterative("reviver"))
