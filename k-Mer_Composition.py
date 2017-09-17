'''==== k-Mer Composition ======

Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.'''

import itertools

def parse_fasta(filename):
    infile = open(filename, 'r')
    sequence = ''
    for line in infile.readlines():
        if not line.startswith('>'):
            sequence += line.rstrip('\n')
    return sequence    

def kmer_composition(k, dna):
    # input length k and DNA string, returns kmer composition array

    query_list = []
    for elem in itertools.product('ACGT', repeat=k):
        query_list.append(''.join(elem))
    # build a list of all possible kmers (length <k>) ordered lexographically

    matrix = ''
    for kmer in query_list:
        count = 0
        for i in range(len(dna)):
            if dna[i:i+k] == kmer:
                count += 1        
        matrix += str(count) + ' '
    # return matrix of count of each possible kmer in dna sequence <dna>
    return matrix
    

# do the work

dna = parse_fasta('dna.txt')
print kmer_composition(4, dna)
