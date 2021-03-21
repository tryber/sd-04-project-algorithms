def study_schedule(start_time, end_time, target_time):
    count = 0
    if target_time == "":
        return 0
    for number in enumerate(start_time):
        if start_time[number] <= target_time <= end_time[number]:
            count += 1
    return count
