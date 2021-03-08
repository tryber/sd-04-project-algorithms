# def selection_string_sort(string):
#     str_array = [letter for letter in string]
#     for i in range(len(str_array)):
#         minimum = i

#         for j in range(i + 1, len(str_array)):
#             if str_array[j] < str_array[minimum]:
#                 minimum = j

#         str_array[minimum], str_array[i] = str_array[i], str_array[minimum]

#     return "".join(str_array)


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def merge_sort(list_source, start=0, end=None):
    list = list_source
    if type(list_source) == str:
        list = [letter for letter in list_source]

    if end is None:
        end = len(list)

    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left, right = merge_sort(list[:mid]), merge_sort(list[mid:])
    return merge(left, right, list.copy())


def is_anagram(first_string, second_string):
    first_string_sorted = merge_sort(first_string)
    second_string_sorted = merge_sort(second_string)
    return True if first_string_sorted == second_string_sorted else False
