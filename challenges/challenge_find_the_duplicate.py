def verify_negative(nums):
    solution = True
    for num in nums:
        if num < 0:
            solution = False
            break
    return solution


def verify_types(nums):
    if not nums:
        return False
    elif type(nums[0]) is str:
        return False
    elif len(nums) <= 1:
        return False
    elif not verify_negative(nums):
        return False
    return True


def verify_load(nums_load, num_atual):
    solution = True
    if len(nums_load) == 0 or len(nums_load) == 1:
        return solution
    for num in nums_load:
        if num_atual == num:
            solution = False
            break
    return solution


def loop_find(nums, num_atual, inspect, len_num):
    new_count = 0
    while inspect < len_num:
        if nums[inspect] == num_atual:
            new_count += 1
        inspect += 1
    return new_count


def find_duplicate(nums):
    if not verify_types(nums):
        return False

    nums_load = []
    count = 0
    solution = -1
    nums_len = len(nums) - 1

    while nums_len > -1:
        new_count = 0
        inspect = 0
        num_atual = nums[nums_len]
        if verify_load(nums_load, num_atual):
            nums_load.append(num_atual)
            new_count = loop_find(nums, num_atual, inspect, nums_len)
        if new_count > count:
            solution = num_atual
            count = new_count
        nums_len -= 1

    return solution if solution != -1 else False
