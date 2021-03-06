def is_anagram(first_string, second_string):

    counter1 = {}
    for c in first_string.lower():
        counter1[c] = counter1.get(c, 0) + 1
    counter2 = {}
    for c in second_string.lower():
        counter2[c] = counter2.get(c, 0) + 1

    return counter1 == counter2
