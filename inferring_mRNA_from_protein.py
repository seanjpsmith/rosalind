# inferring mRNA from protein

dictionary = {'F':2, 'L':6, 'I':3, 'M':1, 'V':4, 'S':4, 'P':4,
              'T':4, 'A':4, 'Y':2, 'Stop':3, 'H':2,'Q':2, 
              'N':2, 'K':2, 'D':2, 'E':2, 'C':2, 'W':1, 'R':6,
              'S':6, 'G':4}

infile = open('dna.txt','r')
dataset = ''
for line in infile.readlines():
    dataset += (line.rstrip('\n'))

# create a list of the number of possible codons of each amino acid
# in dataset
list = []
for i in dataset:
    list.append(dictionary[i])
list.append(dictionary['Stop'])

#print list

# iterate over list, multiplying each element by the last % 1m
count = 1
for i in list:
    count *= i
    if count > 1000000:
        count = count % 1000000

print count
        
