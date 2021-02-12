def find_duplicate(nums):
    try:
        sorted_nums = sorted(nums)
        range_nums = range(len(sorted_nums) - 1)
        for i in range_nums:
            if sorted_nums[i] <= 0:
                break
            if sorted_nums[i] == sorted_nums[i + 1]:
                return sorted_nums[i]
        return False
    except TypeError:
        return False
