import math
a= int(input())
b= int(input())
num=[]
for i in range(a,b+1):
    c=0
    if i<2:
        continue
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0 :
            c=1
    if c==0:
        num.append(i)
if sum(num)==0:
    print(-1)
else:
    print(sum(num))
    print(min(num))

#a부터 b까지 소수의 합과 가장 작은 소수를 구하는 방법.
