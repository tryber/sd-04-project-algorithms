def find_duplicate(nums):
    # dica - ordenar o array
    nums.sort()

    for index in range(len(nums) - 1):
        if type(nums[index]) == str or nums[index] < 0:
            return False
        if nums[index] == nums[index + 1]:
            return nums[index]

    return False
