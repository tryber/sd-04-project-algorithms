def find_duplicate(nums):
    sorted_nums = sorted(nums)

    for i, sn in enumerate(sorted_nums):
        while i < len(sorted_nums):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return True
            else:
                i += 1
        return False


nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
print(find_duplicate(nums))
