def is_anagram(first_string, second_string):

    if len(first_string) != len(second_string):
        return False

    if sort(first_string) == sort(second_string):
        return True

    return False


def sort(array):
    for index in range(0, len(array)):
        current_element = array[index]

        while index > 0 and array[index - 1] > current_element:
            array[index] = array[index - 1]
            index -= 1

        array[index] = current_element
