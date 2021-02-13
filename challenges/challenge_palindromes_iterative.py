def is_palindrome_iterative(word):
    if word == "":
        return False
    for index, letter in enumerate(word):
        if letter != word[len(word) - 1 - index]:
            return False
            if index >= len(word) // 2:
                break
    return True
