def study_schedule(start_time, end_time, target_time):
    on_time = [
        i for i, time in enumerate(start_time)
        if time <= target_time <= end_time[i]
    ]

    return len(on_time)
