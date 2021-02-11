def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    sorted_first = sorted(first_string)
    sorted_second = sorted(second_string)
    # print(sorted_first)
    # print(sorted_second)
    # print(len(sorted_first))
    output = True
    for index, letter in enumerate(sorted_first):
        # print(sorted_first[index] != sorted_second[index])
        if sorted_first[index] != sorted_second[index]:
            # print("inside if", sorted_first[index])
            output = False
    return output
