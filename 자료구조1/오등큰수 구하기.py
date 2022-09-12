from collections import Counter
import sys
a=int(sys.stdin.readline())
result=[-1 for i in range(a)] #오큰수가 없으면 -1 출력해야하기떄문에 미리 -1로 초기화

stack=[0]
b=list(map(int,sys.stdin.readline().split()))
count=Counter(b)

for i in range(1,len(b)):
    while stack and count[b[stack[-1]]]<count[b[i]]: # 만약 stack이 비어있지 않고 stack맨 위보다 b[i]가 작다면 반복
        result[stack.pop()]=b[i] #스택 맨 위에 있는 숫자를 pop하고 그자리에 b[i]를 넣
    stack.append(i)
print(*result) #이렇게하면 공백두고 숫자 출
    
#오등크수구하기다. 단순히 오큰수 구하기에서  count만 while문에 넣었다가 시간초과 당했다.
#Counter을 통해 만약 문자열은 문자별로 카운트해준다.
