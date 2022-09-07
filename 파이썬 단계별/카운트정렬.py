import sys
a=int(input())
num_list=[0]*10001
for i in range(a):
    num_list[int(sys.stdin.readline())]+=1

for j in range(10001):
    if num_list[j]!=0:
        for z in range(num_list[j]):
            print(j)
 #카운트변수는 숫자가 적을때 효율적으로 사용가능하다.
