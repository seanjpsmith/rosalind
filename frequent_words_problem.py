# frequent words problem

s = 'AGGACATGAGGACATGAGGACATGGCACATACAATTTTCTCAGGACATGAGGACATGCCTTAACTACCCTTTCTAATTTTCTCACCCTTTCTCCTTAACTAGGACATGCCTTAACTAGGACATGGCACATACCCTTAACTCCTTAACTAGGACATGAATTTTCTCCCTTAACTAATTTTCTCAATTTTCTCACCCTTTCTGCACATACCCTTAACTGCACATACAGGACATGAATTTTCTCCCTTAACTCCTTAACTCCTTAACTAATTTTCTCAGGACATGCCTTAACTAGGACATGAGGACATGAGGACATGAGGACATGCCTTAACTAATTTTCTCAGGACATGAATTTTCTCAATTTTCTCGCACATACGCACATACACCCTTTCTAGGACATGGCACATACGCACATACGCACATACGCACATACAGGACATGGCACATACGCACATACAATTTTCTCGCACATACCCTTAACTGCACATACAGGACATGGCACATACGCACATACACCCTTTCTGCACATACAGGACATGAGGACATGAATTTTCTCCCTTAACTAATTTTCTCAATTTTCTCAGGACATGAATTTTCTCAATTTTCTCAATTTTCTCAGGACATGGCACATACCCTTAACTAGGACATGCCTTAACTAGGACATGCCTTAACTCCTTAACTCCTTAACTGCACATACAATTTTCTCGCACATACAGGACATGAGGACATGCCTTAACTAATTTTCTCAATTTTCTCACCCTTTCTACCCTTTCTAGGACATGAGGACATGAATTTTCTC'
l = 13
kmer = {}
max_value = 0

'''build a dictionary by iterating through the sequence,
where each unique 13mer is the key and the value is the 
number of occurences of that kmer'''

for i in range(len(s)-l+1):
    # creates a string of the total number of kmer possibilities  
    # print s[i:i+4]

    # if kmer does not already exist as key in dictionary
    # create new key with value 1
    if not kmer.has_key(s[i:i+l]):
        kmer[s[i:i+l]] = 1
    
    # else increase the value by 1
    else:
        kmer[s[i:i+l]] = kmer[s[i:i+l]] + 1

# find kmer in dictionary with highest value         
# iterate through all keys in the dictionary to find highest value
for key in kmer:
    if max_value < kmer[key]:
        max_value = kmer[key]
print max_value

# print the key with the highest value
for key in kmer:
    if kmer[key] == max_value:
        print key,