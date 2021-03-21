def merge_by_sort(first, second):
    merged = ''
    first_i, second_i = 0, 0
    while first_i < len(first) and second_i < len(second):
        print('first_i', first_i)
        print('second_i', second_i)
        if first[first_i] <= second[second_i]:
            merged = merged + first[first_i]
            first_i += 1
        else:
            merged = merged + second[second_i]
            second_i += 1
    if first_i >= len(first):
        print('inside if')
        for index in range(second_i, len(second)):
            merged = merged + second[index]
    else:
        print('inside else')
        for index in range(first_i, len(first)):
            merged = merged + first[index]

    return merged

print(merge_by_sort('bbc', 'aaz'))

def sort_with_merge(string):
    pass


def is_anagram(first_string, second_string):
    return sort_with_merge(first_string) == sort_with_merge(second_string)
