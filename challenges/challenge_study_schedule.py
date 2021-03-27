def study_schedule(start_time, end_time, target_time):
    count = 0
    if start_time == [] or end_time == 0:
        return count
    for i in range(len(end_time)):
        if target_time <= end_time[i]:
            if start_time[i] <= target_time:
                count = count + 1

    return count