def is_anagram(first_string, second_string):
    if quick_sort(first_string) == quick_sort(second_string):
        return True
    return False


def quick_sort(word):
    word_list = list(word)
    if word_list == []:
        return []
    else:
        first = word_list[0]
        lesser = quick_sort([index for index in word_list[1:] if index < first])
        greater = quick_sort([index for index in word_list[1:] if index >= first])
        return lesser + [first] + greater
