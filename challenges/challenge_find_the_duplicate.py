# quora.com/What-is-the-python-program-for-finding-duplicate-element-from-a-list

def find_duplicate(nums):
    """ Faça o código aqui. """

    # nums.sort()
    # repeat = set()

    # for i in range(1, len(nums)):
    #     if type(nums[i]) != int or nums[i] < 0:
    #         return False
    #     if(nums[i] == nums[i-1]):
    #         repeat.add(nums[i])
    #     return repeat

    # return False

    nums.sort()

    for i in range(1, len(nums)):
        if type(nums[i]) != int or nums[i] < 0:
            return False
        if(nums[i] == nums[i-1]):
            return nums[i]

    return False

