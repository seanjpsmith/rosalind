# computing GC content Rosalind

f = open('dna.txt','r')
data = {}
gc = {}
string = ''
list = []

for line in f:
    # build a dictionary using the fasta title as key and sequence as value
    if line.startswith('>'):
        string = line.rstrip('\n')
        data[string] = ''
    else:
        data[string] = data[string] + line.rstrip('\n')
   
for item in data:
    # create a second dictionary with the gc content as the value
    string = data[item]
    gc[item] = 100 * float(string.count('G') + string.count('C')) / (len(string))

# print key and value of maximum value in dictionary
print max(gc, key = gc.get)
print gc[max(gc, key = gc.get)]
