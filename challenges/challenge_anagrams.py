def insert_sort(iterable):
    listed = list(iterable)
    swapping = False

    while swapping:
        swapping = False
        for index, item in enumerate(listed):
            if (index + 1 < len(item)) and item < listed[index + 1]:
                listed[index], listed[index + 1] = (
                    listed[index + 1],
                    listed[index],
                )
                swapping = True

    return listed


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    return insert_sort(first_string) == insert_sort(second_string)
