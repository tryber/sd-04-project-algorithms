start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]
target_time = 5


def study_schedule(start_time, end_time, target_time):
    counter = 0
    if start_time is None or target_time is None:
        return counter
    for x in range(len(start_time)):
        if start_time[x] <= target_time <= end_time[x]:
            counter += 1
    return counter
