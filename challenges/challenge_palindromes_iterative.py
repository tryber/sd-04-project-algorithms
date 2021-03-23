def is_palindrome_iterative(word):

    if (not word or word == ''):
        return False

    # Converta o argumento em uma string minúscula
    char = str(word).lower()
    size = len(char)

    # Definindo os índices para iteração
    inicio = 0
    fim = size - 1

    for i in char:
        # Verificando o 1 e o último caracteres no argumento
        if char[inicio] == char[fim]:
            inicio = inicio + 1   # Aumentando o valor do índice em 1
            # Reduz o valor do índice em 1, pq está acessando a string por trás
            fim = fim - 1
            True
        else:
            False
    return True
