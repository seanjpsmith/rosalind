#frequent_words_with_mismatches

s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'

# size of kmer
k = 4
# number of mismatches allowed
d = 1

#define functions
def check_alignment(seq, pattern):
    #function checking alignment
    alignment_score = 0
    for i in range(len(pattern)):
        if seq[i] == pattern[i]:
            alignment_score += 1
    return alignment_score

# build a dictionary of all k-mers in string
kmer = {}
for i in range(len(s)-k+1):
    if not kmer.has_key(s[i:i+k]):
        kmer[s[i:i+k]] = 1
    
    # else increase the value by 1
    else:
        kmer[s[i:i+k]] = kmer[s[i:i+k]] + 1

# for each (unique) entry in dictionary
# check for appearance of that kmer in string
# with d mismatches

answer = {}

for key in kmer:
    for i in range(len(s) - k + 1):
        seq = s[i:i+k]
        score = check_alignment(seq,key)
        if score >= k - d:
            if key not in answer:
                answer[key] = 1
            else:
                answer[key] += 1
list = []               
max_number = 0
for key in answer:
    if answer[key] > max_number:
        max_number = answer[key]

for key in answer:
    if answer[key] == max_number:
        list.append(key)

print list        


        