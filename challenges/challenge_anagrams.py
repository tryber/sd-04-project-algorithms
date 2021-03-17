# def is_anagram(first_string, second_string):

#     if sorted(first_string) == sorted(second_string):
#         return True
#     return False

# def get_dict_from_word(word):
#     word_dict = {}

#     for character in word:
#         if character not in word_dict:
#             word_dict[character] = 1
#         else:
#             word_dict[character] += 1

#     return word_dict


# def is_anagram(first_string, second_string):
#     if get_dict_from_word(first_string) == get_dict_from_word(second_string):
#         return True
#     return False

# https://app.betrybe.com/course/computer-science/algorithms/sorting-and-searching/conteudos/algoritmos-de-ordenacao?use_case=side_bar

def merge_sort(array):
    arr = list(array)

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor = 0
    right_cursor = 0

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


def is_anagram(first_string, second_string):
    return merge_sort(first_string) == merge_sort(second_string)
