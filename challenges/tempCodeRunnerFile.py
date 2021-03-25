def selection_sort(word):
    array = [x for x in word]
    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]
    return array


def is_anagram(first_string, second_string):
    return selection_sort(first_string) == selection_sort(second_string)


print(is_anagram('perda', 'pedra')
