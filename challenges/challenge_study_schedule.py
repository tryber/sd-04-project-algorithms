def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    student = 0
    for index, hour in enumerate(start_time):
        if hour <= target_time <= end_time[index]:
            student += 1
    return student
