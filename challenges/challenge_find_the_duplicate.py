def find_duplicate(nums):
    if nums == [] or type(nums[0]) == str or len(nums) == 1:
        return False
    ordered = sorted(nums)
    for index in range(len(ordered) - 1):
        saved = ordered[index]
        if ordered[index] <= 0:
            return False
            break
        if saved == ordered[index + 1]:
            return saved
    return False
