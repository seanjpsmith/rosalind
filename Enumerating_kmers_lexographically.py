#Enumerating kmers lexographically

import itertools

for elem in itertools.product('LNMK', repeat=4):
    print ''.join(elem)