#mortal_fibunachi

m = 20 # months living for
n = 85 #number of months


x = 0 # juveniles
y = 0 # adults
a = 1 # juveniles from prev. month
b = 0 # adults from prev. month
list = []
# starting gen 2

for i in range(n - 1):
    list.append(a)
    x = b * 1
    y = a + y
    if len(list) >= m:
        y -= list.pop(0)
    b = y
    a = x
    print 'gen:' + str(i + 2) + ' ' + 'juv:' + str(x) + ' ' + 'adu:' + str(y) + ' '

print x + y        