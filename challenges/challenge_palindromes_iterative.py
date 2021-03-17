from collections import deque


def is_palindrome_iterative(word):
    fila = deque(word)
    for _ in range(len(word) + 1):
        # print(f"fila em cada volta {fila}")
        if len(fila) == 0:
            # print("chagou no len0")
            return False
        elif len(fila) == 1:
            # print(f"chagou no len0 {len(fila)}")
            return True
        else:
            if fila[0] != fila[-1]:
                return False
            else:
                fila.pop()
                fila.popleft()
