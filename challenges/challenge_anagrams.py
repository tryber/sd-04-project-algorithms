def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    if sorted(first_string) == sorted(second_string):
        return True
    return False

    # char_qty = dict()

    # for i in first_string:
    #     if i in char_qty:
    #         char_qty[i] += 1
    #     else:
    #         char_qty[i] = 1

    # for i in second_string:
    #     if i in char_qty:
    #         char_qty[i] -= 1
    #     else:
    #         char_qty[i] = 1

    # for i in char_qty:
    #     if char_qty[i] != 0:
    #         return False
    # return True
