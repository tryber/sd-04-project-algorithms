def diminui_complexidade(arr):
    index = 0
    for num in range(len(arr) - 1):
        if arr[num] == arr[index + 1]:
            if arr[num] < 0:
                return False
            else:
                return arr[num]
        else:
            index += 1
    return False


def checa_tipo(arr):
    if len(arr) < 2 or type(arr[0]) == str:
        return False
    else:
        return True


def find_duplicate(nums):
    if not checa_tipo(nums):
        return False
    order = sorted(nums)
    return diminui_complexidade(order)


nums = [3, 1, 2, 4, 6, 5, 7, 8]
nums2 = [-1, -1]
nums3 = ['a']
nums4 = ['a', 'a']
print(find_duplicate(nums4))


# try:
#         _ = nums[1] + 1
#         order = sorted(nums)
#         index = 0
#         for num in range(len(order) - 1):
#             if order[num] == order[index + 1]:
#                 if order[num] < 0:
#                 return False
#                 else:
#                 return order[num]
#             else:
#                 index += 1
#         return False
#     except TypeError:
#         return False
#     except IndexError:
#         return False
