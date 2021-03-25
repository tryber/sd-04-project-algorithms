def find_duplicate(nums):
    ordered_nums = sorted(nums)
    if len(nums) > 1:
        for i, number in enumerate(ordered_nums):
            if type(number) != int or number < int(0):
                return False
            if number == ordered_nums[i - 1]:
                return number
    return False
