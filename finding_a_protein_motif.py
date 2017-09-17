# finding a protein motif

#import modules
import urllib,urllib2

# define helper functions
def import_fasta_file(ID):
# takes uniprot access ID, returns protein sequence as string
    seq = ''
    url = 'http://www.uniprot.org/uniprot/' + ID + '.fasta'
    params = {
    'format':'tab',
    }

    data = urllib.urlencode(params)
    request = urllib2.Request(url, data)
    contact = "seanjpsmith@gmail.com" # Please set your email address here to help us debug in case of problems.
    request.add_header('User-Agent', 'Python %s' % contact)
    response = urllib2.urlopen(request)

    # process fasta file and return string
    for line in response:
        line = line.rstrip()
        if line.startswith('>'):
            name = line
        else:
            seq += line
    return seq

def Nglycosylation_motif_location(name,seq):
    # take protein sequence and returns locations of N-glycosylation motif
    # N-glycosylation motif is written as N{P}[ST]{P}.
    locations = ''
    for i in range(len(seq)):
        prot = seq[i:i+4]  
        if prot[0] == 'N':
            if prot[1] != 'P':
                if prot[2] == 'S' or prot[2] == 'T':
                    if prot[3] != 'P':
                        locations += str(i+1) + ' '
    if locations != '':
        print name
        print locations

#=====  get the job done =====

infile = open('dna.txt', 'r')
data = infile.readlines()
dataset = []
for line in data:
    dataset.append(line.rstrip('\n'))

for item in dataset:
    
    seq = import_fasta_file(item)
    Nglycosylation_motif_location(item, seq)
