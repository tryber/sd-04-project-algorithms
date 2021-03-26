def find_duplicate(nums):
    for number in nums:
        if(type(number) is str or number < 0):
            return False
        if(nums.count(number) > 1):
            return number
    return False
