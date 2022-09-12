import sys
a=list(sys.stdin.readline().rstrip())
result=0
stack=[]
for i in range(len(a)):
    if a[i]=='(':
        stack.append('(')
    else:
        if a[i-1]=='(': #()라면 (를 pop으로 뺴주고 (수만큼 result에 더해준다.
            stack.pop()
            result+=len(stack)
        else:
            stack.pop()
            result+=1 #()가 아니라면 줄의 마지막부분을 더해준다.
print(result)

#첫 구상은 그럴듯 했지만 선이 쪼개졌을떄 끝의 값을 어떻게 해야하나 고민이였다 다른사람의 코드를 참고했는데
#그저 ()가 아닌 ) 이라면 값을 1 더해주면 되는거였다. 조금 더 문제해결능력을 키워야 될것같다.
