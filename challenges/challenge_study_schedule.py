def study_schedule(start_time, end_time, target_time):
    count = 0
    if len(start_time) == 0 or target_time == 0:
        return 0
    else:
        for number in enumerate(start_time):
            if start_time[number] <= target_time <= end_time[number]:
                    count += 1
    return count
