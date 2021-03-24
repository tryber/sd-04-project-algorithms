def study_schedule(start_time, end_time, target_time):
    studing = 0
    for i in range(len(start_time)):
        if end_time[i] >= target_time >= start_time[i]:
            studing += 1

    return studing