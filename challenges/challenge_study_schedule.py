def study_schedule(start_time, end_time, target_time):

    melhor_horario = 0

    for i in range(len(start_time)):
        if start_time[i] <= target_time and target_time <= end_time[i]:
            return melhor_horario += 1

    return melhor_horario
