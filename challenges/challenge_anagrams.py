def is_anagram(first_string, second_string):
    if (len(first_string) == len(second_string)):
        x = [data for data in first_string]
        y = [data for data in second_string]
        return(set(x) == set(y))

    return False
