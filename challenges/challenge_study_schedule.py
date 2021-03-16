# start = [2, 1, 2, 1, 4, 4]
# end = [2, 2, 3, 5, 5, 5]
# alvo = 5


def study_schedule(start_time, end_time, target_time):
    """ recebendo dois array descubra qual hora eh a mais utilizada
    se recber 1 array vazio ou target =0 retorna zero """
    dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    if len(start_time) == 0 or target_time == 0:
        return 0
    else:
        for hora_a in range(len(start_time)):
            contador = start_time[hora_a]
            if start_time[hora_a] == end_time[hora_a]:
                dicionario[start_time[hora_a]] += 1
            else:
                for _ in range((end_time[hora_a] - start_time[hora_a]) + 1):
                    dicionario[contador] += 1
                    contador += 1

    return dicionario[target_time]

    # tempo 0.034
    # dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    # if len(start_time) == 0 or target_time == 0:
    #     return 0
    # else:
    #     for hora_a in range(len(start_time)):
    #         final = end_time[hora_a]
    #         contador = start_time[hora_a]
    #         while contador <= final:
    #             dicionario[contador] += 1
    #             # print(f"{hora_a}, {contador} {dicionario}")
    #             contador += 1

    #     # print(f"dicionario {dicionario}")
    # return dicionario[target_time]

# tempo 0.045
# dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
#     if len(start_time) == 0 or target_time == 0:
#         return 0
#     else:
#         for hora_a in range(len(start_time)):
#             contador = start_time[hora_a]
#             if start_time[hora_a] == end_time[hora_a]:
#                 dicionario[start_time[hora_a]] += 1
#             else:
#                 for _ in range((end_time[hora_a] - start_time[hora_a]) + 1):
#                     dicionario[contador] += 1
#                     contador += 1

#     return dicionario[target_time]

# start = [2, 1, 2, 1, 4, 4]
# end = [2, 2, 3, 5, 5, 5]
# alvo = 5

# print(f"chamada{study_schedule(start, end, alvo)}")
