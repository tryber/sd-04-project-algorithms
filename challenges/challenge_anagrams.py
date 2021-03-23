def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    if(
        sort_word(first_string.replace(" ", "")) 
        == sort_word(second_string.replace(" ", ""))
    ):
        return True

    return False


def sort_word(word):
    word_letters = list(word)
    for i in range(len(word)-1):
        for n in range(i, len(word) - 1):
            if word_letters[n + 1] < word_letters[i]:
                word_letters[i], word_letters[n + 1] = word_letters[n + 1], word_letters[i]
    return word_letters
