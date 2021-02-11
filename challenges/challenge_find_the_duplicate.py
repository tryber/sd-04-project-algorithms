def find_duplicate(nums):
    if len(nums) < 2:
        return False
    # print(nums)
    # sorted_nums = nums.sort()
    sorted_nums = sorted(nums)
    # print(sorted_nums)
    n_minus_one = sorted_nums[0]
    for num in sorted_nums:
        if n_minus_one == num:
            return False
        n_minus_one = num
