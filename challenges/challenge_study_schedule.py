def study_schedule(start_time, end_time, target_time):
    target_time_counter = 0
    if len(start_time) > 0:
        for i in range(len(end_time)):
            if target_time in range(start_time[i], end_time[i] + 1):
                target_time_counter += 1
    return target_time_counter
