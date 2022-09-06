import math
import sys
a=int(input())
b=list(map(int,sys.stdin.readline().split()))
count=a
for i in b:
    if i>1:
        for j in range(2, int(math.sqrt(i))+1):
            if i%j==0:
                count-=1
                break
    else:
        count-=1
print(count)
        
#소수는 제곱근으로 구하는게 시간이 훨씬 절약된다.
#왜? 가운데수를 기준으로 대칭적으로 곱을 통해 만들 수 있기 떄문이다.
#그러므로 제곱근까지만 살펴보면 소수 판별이 가능하다.
#하지만 이것도 숫자가 많아지면 비효율적이다.
#그래서 에라토스테네스의 체 알고리즘을 사용한다.
