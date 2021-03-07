def find_duplicate(nums):
    """ Faça o código aqui. """

    # verifica se lista está vazia
    # ou tem apenas um elemento
    if len(nums) <= 1:
        return False

    # cont_duplicate dicionário que armazena todas as duplicidades
    cont_duplicate = {}

    # contando os itens e adicionando no dic(cont_duplicate)
    for num in nums:
        # verifica se a lista contém letras ou números negativos.
        if type(num) != int or num < 0:
            return False
        # caso o item não esteja no dict
        # add com o valor 1.
        if num not in cont_duplicate:
            cont_duplicate[num] = 1
        # se o item já está incluído no dict
        # incrementa o seu valor com 1.
        else:
            cont_duplicate[num] += 1

    # compara o dict com a lista,
    # se o tamanho das lista forem iguais então,
    # não existe duplicidade.
    if len(cont_duplicate) == len(nums):
        return False
    else:
        # caso exista duplicidade
        # retorna o numero mais frequente,
        return max(cont_duplicate, key=cont_duplicate.get)
