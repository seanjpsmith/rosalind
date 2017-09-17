#counter

k = 4

counter = []
for i in range(k):
    counter.append(0)

print counter

while counter[0] <= 4:
    counter[-1] += 1
    n = -1
    print counter
    while n >= -3:
        if counter[n] == 4:
            counter[n] = 0
            counter[n-1] += 1
        n = n - 1
