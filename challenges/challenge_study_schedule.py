def study_schedule(start_time, end_time, target_time):

    melhor_horario = 0

    for i in range(len(start_time)):
        if start_time[i] <= target_time and target_time <= end_time[i]:
            return melhor_horario += 1

    return melhor_horario

# melhor_horario (=== quantidade_de_estudantes)
# estudantes = [1, 2, 3, 4, 5]
# start_time = [2, 3, 2, 1, 2]
# end_time = [5, 4, 3, 4, 5]
# print(study_schedule(start_time, end_time, 4))
