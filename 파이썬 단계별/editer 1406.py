import sys
left=list(sys.stdin.readline().rstrip())
right=[]

for _ in range(int(sys.stdin.readline())): # for문중에 _는 값을 무시하거나 변수에 의미를 부여할떄 사용한다.
    com=list(sys.stdin.readline().split())
    if com[0]=='L':
        if left: ##left에 값이 있을때만 하도록 한다. 
            right.append(left.pop())

    elif com[0]=='D':
        if right:
                left.append(right.pop())
    elif com[0]=='B':
        if left:
                left.pop()
    else:
        left.append(com[1])
            
left.extend(reversed(right)) #extend를 통해 right를 뒤집은 문자열과 합쳐준다.
print(''.join(left)) #''.join을 통해 fomat형식을 맞춰준다.
            
    
"""처음에는 insert , remove를 사용했는데 시간초과로 인해 틀렸었다. 알아보니 insert와 remove는 O(N)만큼의 시간을 소요한다고 한다.
그래서 문자열 스택을 2개로 나눠서 값을 추가 삭제한는것으로 커서를 이동하는 기능을 구현하면
append와 pop을 통해 O(1)로 사용가능하다. 마지막에는 right스택을 뒤집어주고 extend로 left와 right함수를 합쳐준다.
여기서 reversd는 왜해줄까? : 커서를 옮기는게 오른쪽 스택으로 저장하면서 스택처럼 마지막에 들어온게 처음 빠지기 떄문에.
예를들어 abc를 c에서부터 커맨드 L을 통해 오른쪽으로 넘기면 스택은 cba로 쌓인다. 그렇다면 마지막에 문자열을 합칠떄는 reversed를 통해 abc로 맞춰줘야한다.
"""
