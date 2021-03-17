def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string) \
            or first_string == '' or second_string == '':
        return False
    x = []
    y = []

    for i_first, letter_first in enumerate(first_string):
        for i_second, letter_second in enumerate(second_string):
            if letter_first == letter_second \
                    and i_first <= len(first_string) - 1:
                x.append(letter_first)
                second_string.replace(letter_second, '')
                break
            elif letter_first != letter_second \
                    and i_second == len(second_string) - 1:
                y.append(letter_first)

    z = ''.join(x)
    if z == first_string and y == []:
        return True
    else:
        return False


# def sort_string(word):
#     word_letters = list(word)

#     return string_to_array


# def is_anagram(first_string, second_string):
#     if len(first_string) != len(second_string) \
#             or first_string == '' or second_string == '':
#         return False

#     if sort_string(first_string) == sort_string(second_string):
#         return True
#     else:
#         return False

#     return False

# def sort(word):

#     lista = list(word)

#     for index in range(0, len(lista)):
#         current_element = lista[index]

#         while index > 0 and lista[index - 1] > current_element:
#             lista[index] = lista[index - 1]
#             index -= 1

#         lista[index] = current_element

#     return lista


# def is_anagram(first_string, second_string):

#     if first_string is None or second_string is None:
#         return False

#     if len(first_string) != len(second_string):
#         return False

#     if sort(first_string) == sort(second_string):
#         return True

#     return False


first_string = "pedra"
second_string = "perdaaa"

# first_string = "pedra"
# second_string = "pedro"

# first_string = "pedra"
# second_string = "perda"

# first_string = ""
# second_string = "perda"

# first_string = "pedra"
# second_string = ""

# print(sort_string(first_string))
# print(sort_string(second_string))
print(is_anagram(first_string, second_string))
