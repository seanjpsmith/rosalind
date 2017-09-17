#Enumerating Oriented Gene Orderings

import itertools
list = []

for item in itertools.permutations('123456', 6):
    list.append(str(item))

print len(list)
for item in list:
    print item.translate(None, "'(),")