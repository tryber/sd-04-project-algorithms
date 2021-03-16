def sort_string(word):
    for i in range(len(word)):
        curr_value = word[i]
        curr_index = i
        while (
            curr_index > 0
            and word[curr_index - 1] > curr_value
        ):
            word[curr_index] = word[curr_index - 1]
            curr_index = curr_index - 1
        word[curr_index] = curr_value
    return word


def is_anagram(first_string, second_string):

    if (len(first_string) == len(second_string)):
        new_first_string = sort_string(list(first_string))
        new_second_string = sort_string(list(second_string))
        if (new_first_string == new_second_string):
            return True
    return False
