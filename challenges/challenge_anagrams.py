def my_sorted(word):
    for i in range(len(word)):
        actual_value = word[i]
        position = i
        while (
            position > 0
            and word[position - 1] > actual_value
        ):
            word[position] = word[position - 1]
            position = position - 1
        word[position] = actual_value
    return word


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    if my_sorted(list(first_string)) == my_sorted(list(second_string)):
        return True
    return False
