def find_duplicate(nums):
    if len(nums) < 2:
        return False
    # print(nums)
    # sorted_nums = nums.sort()
    sorted_nums = sorted(nums)
    # print(sorted_nums)
    n_minus_one = 0
    for num in sorted_nums:
        if (type(num) is not int or num < 0):
            return False
        if n_minus_one == num:
            return num
        n_minus_one = num
    return False
    
