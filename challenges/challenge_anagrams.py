def is_anagram(first_string, second_string):
    def qsort(string):
        inlist = list(string)
        if inlist == []:
            return []
        else:
            pivot = inlist[0]
            lesser = qsort([x for x in inlist[1:] if x < pivot])
            greater = qsort([x for x in inlist[1:] if x >= pivot])
            return lesser + [pivot] + greater

    primeira = ''.join(qsort(first_string))
    segunda = ''.join(qsort(second_string))

    return primeira == segunda
