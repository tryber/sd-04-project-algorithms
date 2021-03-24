def merge_sort(left, right):
    result = []
    i_left = i_right = 0
    left_length = len(left)
    right_length = len(right)

    while i_left < left_length and i_right < right_length:
        if left[i_left] <= right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1

    if i_right == right_length:
        result += left[i_left:]

    if i_left == left_length:
        result += right[i_right:]

    return result


def insertion_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    for i in range(start + 1, end):
        value = arr[i]
        position = i
        while position - 1 >= start and arr[position - 1] > value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = value
    return arr


def tim_sort(string):
    arr = list(string)
    min_run = 10
    length = len(arr)

    for start in range(0, length, min_run):
        insertion_sort(arr, start, min((start + min_run), length))

    actual_length = min_run
    while actual_length < length:
        for start in range(0, length, actual_length * 2):
            mid = start + actual_length
            end = min((start + actual_length * 2), length)
            if mid >= end:
                break
            merged = merge_sort(arr[start:mid], arr[mid:end])
            arr[start:start + len(merged)] = merged
        actual_length *= 2
    return arr


def is_anagram(first_string, second_string):
    return tim_sort(first_string) == tim_sort(second_string)
