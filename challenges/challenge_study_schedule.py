def study_schedule(start_time, end_time, target_time):
    count = 0
    for i, number in enumerate(start_time):
        if start_time[i] <= target_time <= end_time[i]:
            count += 1
    return count
