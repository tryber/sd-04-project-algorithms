def combine_by_sort(first, second):
    combined = ''
    first_i, second_i = 0, 0
    while first_i < len(first) and second_i < len(second):
        if first[first_i] <= second[second_i]:
            combined += first[first_i]
            first_i += 1
        else:
            combined += second[second_i]
            second_i += 1
    if first_i >= len(first):
        combined += second[second_i:]
    else:
        combined += first[first_i:]
    return combined


def sort_with_combine(string):
    if len(string) <= 1:
        return string
    middle_index = len(string) // 2
    first_part = sort_with_combine(string[:middle_index])
    second_part = sort_with_combine(string[middle_index:])
    return combine_by_sort(first_part, second_part)


def is_anagram(first_string, second_string):
    return sort_with_combine(first_string) == sort_with_combine(second_string)
