def study_schedule(start_time, end_time, target_time):
    students_simultaneously = 0

    if not start_time or not target_time:
        return 0

    students = len(start_time)
    for student in range(students):
        if start_time[student] <= target_time <= end_time[student]:
            students_simultaneously += 1
    return students_simultaneously
