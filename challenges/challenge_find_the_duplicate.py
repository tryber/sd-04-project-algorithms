from statistics import multimode


def find_duplicate(nums):
    if not nums or len(nums) == 1:
        return False

    num_list = multimode([x for x in nums if isinstance(x, int) and x >= 0])

    if not num_list or len(num_list) > 1:
        return False

    return num_list[0]
