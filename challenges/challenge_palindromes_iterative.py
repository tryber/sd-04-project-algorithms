def is_palindrome_iterative(word):
    if word == "":
        return False

    compare = len(word) - 1

    for letter in word:
        if letter != word[compare]:
            return False
        compare -= 1
        if compare < len(word) / 2:
            break
    return True
