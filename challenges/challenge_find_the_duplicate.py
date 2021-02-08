def find_duplicate(nums):
    if len(nums) <= 1 or len(nums) == len(set(nums)):
        return False
    for item in nums:
        if type(item) == str or item < 0:
            return False

    # dica - ordenar o array nums
    nums.sort()

    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            return nums[index]

    return False
