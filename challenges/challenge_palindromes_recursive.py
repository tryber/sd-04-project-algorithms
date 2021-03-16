from collections import deque


def is_palindrome_recursive(word, low, high):

    fila = deque(word)
    # print(f"fila em cada volta {fila}")

    if len(fila) == 0:
        # print("chagou no len0")
        return False

    elif len(fila) == 1:
        # print(f"chagou no len1 {len(fila)}")
        return True

    else:
        # print('entrou no else')
        if fila[0] != fila[-1]:
            # print('primeiro e ultimo diferentes')
            return False
        else:
            # print('entrou no segundo else')
            fila.pop()
            fila.popleft()
            if len(fila) == 0:
                # print('true com quantidade par')
                return True
            else:
                word = ''.join(fila)
                # print(f"word {word}")
                return is_palindrome_recursive(word, 0, len(word) - 1)


# word = 'bccb'
# print(is_palindrome_recursive(word, 0, len(word) - 1))
# nao eh recursiva, mas funciona
# fila = deque(word)
#     for _ in range(len(word) + 1):
#         # print(f"fila em cada volta {fila}")
#         if len(fila) == 0:
#             # print("chagou no len0")
#             return False
#         elif len(fila) == 1:
#             # print(f"chagou no len0 {len(fila)}")
#             return True
#         else:
#             if fila[0] != fila[-1]:
#                 return False
#             else:
#                 fila.pop()
#                 fila.popleft()
