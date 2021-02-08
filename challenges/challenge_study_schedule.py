def study_schedule(start_time, end_time, target_time):
    if not start_time or not target_time:
        return 0
    contador = 0
    for index, value in enumerate(start_time):
        if value <= target_time and end_time[index] >= target_time:
            contador += 1
    return contador
