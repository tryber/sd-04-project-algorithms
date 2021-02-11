def is_anagram(first_string, second_string):
    if (len(first_string) < 1 or len(second_string) < 1):
        return False
    sorted_first = sorted(first_string)
    sorted_second = sorted(second_string)
    output = True
    for index, letter in enumerate(sorted_first):
        if sorted_first[index] != sorted_second[index]:
            output = False
    return output
