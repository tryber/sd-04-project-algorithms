def is_anagram(first_string, second_string):

    if (len(first_string) != len(second_string)):
        return False

    word_dic = {}

    # n iterations
    for char in first_string:
        if word_dic.get(char):
            word_dic[char] += 1
        else:
            word_dic[char] = 1

    # n iterations
    for char in second_string:
        if word_dic.get(char):
            word_dic[char] -= 1
        else:
            return False

    # n iterations
    for v in word_dic.values():
        if v != 0:
            return False

    return True
