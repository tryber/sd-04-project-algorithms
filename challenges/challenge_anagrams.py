def sort(string):
    string_list = list(string)
    for i in range(1, len(string_list)):
        letter = string_list[i]
        j = i - 1

        while j >= 0 and string_list[j] > letter:
            string_list[j + 1] = string_list[j]
            j -= 1
        string_list[j + 1] = letter
    return string_list


def is_anagram(first_string, second_string):
    if (len(first_string) != len(second_string)):
        return False

    first = sort(first_string)
    second = sort(second_string)

    return first == second