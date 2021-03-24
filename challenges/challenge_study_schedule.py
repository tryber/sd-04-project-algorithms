def study_schedule(start_time, end_time, target_time):
    result = [
        index
        for index, time in enumerate(start_time)
        if time <= target_time <= end_time[index]
    ]

    return len(result)
