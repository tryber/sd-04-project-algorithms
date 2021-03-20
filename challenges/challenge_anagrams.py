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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())

# referência https://stackoverflow.com/questions/48217471/is-it-possible-to-check-for-anagram-without-using-sorted-or-dictionary-that-pe


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    primeiro_anagrama = "".join(merge_sort(list(first_string)))
    segundo_anagrama = "".join(merge_sort(list(second_string)))
    for i in range(len(primeiro_anagrama)):
        if primeiro_anagrama[i] != segundo_anagrama[i]:
            return False
    return True
