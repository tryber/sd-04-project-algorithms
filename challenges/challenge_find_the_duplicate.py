def find_duplicate(nums):
    for n in nums:
        if type(n) is str or n < 0:
            return False
        if nums.count(n) > 1:
            return n
    return False
