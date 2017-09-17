'''
===== Introduction to Random Strings =====
Given: A DNA string of length at most 100 bp and an array containing 
at most 20 numbers between 0 and 1.
Return: An array having the same length as in which represents the 
common logarithm of the probability that a random string constructed 
with the GC-content found in will match exactly.
'''

import math

input = '''
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783
'''.strip('\n').split('\n')

DNA, GC_ARRAY  = list(input[0]), map(float, input[1].split())

def random_string(gc_array, dna):
    ans = []
    for item in gc_array:
        prob = 0
        for nuc in dna:
            if nuc == 'G' or nuc == 'C':
                prob += math.log10(item/2)
            elif nuc == 'A' or nuc == 'T':
                prob += math.log10((1-item)/2)
        ans.append(prob)
    return str(ans)[1:-1].replace(',','')

print random_string(GC_ARRAY, DNA)