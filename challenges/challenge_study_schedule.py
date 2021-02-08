start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]
target_time = 0


def study_schedule(start_time, end_time, target_time):
    answer = 0
    if not start_time:
        return answer
    # ------------- Primeiro Código-----------
    # for i in range(len(end_time)):
    #     if target_time <= end_time[i]:
    #         if start_time[i] <= target_time:
    #             answer += 1

    # ------------- Primeira refatoração -----------
    # for i in range(len(end_time)):
    #     if end_time[i] >= target_time >= start_time[i]:
    #         answer += 1

    # ------------- Código final (Pythonic)-----------
    for input, end_time in zip(start_time, end_time):
        if input <= target_time <= end_time:
            answer += 1

    return answer
