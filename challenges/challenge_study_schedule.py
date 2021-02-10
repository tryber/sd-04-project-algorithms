def study_schedule(start_time, end_time, target_time):
    temp = 0
    if not start_time or not end_time or target_time == 0:
        return 0
    for index, element in enumerate(end_time):
        if element >= target_time:
            if start_time[index] <= target_time:
                temp += 1
    return temp
