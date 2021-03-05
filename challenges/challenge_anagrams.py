def selection_string_sort(string):
    str_array = [letter for letter in string]
    for i in range(len(str_array)):
        minimum = i

        for j in range(i + 1, len(str_array)):
            if str_array[j] < str_array[minimum]:
                minimum = j

        str_array[minimum], str_array[i] = str_array[i], str_array[minimum]

    return "".join(str_array)


def is_anagram(first_string, second_string):
    first_string_sorted = selection_string_sort(first_string)
    second_string_sorted = selection_string_sort(second_string)
    return True if first_string_sorted == second_string_sorted else False
