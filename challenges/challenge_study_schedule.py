def study_schedule(start_time, end_time, target_time):
    count = 0
    for index, time in enumerate(start_time):
        if time <= target_time <= end_time[index]:
            count += 1

    return count
