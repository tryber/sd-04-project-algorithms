def find_duplicate(nums):
    for x in nums:
        if type(x) is str or x < 0:
            return False
        if nums.count(x) > 1:
            return x
    return False
