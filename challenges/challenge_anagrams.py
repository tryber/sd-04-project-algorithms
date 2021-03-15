# referencias de estudo:
# https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html#lst-anagramsolution
# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
# https://realpython.com/sorting-algorithms-python/


def verify_list_size(x, y):
    if len(x) != len(y):
        return False


def iterate_counter(first_string, second_string, count1, count2):
    for i in first_string:
        count1[ord(i)] += 1
    for i in second_string:
        count2[ord(i)] += 1


def is_anagram(first_string, second_string):
    NO_OF_CHARS = 256  # - Assumo que caracteres são armazenados usando 8 bits
    # e pode haver 256 caracteres possíveis.

    # Crio 2 arrays de valores iniciando no 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    # Incrementa o contador para cada caracter da string
    # cada uma em um array
    iterate_counter(first_string, second_string, count1, count2)

    # Verifica o tamanho dos arrays.
    verify_list_size(first_string, second_string)

    # Compara a posição nos arrays
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return False

    return True


# - Apesar de considerar a solução abaixo mais compreensivel a mesma
# possui alta complexidade, mantive para fins de estudo.

# def is_anagram(first_string, second_string):
#     if len(first_string) != len(second_string):
#         return False

#     alist = list(second_string)
#     pos1 = 0

#     while pos1 < len(first_string) and True:
#         pos2 = 0
#         while pos2 < len(alist) and not False:
#             if first_string[pos1] == alist[pos2]:
#                 found = True
#             else:
#                 pos2 = pos2 + 1

#         if found:
#             alist[pos2] = None
#         else:
#             return False
#         pos1 = pos1 + 1

#     return True


print(is_anagram("AAAAB", "BBBBA"))
