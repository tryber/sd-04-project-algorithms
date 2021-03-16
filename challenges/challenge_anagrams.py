# from collections import deque
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

    primeira = ''.join(qsort(first_string))
    segunda = ''.join(qsort(second_string))

    return primeira == segunda


first_string = "pedra"
second_string = "perda"

print(is_anagram(first_string, second_string))

# tempo 8.79 
# def selectionSort(frase):
#         string = list(frase)
#         n = len(frase)
#         for i in range(n):
#             # Initially, assume the first element of
#             # the unsorted part as the minimum.
#             minimum = i

#             for j in range(i+1, n):
#                 if (string[j] < string[minimum]):
#                     # Update position of minimum element
#                     # if a smaller element is found.
#                     minimum = j

#             # Swap the minimum element with the first
#             # element of the unsorted part.
#             temp = string[i]
#             string[i] = string[minimum]
#             string[minimum] = temp

#         # print(f"string {string}")
#         return string

#     primeira = ''.join(selectionSort(first_string))
#     segunda = ''.join(selectionSort(second_string))

#     return primeira == segunda
