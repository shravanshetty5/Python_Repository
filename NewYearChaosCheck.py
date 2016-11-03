import sys

def NewyearChaosCheck(n,a):
    for i, x in enumerate(a):
        if x - (i +1) > 2:
            return "Too chaotic"
    swap = False
    count = 0
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swap = True
                count +=1
        if swap:
            swap = False
        else:
            break
    return count


if __name__ == "__main__":
    T = int(raw_input().strip())
    for a0 in xrange(T):
        n = int(raw_input().strip())
        q = map(int,raw_input().strip().split(' '))
        # your code goes here
        print NewyearChaosCheck(n,q)