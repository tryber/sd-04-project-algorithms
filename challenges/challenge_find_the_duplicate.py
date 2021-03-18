def find_duplicate(nums):
    if nums == [] or len(nums) < 2:
        return False

    sorted_nums = sorted(nums)

    for i, sn in enumerate(sorted_nums):
        if type(sn) is str or sn < 0:
            return False
        elif (
            i < (len(sorted_nums) - 1) and sorted_nums[i] == sorted_nums[i + 1]
        ):
            return sorted_nums[i]
    return False
