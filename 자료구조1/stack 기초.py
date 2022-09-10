import sys
a=int(sys.stdin.readline())
stack=[]
for i in range(a):
    manual=sys.stdin.readline().split()
    if manual[0]=='push':
        stack.append(manual[1])
    elif manual[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop()) #pop(x)는 리스트의 x번쨰 요소를 출력하고 요소는 삭제한다. 그냥 pop()는 가장 위에 있는 정수를 뺸다.
    elif manual[0]=='size':
        print(len(stack))
    elif manual[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif manual[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
