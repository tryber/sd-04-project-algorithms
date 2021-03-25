# https://pt.stackoverflow.com/questions/216413/identificar-elementos-repetidos-em-lista-com-python


def find_duplicate(nums):
    length = len(nums)
    if length <= 1 or isinstance(nums[0], str):
        return False
    sorted_nums = sorted(nums)
    for i in range(length - 1):
        if sorted_nums[i] <= 0:
            break
        if sorted_nums[i] == sorted_nums[i + 1]:
            return sorted_nums[i]
    return False
