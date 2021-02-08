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
    for start_time, end_time in zip(start_time, end_time):
        if start_time <= target_time <= end_time:
            answer += 1

    return answer
