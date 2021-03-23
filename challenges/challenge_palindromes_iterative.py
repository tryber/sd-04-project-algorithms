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
        if char[inicio] == char[fim]: # Verificando o primeiro e o último caracteres no argumento
            inicio = inicio + 1   # Aumentando o valor do índice em 1
            fim = fim - 1 # Reduzindo o valor do índice em 1, porque está acessando a string por trás
            True
        else:
            False
    return True