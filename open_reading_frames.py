
##Open Reading Frames
##====================
##
##Either strand of a DNA double helix can serve as the coding strand for RNA
##transcription. Hence, a given DNA string implies six total reading frames,
##or ways in which the same region of DNA can be translated into amino acids:
##three reading frames result from reading the string itself, whereas three
##more result from reading its reverse complement.
##
##An open reading frame (ORF) is one which starts from the start codon and
##ends by stop codon, without any other stop codons in between. Thus, a
##candidate protein string is derived by translating an open reading frame
##into amino acids until a stop codon is reached.
##
##Given: A DNA string s of length at most 1 kbp in FASTA format.
##
##Return: Every distinct candidate protein string that can be translated from
##ORFs of s. Strings can be returned in any order.
##
##
##Sample Dataset
##--------------
##>Rosalind_99
##AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
##
##Sample Output
##--------------
##MLLGSFRLIPKETLIQVAGSSPCNLS
##M
##MGMTPRLGLESLLE
##MTPRLGLESLLE


from string import maketrans

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


def reverse_complement(dna):
    # takes dna and returns reverse complement
    trantab = maketrans('ATGC', 'TACG')
    return dna[::-1].translate(trantab)

def transcribe(dna):
    # replaces T with U to return RNA
    rna = dna.replace('T', 'U')
    return rna
  
def return_start_codons(rna):
    # takes a rna string and returns a list of location of all start codons
    start_codons = []
    
    # view all 3 forward reading frames
    for i in range(3):
        sequence = rna[i:]
                
        # identify location of start codons
        for codon in range(len(sequence)/3):
            if sequence[codon*3:codon*3+3] == 'AUG':
                start_codons.append(codon*3 + i)
    return start_codons


def translate(coding_sequence):
    # takes rna reading frame and translates until stop codon, returns protein if stop codon
    stop = False
    protein = ''
    for i in range(len(coding_sequence)/3):
        codon = coding_sequence[i*3:i*3+3]
        if stop == False and codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
            stop = True
            protein += RNA_CODON_TABLE[codon]  
        if stop == False:
            protein += RNA_CODON_TABLE[codon]
        if protein[-4:] == 'Stop':
            return protein[:-4]

# open and parse fasta file
infile = open('dna.txt', 'r')
dna_string = ''
for line in infile.readlines():
    if not line.startswith('>'):
        dna_string += line.rstrip('\n')
rna = [transcribe(dna_string), transcribe(reverse_complement(dna_string))]

# get the job done
proteins = []
for sense in rna:
    start_codons = return_start_codons(sense)
    for locus in start_codons:
        protein = translate(sense[locus:])
        if protein != None and protein not in proteins:
            proteins.append(protein)

for protein in proteins:
    print protein

