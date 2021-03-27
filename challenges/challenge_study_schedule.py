def study_schedule(start_time, end_time, target_time):
    solution = 0
    loop_index = 0

    for person_start in start_time:
        comparation = person_start
        person_close = end_time[loop_index]
        dif = person_close - person_start
        while dif != -1:
            if comparation == target_time:
                solution += 1
            comparation += 1
            dif -= 1
        loop_index += 1

    return solution
