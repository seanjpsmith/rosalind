#skew_problem

# length of k-mer
k = 5

#length of sequence
L = 75

# number of times pattern appears
t = 4

sequence = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'

def clump_check(seq):
    # checks a clump for k-mers occuring t or more times
    
    #build a dictionary of k-mers with sequence as key and value as frequency
    kmers = {}
    for i in range (len(seq) - k + 1):
        if not kmers.has_key(seq[i:i+k]):
            kmers[seq[i:i+k]] = 1
        else:
            kmers[seq[i:i+k]] = kmers[seq[i:i+k]] + 1
    
    # return a list of all kers occuring more than t or more times
    ltmers = []
    for key in kmers:
        if kmers[key] >= t:
            ltmers.append(key)
    return ltmers

# check sequence for lt clumps
list_of_ltmers = []

for i in range(len(sequence) - L + 1):
    list = clump_check(sequence[i:i+L])
    for item in list:
        if item not in list_of_ltmers:
            list_of_ltmers.append(item)

print list_of_ltmers.join(',')            

    
    
    
            
    