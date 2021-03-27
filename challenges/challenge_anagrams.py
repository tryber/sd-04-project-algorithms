def loops_anagram(first_string, second_string, len1, len2):
    solution = True
    while len2 > -1:
        solution = False
        if first_string[len1] == second_string[len2]:
            solution = True
            break
        len2 -= 1
    return solution


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if not len(first_string) == len(second_string):
        return False

    solution = True
    first_len = len(first_string) - 1
    second_len = len(second_string) - 1
    while solution and first_len > -1:
        solution = loops_anagram(
            first_string, second_string, first_len, second_len)
        first_len -= 1

    return solution
