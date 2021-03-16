def merged_sorted(left_array, right_array, copied_array):
    left_index = 0
    right_index = 0
    length_left = len(left_array)
    length_right = len(right_array)

    while left_index < length_left and right_index < length_right:
        if left_array[left_index] <= right_array[right_index]:
            copied_array[left_index + right_index] = left_array[left_index]
            left_index += 1
        else:
            copied_array[left_index + right_index] = right_array[right_index]
            right_index += 1

    for left_index in range(left_index, length_left):
        copied_array[left_index + right_index] = left_array[left_index]

    for right_index in range(right_index, length_right):
        copied_array[left_index + right_index] = right_array[right_index]

    return copied_array


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid_index = len(array) // 2
    left_array = merge_sort(array[:mid_index])
    right_array = merge_sort(array[mid_index:])

    return merged_sorted(left_array, right_array, array)


def is_anagram(first_string, second_string):

    first_sorted = merge_sort(list(first_string))
    second__sorted = merge_sort(list(second_string))
    print(first_sorted, second__sorted)
    return first_sorted == second__sorted
