def string_to_dict(str):
    char_qty = dict()

    for i in str:
        if i in char_qty:
            char_qty[i] += 1
        else:
            char_qty[i] = 1

    return char_qty


def is_anagram(first_string, second_string):
    dict1 = string_to_dict(first_string)
    dict2 = string_to_dict(second_string)

    if dict1 == dict2:
        return True
    return False
