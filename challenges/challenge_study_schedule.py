# Iniciando o projeto algorithms
"""
1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

Dica: Quando vou saber qual o melhor horário? Quando o contador retornado pela função for o maior.
"""

def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    count_best_hour = 0
    if not start_time:
        return count_best_hour

    
