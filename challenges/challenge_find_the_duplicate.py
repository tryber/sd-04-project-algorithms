def find_duplicate(nums):

    nums.sort()

    for x in range(1, len(nums)):
        if type(nums[x]) != int or nums[x] < 0:
            return False
        if(nums[x] == nums[x-1]):
            return nums[x]

    return False
