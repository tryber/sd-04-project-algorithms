def study_schedule(start_time, end_time, target_time):
    counter = 0
    if not start_time or not target_time:
        return counter

    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            counter += 1

    return counter
