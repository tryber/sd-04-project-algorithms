def study_schedule(start_time, end_time, target_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            count += 1
    return count


# print(study_schedule([4, 1, 3, 2], [4, 3, 4, 5], 2))
# print(study_schedule([4, 1, 3, 2], [4, 3, 4, 5], 3))
# print(study_schedule([4, 1, 3, 2], [4, 3, 4, 5], 5))
