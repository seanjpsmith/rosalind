# locating restriction sites

from string import maketrans

def reverse_complement(dna):
    # takes dna and returns reverse complement
    trantab = maketrans('ATGC', 'TACG')
    return dna[::-1].translate(trantab)
    
def is_reverse_palendrome(dna):
    # returns true for reverse palendromic sequence
    if reverse_complement(dna) == dna:
        return True

def print_reverse_palendromes(sequence):
    # prints location and length of reverse palendromes wile length between 4 and 12
    for loci in range(len(sequence)):
        for item in range(4, 13):
            oligo = sequence[loci:loci+item]
            if is_reverse_palendrome(oligo) and len(oligo) == item:
                print loci + 1, item

infile = open('dna.txt', 'r')
sequence = ''
for line in infile.readlines():
    if not line.startswith('>'):
        sequence += line.rstrip('\n')
    
print_reverse_palendromes(sequence)
