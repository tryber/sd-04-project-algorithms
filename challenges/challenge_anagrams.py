def is_anagram(first_string, second_string):
    if (len(first_string) == len(second_string)):
        first = [letter for letter in first_string]
        second = [letter for letter in second_string]

        return(set(first) == set(second))

    return False