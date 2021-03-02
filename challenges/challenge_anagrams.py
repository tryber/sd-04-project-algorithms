def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) <= 1 or len(second_string) <= 1:
        return False

    # converte cada string em uma lista
    lista1 = list(first_string)
    lista2 = list(second_string)
    # ordenando alfabeticamente
    lista1.sort()
    lista2.sort()

    pos = 0
    iguais = True

    # comparando os valores das duas listas
    while pos < len(first_string) and iguais:
        if lista1[pos] == lista2[pos]:
            pos = pos + 1
        else:
            iguais = False

    return iguais
