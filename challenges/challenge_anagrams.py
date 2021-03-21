def merge_by_sort(first, second):
    merged = ''
    first_i, second_i = 0, 0
    while first_i < len(first) and second_i < len(second):
        if first[first_i] <= second[second_i]:
            merged += first[first_i]
            first_i += 1
        else:
            merged += second[second_i]
            second_i += 1
    if first_i >= len(first):
        merged += second[second_i:]
    else:
        merged += first[first_i:]
    return merged


def sort_with_merge(string):
    if len(string) <= 1:
        return string
    middle_index = len(string) // 2
    first_part = sort_with_merge(string[:middle_index])
    second_part = sort_with_merge(string[middle_index:])
    return merge_by_sort(first_part, second_part)


def is_anagram(first_string, second_string):
    return sort_with_merge(first_string) == sort_with_merge(second_string)
