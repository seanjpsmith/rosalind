# mismatches

sequence = ''
pattern = ''

#number of mismatches allowed
mismatches = 


def check_alignment(seq, pattern):
    #function checking alignment
    alignment_score = 0
    for i in range(len(pattern)):
        if seq[i] == pattern[i]:
            alignment_score += 1
    return alignment_score
    
# test print check_alignment(sequence,pattern)

position = []

for i in range(len(sequence) - len(pattern) + 1):
    seq = sequence[i:i+len(pattern)]
    score = check_alignment(seq,pattern)
    if score >= len(pattern) - mismatches:
        position.append(str(i))

print (','.join(position)).replace(',',' ')
        
        