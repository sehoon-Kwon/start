import sys
a,b=map(int,input().split())
filist=[]
selist=[]
num=b-1
for i in range(1,a+1):
    filist.append(i)
for i in range(a):
    if len(filist)>num:
        selist.append(filist.pop(num))
        num+=b-1
    elif len(filist)<=num:
        num=num%len(filist)
        selist.append(filist.pop(num))
        num+=b-1
print("<",', '.join(str(i) for i in selist), ">",sep= '')



"""설계의 중요성을 깨달았다. 처음 문제를 직면했을떄는 고민이 많았다. 숫자를 뺄수록 배열의 값을 조절해야하고
만약 배열의 길이가 num보다 커지면 다른 조건을 걸어야 했다. 처음부터 숫자의 반복성과 설계를 제대로 했다면
문제를 더 쉽게 풀 수 있었을 것이다.
