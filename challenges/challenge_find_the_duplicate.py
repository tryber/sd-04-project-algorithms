def find_duplicate(nums):
    """ Faça o código aqui. """
    num_checados = set()
    prim_duplicado = False

    for num in nums:
        if num < 0:
            return False
        if num in num_checados:
            prim_duplicado = num
            break
        num_checados.add(num)

    return prim_duplicado
