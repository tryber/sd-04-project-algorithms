def find_duplicate(nums):
    order = sorted(nums)
    if len(nums) > 1:
        for i, number in enumerate(order):
            if type(number) != int or number < int(0):
                return False
            # print(number, order[i])
            # compara o numero com o próximo da lista
            if number == order[i - 1]:
                return number
    return False


# print(find_duplicate([1, 3, 4, 2, 2]))
# print(find_duplicate([7, 3, 4, 4, 2, 1, 5, 3]))
