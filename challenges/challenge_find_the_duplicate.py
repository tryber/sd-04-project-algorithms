def find_duplicate(nums):
    sorted_nums = sorted(nums)
    size = len(nums)

    if size <= 1 or isinstance(sorted_nums[0], str):
        return False

    for i in range(size - 1):
        actual_number = sorted_nums[i]
        if actual_number < 0:
            break
        if actual_number == sorted_nums[i + 1]:
            return actual_number

    return False