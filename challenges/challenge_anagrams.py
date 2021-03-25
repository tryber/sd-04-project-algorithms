# https://stackoverflow.com/questions/3855537/fastest-way-to-sort-in-python

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

    first_word = ''.join(qsort(first_string))
    second_word = ''.join(qsort(second_string))

    return first_word == second_word
