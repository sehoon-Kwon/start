import sys
a=int(input())
arr=[]
for i in range(a):
    b,c=map(int,sys.stdin.readline().split())
    arr.append((b,c))
arr.sort()
for j in range(a):
    print(arr[j][0],arr[j][1])
    
