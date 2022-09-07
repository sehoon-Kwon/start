import sys
while True:
    n=int(input())
    t=n*2
    if n==0:
        break
    a = [False,False] + [True]*(t-1)
    primes=[]
    for i in range(2,t+1):
        if a[i]:
            if i>=n:
                primes.append(i)
            for j in range(2*i, t+1, i):
                a[j] = False
    print(len(primes))
