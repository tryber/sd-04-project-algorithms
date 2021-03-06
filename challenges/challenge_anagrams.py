def sort_me_this_please(word):
    word_listed = list(word)
    i = 0
    while i < len(word_listed):
        minimum = i
        j = i + 1
        while j < len(word_listed):
            if word_listed[j] < word_listed[minimum]:
                minimum = j
            j += 1
        temp = word_listed[minimum]
        word_listed[minimum] = word_listed[i]
        word_listed[i] = temp
        i += 1
    return word_listed


def is_anagram(first_string, second_string):
    if (len(first_string) < 1 or len(second_string) < 1):
        return False
    # sorted_first = sorted(first_string)
    # sorted_second = sorted(second_string)
    sorted_first = sort_me_this_please(first_string)
    sorted_second = sort_me_this_please(second_string)
    output = True
    for index, letter in enumerate(sorted_first):
        if sorted_first[index] != sorted_second[index]:
            output = False
    return output
