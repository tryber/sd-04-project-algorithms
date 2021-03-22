def study_schedule(start_time, end_time, target_time):
    student = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            student += 1
    return student
