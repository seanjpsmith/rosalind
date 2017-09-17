#partial permutations

from math import factorial

def p(n,k):
    # p(n,k) is n!/(n-k)!
    return factorial(n) / factorial(n-k) % 1000000

# test
print p(21,7)
