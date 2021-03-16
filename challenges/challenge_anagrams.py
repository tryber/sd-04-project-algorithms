def merge(le, r, m):
    left = 0
    right = 0
    while left < len(le) and right < len(r):
        if le[left] <= r[right]:
            m[left + right] = le[left]
            left += 1
        else:
            m[left + right] = r[right]
            right += 1
    for right in range(right, len(r)):
        m[left + right] = r[right]
    for left in range(left, len(le)):
        m[left + right] = le[left]
    return m


def merge_sort(obj):
    if len(obj) <= 1:
        return obj
    mid = len(obj) // 2
    left = merge_sort(obj[:mid])
    right = merge_sort(obj[mid:])
    return merge(left, right, obj.copy())


def is_anagram(first_string, second_string):
    if first_string == "":
        return False
    if second_string == "":
        return False
    else:
        first = "".join(merge_sort(list(first_string)))
        second = "".join(merge_sort(list(second_string)))
    for i in range(len(first)):
        if first[i] != second[i]:
            return False
    return True
