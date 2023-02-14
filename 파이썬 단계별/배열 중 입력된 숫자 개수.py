import sys
num=int(input())
num1=sys.stdin.readline().split()
col=input()
cnt=0
for i in range(num):
    if col==num1[i]:
        cnt+=1
print(cnt)

##간단한 숫자찾기 문제


