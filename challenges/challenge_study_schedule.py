# Iniciando o projeto algorithms
"""
1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

Dica: Quando vou saber qual o melhor horário? Quando o contador retornado pela função for o maior.
"""

def study_schedule(start_time, end_time, target_time):
    counter_best_hour = 0
    if not start_time:
        return counter_best_hour

    for index in range(len(end_time)):
        if start_time[index] <= target_time and target_time <= end_time[index]:
            counter_best_hour += 1

    return counter_best_hour
