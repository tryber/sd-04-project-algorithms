def study_schedule(start_time, end_time, target_time):
    counter = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time and target_time <= end_time[i]:
            counter += 1

    return counter
