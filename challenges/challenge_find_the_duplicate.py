def find_duplicate(nums):
    """ Faça o código aqui. """

    # verifica se lista está vazia
    # ou tem apenas um elemento
    if len(nums) <= 1:
        return False

    # lista alfabeto
    string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z']

    # cont_duplicate dicionário que armazena todas as duplicidades
    cont_duplicate = {}

    # most_frequent variável que guarda o número mais frequente
    # inicializa com o primeiro elemento da lista (nums[0])
    most_frequent = nums[0]

    # contando os itens e adicionando no dic(cont_duplicate)
    for num in nums:
        # verifica se a lista contém letras ou números negativos.
        if num in string or num < 0:
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
