def study_schedule(start_time, end_time, target_time):
    if start_time is None or end_time is None:
        return 0
    counter = 0
    for x in range(len(start_time)):
        if start_time[x] <= target_time <= end_time[x]:
            counter += 1
    return counter
