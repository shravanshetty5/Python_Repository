import sys

def quecheck(n,a):
    count = 0
    for i in range(0,n):
        x = a[i] - (i +1)
        print x
        if x >= 3:
            return "Too chaotic"
        elif x >0:
            count = count + x
    return count

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    # your code goes here
    print quecheck(n,q)