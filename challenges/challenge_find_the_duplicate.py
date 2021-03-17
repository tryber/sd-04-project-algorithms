def find_duplicate(nums):
    try:
        _ = nums[1] + 1
        order = sorted(nums)
        index = 0
        for num in range(len(order) - 1):
            if order[num] == order[index + 1]:
                # if order[num] < 0:
                # return False
                # else:
                return order[num]
            else:
                index += 1
        return False
    except TypeError:
        return False
    except IndexError:
        return False


# nums = [3, 1, 2, 4, 6, 5, 7, 8]
# nums2 = [-1, -1]

# print(find_duplicate(nums2))
