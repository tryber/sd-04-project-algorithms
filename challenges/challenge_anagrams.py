# criar próprio sort!
# https://app.betrybe.com/course/computer-science/algorithms/sorting-and-searching/conteudos/algoritmos-de-ordenacao?use_case=side_bar
# quicksort
# https://stackoverflow.com/questions/24023549/lists-strings-and-quick-sort/24023646
# https://www.geeksforgeeks.org/python-program-for-quicksort/


def quick_sort(word):
    arr = list(word)
    if arr == []:
        return []
    else:
        pivot = arr[0]
        lesser = quick_sort([x for x in arr[1:] if x < pivot])
        greater = quick_sort([x for x in arr[1:] if x >= pivot])
        return lesser + [pivot] + greater


def is_anagram(first_string, second_string):
    if quick_sort(first_string) == quick_sort(second_string):
        return True
    return False


# def is_anagram(first_string, second_string):
#     # anagrama simples com sorted
#     if sorted(first_string) == sorted(second_string):
#         return True
#     return False


# print(is_anagram("amor", "roma"))
# print(is_anagram("trybe", "roma"))
