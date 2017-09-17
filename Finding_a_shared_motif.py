#Finding a shared motif - brute force algorithm

infile = open('dna.txt', 'r')
list = []
count = -1
for line in infile:
    if line.startswith('>'):
        count += 1
        list.append('')
    else:
        list[count] += (line.rstrip('\n'))

# sort list and define smallest item as ref
list.sort(key=len)
ref = list.pop(0)


# returns true if sequence is common to all items in list
def is_common_substring(sequence, list):
    n = 0
    for item in list:
        if sequence in item:
            n += 1
    if n == len(list):
        return True

n = len(ref)
found = False

while found == False:
    for num in range(len(ref) - n + 1):
        motif = ref[num:num+n]
        if is_common_substring(motif, list):
            found = True
            print 'motif is ' + motif
    n -= 1
    print n
