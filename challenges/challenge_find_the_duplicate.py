def find_duplicate(nums):
    try:
        _ = nums[1] + 1
        order = sorted(nums)
        index = 0
        for num in range(len(order) - 1):
            # print(f"order, {order}")
            # print(f"num, {num}")
            if order[num] == order[index + 1]:
                if order[num] < 0:
                    return False
                else:
                    return order[num]
            else:
                # print(f"index antes, {index}")
                # print(f"num = {order[num]}, seguinte = {order[index + 1]}")
                index += 1
                # print(f"index depois, {index}")
        return False
    except TypeError:
        return False
    except IndexError:
        return False


# nums = [3, 1, 2, 4, 6, 5, 7, 8]
# nums2 = [-1, -1]

# print(find_duplicate(nums2))
