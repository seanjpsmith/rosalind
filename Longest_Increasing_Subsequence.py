#===Rosalind Longest Increasing Subsequence===

#Given: A positive integer n≤10000 n≤10000 followed by a 
#permutation ππ of length nn.

#Return: A longest increasing subsequence of ππ, followed 
#by a longest decreasing subsequence of ππ.

''' 
Sample dataset
5
5 1 4 2 3

Sample output
1 2 3
5 4 2 '''


input = '5 1 4 2 3'

# create a string of the input permutation called permutation
permutation = []
input = input.replace(" ","")
for i in input:  
    permutation.append(int(i))

memory = []
answer = []

memory.append(1)


''' When trying to find the optimal permutation, you should search 
for the ideal combination, i.e. if the first number is 1, the next
should be 2, only if this isn't possible should the algorithm accept
3.'''




for i in range(len(permutation)):
    
    # add the first value
    memory.append(permutation[i])
    
    # create a running total
    position_on_permutation = i + 1
    
    # create a loop, while we're still on the permutation string
    while position_on_permutation < len(permutation):
        if permutation[position_on_permutation] > memory[-1]:
            memory.append(permutation[position_on_permutation])
        position_on_permutation += 1
    if len(memory) > len(answer):
        answer = memory
    memory = []

print(answer)