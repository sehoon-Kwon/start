import sys,math
num,me=sys.stdin.readline().split()
num=int(num)
me=int(me)
Dvalue=[]
anum=list(map(int,sys.stdin.readline().split()))
for i in anum:
    Dvalue.append(abs(me-i))

ans=Dvalue[0]
for i in range(1,num):
    ans=math.gcd(Dvalue[i],ans)

print(ans)
        

"""
첫째줄에 anum의 숫자와 기준점을 준다.
기준점에서 anum간의 거리의 최대공약수를 구하는 문제이다.
그래서 me와 anum을 뺀 절대값을 Dvalue에 append시키고
Dvalue의 값을 비교해서 최대공약수를 구하도록 구성했다.
"""
