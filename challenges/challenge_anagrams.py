def is_anagram(first_string, second_string):
    if len(first_string) == len(second_string):
        firstList = list(first_string)
        secondList = list(second_string)
        if insertion_sort(firstList) == insertion_sort(secondList):
            return True
    return False


def insertion_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        current_position = i
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        array[current_position] = current_value
    print(array)
    return array
