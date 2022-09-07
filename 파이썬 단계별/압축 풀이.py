import sys
a=int(input())
b=list(map(int,sys.stdin.readline().split()))
num=[]

num=list(sorted(set(b)))
dic={num[i]:i for i in range(len(num))} #{dick[요소]:요소의 index}의 형태로 저장해 줌
for i in b:
       print(dic[i],end=' ')


#list.index(i)는 시간복잡도 O(N)을 가지고 index[i]형태는 시간복잡도 O(1)을 가진다.

