def study_schedule(start_time, end_time, target_time):
    people = 0
    for index, hour in enumerate(start_time):
        if hour <= target_time <= end_time[index]:
            people += 1
    return people
