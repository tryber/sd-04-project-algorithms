def is_palindrome_iterative(word):
    if word:
        splitWord = list(reversed(list(word)))
        return word == "".join(splitWord)
    return False