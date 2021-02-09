def study_schedule(start_time, end_time, target_time):
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
