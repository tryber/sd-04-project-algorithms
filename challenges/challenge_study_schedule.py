""" Toda vez que uma pessoa estudante abre o sistema, é cadastrado no
banco de dados o horário de entrada (start_time). Da mesma forma
funciona quando o estudante sai do sistema, é cadastrado no banco
de dados o horário de saída (end_time).

Seu trabalho é descobrir qual o melhor horário para disponibilizar
os conteúdos. Para achar o horário, utilize força bruta. Ou seja,
para achar o melhor horário, passe valores diferentes para a variável
target_time, analisando o retorno da função.
Dica: Quando vou saber qual o melhor horário? Quando o contador
retornado pela função for o maior.
 """


def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    result = 0
    if not start_time:
        return result
    # Se o tempo de entrada for menor ou igual ao tempo escolhido
    # e se o tempo escolhido for menor ou igual que o horário de saída
    # acrescenta +1 no resultado
    for i in range(len(end_time)):
        if target_time <= end_time[i]:
            if start_time[i] <= target_time:
                result += 1

    return result
