import sys
a=int(input())
num_list=[0]*10001
for i in range(a):
    num_list[int(sys.stdin.readline())]+=1

for j in range(10001):
    if num_list[j]!=0:
        for z in range(num_list[j]):
            print(j)

    
