RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def transcribe(sequence, introns):
    # takes sequence, removes introns and replaces thymine with uracil
    for item in introns:
        sequence = sequence.replace(item, '')
    rna = sequence.replace('T', 'U')
    return rna
    
def translate(coding_sequence):
    stop = False
    protein = ''
    for i in range(len(coding_sequence)/3):
        codon = coding_sequence[i*3:i*3+3]
        if codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
            stop = True
        if stop == False:
            protein += RNA_CODON_TABLE[codon]
    return protein

#=== brutish parser ===      
infile = open('dna.txt', 'r')
sequence = ''
introns = []
count = 0
for line in infile.readlines():
    if line.startswith('>'):
        count += 1
    else:
        if count == 1:
            sequence += line.rstrip('\n')
        else:
            if len(introns) == count - 1:
                introns[count - 2] += line.rstrip('\n')
            else:
                introns.append(line.rstrip('\n'))         
    
rna = transcribe(sequence, introns)
protein = translate(rna)

print protein
