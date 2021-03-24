def study_schedule(start_time, end_time, target_time):
    studing = 0
    for start, end in zip(start_time, end_time):
        if start >= target_time >= end:
            studing += 1

    return studing
