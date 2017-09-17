#protein_tranlsation_problem

dict = {'ACC': 'T', 'GCA': 'A', 'AAG': 'K', 'AAA': 'K', 'GUU': 'V', 'AAC': 'N', 'AGG': 'R', 'UGG': 'W', 'GUC': 'V', 'AGC': 'S', 'ACA': 'T', 'AGA': 'R', 'AAU': 'N', 'ACU': 'T', 'GUG': 'V', 'CAC': 'H', 'ACG': 'T', 'AGU': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'CGA': 'R', 'CAG': 'Q', 'CGC': 'R', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'CCU': 'P', 'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'CCG': 'P', 'UCC': 'S', 'UAC': 'Y', 'CGU': 'R', 'GAA': 'E', 'AUA': 'I', 'AUC': 'I', 'CUU': 'L', 'UCA': 'S', 'AUG': 'M', 'UGA': '\n', 'CUG': 'L', 'GAG': 'E', 'AUU': 'I', 'CAU': 'H', 'CUA': 'L', 'UAA': '\n', 'GCC': 'A', 'UUU': 'F', 'GAC': 'D', 'GUA': 'V', 'UGC': 'C', 'GCU': 'A', 'UAG': '\n', 'CUC': 'L', 'UUG': 'L', 'UUA': 'L', 'GAU': 'D', 'UUC': 'F'}

rna = ''

n = 0
protein = ''

while n < len(rna):
    protein += str(dict[rna[n:n+3]])
    n += 3
    
print protein