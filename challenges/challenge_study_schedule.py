def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    count = 0
    start = len(start_time)
    for i in range(start):
        if start_time[i] <= target_time <= end_time[i]:
            count += 1
    return count
