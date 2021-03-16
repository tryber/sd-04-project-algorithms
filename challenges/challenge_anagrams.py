def is_anagram(first_string, second_string):

    if len(first_string) != len(second_string):
        return False

    if sort(first_string) == sort(second_string):
        return True

    return False


def sort(word):

    lista = list(word)

    for index in range(0, len(lista)):
        current_element = lista[index]

        while index > 0 and lista[index - 1] > current_element:
            lista[index] = lista[index - 1]
            index -= 1

        lista[index] = current_element

    return lista
