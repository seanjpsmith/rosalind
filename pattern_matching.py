#pattern_matching

infile = open('dna.txt','r')
string = infile.read()

pattern = 'GTCAATGT'
answer = ''

for i in range(len(string) - len(pattern) + 1 ):
    if string[i:i + len(pattern)] == pattern:
        answer = answer + ' ' + str(i)
 
print answer
