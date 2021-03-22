def is_anagram(first_string, second_string):
    # anagrama simples com sorted
    if sorted(first_string) == sorted(second_string):
        return True
    return False


# print(is_anagram("amor", "roma"))
# print(is_anagram("trybe", "roma"))
