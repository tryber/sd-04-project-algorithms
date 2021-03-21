def study_schedule(start_time, end_time, target_time):
    total_of_students_at_target_time = 0
    for index, student_start_time in enumerate(start_time):
        is_online = student_start_time <= target_time and target_time <= end_time[index]
        if(is_online): total_of_students_at_target_time += 1
    return total_of_students_at_target_time
