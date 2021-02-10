def selection_sort(name):
    arr = list(name)
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

def is_anagram(first_string, second_string):
    return selection_sort(first_string) == selection_sort(second_string)

print(is_anagram('amor','rma'))
