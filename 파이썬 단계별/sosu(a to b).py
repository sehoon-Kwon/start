#a부터 2a까지의 소수의 개수
import math,sys

def isPrime(n):
	if n==1:
		return False
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
			break
	else:
		return True
		
n=int(input())
#주어진 범위 안에서 소수들을 먼저 저장
prime=[i for i in range(1,10000+1) if isPrime(i)]
b=[]
c=[]
for z in range(n):
        num=int(input())

        a,b=num//2, num//2
        while a>0:
                if isPrime(a) and isPrime(b):
                        print(a,b)
                        break
                else:
                        a-=1
                        b+=1
