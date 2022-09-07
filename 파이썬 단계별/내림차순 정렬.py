import sys
a,b=map(int,sys.stdin.readline().split())
c=list(map(int,sys.stdin.readline().split()))
d=sorted(c,reverse=True)
print(d[b-1])
