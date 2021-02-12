def merge_sort(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    i_left = i_right = 0
    left_length = len(left)
    right_length = len(right)
    result_length = left_length + right_length

    while i_left < left_length and i_right < right_length:
        if left[i_left] <= right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1

    if i_right == right_length:
        result += left[i_left:]

    if i_right == left_length:
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

# fonte de estudo: https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python
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
            if (mid >= end):
                break
            merged = merge_sort(arr[start:mid], arr[mid:end])
            arr[start : start + len(merged)] = merged
        actual_length *= 2
    return arr


def is_anagram(first_string, second_string): # codigo não está nada otimizado
    return tim_sort(first_string) == tim_sort(second_string)
    # O(n log n + n log n) ???


import timeit 
if __name__ == '__main__':
    setup_import = "from challenges.challenge_anagrams " "import tim_sort"
    first_string = (
        "Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, do sed eiusmod tempor "
        "incididunt ut labore et dolore magna aliqua."
    )
    second_string = (
        "Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, do sed eiusmod tempor "
        "incididunt ut labore et dolore magna aliqua."
    )
    time = timeit.timeit(
        f'tim_sort("{first_string}")',
        setup=f"{setup_import}",
        number=10000,
    )
    print(time)
