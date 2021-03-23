def is_anagram(first_string, second_string):
    sorted_first_string = sort_word(
        first_string.replace(" ", "").replace(".", "").replace(",", "")
    )

    sorted_second_string = sort_word(
        second_string.replace(
            " ", "").replace(".", "").replace(",", "")
    )

    if(
        sorted_first_string == sorted_second_string
    ):
        return True

    return False


def sort_word(word):
    word_letters = list(word)
    for i in range(len(word)-1):
        for n in range(i, len(word) - 1):
            if word_letters[n + 1] < word_letters[i]:
                word_letters[i], word_letters[
                    n + 1
                ] = word_letters[n + 1], word_letters[i]
    return word_letters
