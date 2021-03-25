# http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """

    def verify_word(string):
        inlist = list(string)
        if inlist == []:
            return []
        else:
            pivot = inlist[0]
            lesser = verify_word([x for x in inlist[1:] if x < pivot])
            greater = verify_word([x for x in inlist[1:] if x >= pivot])
            return lesser + [pivot] + greater

    f_word = "".join(verify_word(first_string))
    s_word = "".join(verify_word(second_string))

    return f_word == s_word
