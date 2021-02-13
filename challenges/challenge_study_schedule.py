# estudante     1  2  3  4  5  6
# start_time = [2, 1, 2, 1, 4, 4]
# end_time   = [2, 2, 3, 5, 5, 5]

# target_time = 5  # saída: 3
# target_time = 4  # saída: 3
# target_time = 3  # saída: 2
# target_time = 2  # saída: 4
# target_time = 1  # saída: 2


def study_schedule(start_time, end_time, target_time):
    # if start_time == [] or end_time == []:
    #     return 0

    students_online = 0
    both_times = start_time + end_time

    for index, both_time in enumerate(both_times):
        if start_time == [] or end_time == [] or index == len(start_time):
            return students_online
        else:
            pair = [both_time] + [both_times[int(index + len(both_times) / 2)]]
            for n in range(pair[0], pair[1] + 1):
                if n == target_time:
                    students_online += 1


start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]
target_time = 5
print(study_schedule(start_time, end_time, target_time))
