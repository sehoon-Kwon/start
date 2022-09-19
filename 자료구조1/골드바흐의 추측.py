import sys
import math
n=1000000
a = [False,False] + [True]*(n+1)
for i in range(2,int(math.sqrt(n))+1):
    if a[i]:
        for j in range(2*i, n, i):
            a[j] = False
                

while True:
    num=int(input())
    if num==0:
        break
    for i in range(3,num//2+1):
        if a[i]==True and a[num-i]==True:
            print("%d = %d + %d"%(num, i, num-i))
            break
            
    else:
        print("Goldbach's conjecture is wrong.")
               
  
            
"""4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다는 골드바흐의 추측을 기반으로
입력된 짝수가 두 홀수 소수의 합으로 나타내는데 b-a가 가장 큰 숫자를 출력한다.
먼저 최대 1000000까지의 숫자가 출력된다고 하니 소수 리스트를 에라토스테네스의 체로 만들어주고
만약 a[i]와 num-a[i] 둘다 소수라면 바로 print해준다 왜? 3부터 검색했기떄문에 b-a가 가장 클 수 밖에 없다.
"""
