def is_palindrome_iterative(word):
    if not word:
        return False
    solution = True
    word_end = len(word) - 1
    word_begin = 0
    while word_end > word_begin:
        if not word[word_begin] == word[word_end]:
            solution = False
            break
        word_begin += 1
        word_end -= 1
    return solution
