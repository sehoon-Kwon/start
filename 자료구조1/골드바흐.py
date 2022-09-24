import sys
import math
cnt=int(sys.stdin.readline())
n=1000000
a = [False,False] + [True]*(n+1)
for i in range(2,int(math.sqrt(n))+1):
    if a[i]:
        for j in range(2*i, n, i):
            a[j] = False

for i in range(cnt):
    count=0
    num=int(sys.stdin.readline())
    for j in range(2,num//2+1):
        if num==0:
                print(0)
        else:
            if a[j]==True and a[num-j]==True:
                    count+=1
    print(count)
