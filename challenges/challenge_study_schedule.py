def study_schedule(start_time, end_time, target_time):
    people = 0

    if not start_time or not target_time:
        return people

    for i, current_start_time in enumerate(start_time):
        if end_time[i] >= target_time >= current_start_time:
            people += 1

    return people
