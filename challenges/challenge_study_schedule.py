def study_schedule(start, end, target):
    count = 0
    if start == [] or target == 0:
        return 0
    for index in range(len(start)):
        if start[index] <= target <= end[index]:
            count += 1
    return count
