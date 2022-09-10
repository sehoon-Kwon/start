import sys
a=int(input())
st=[]
for i in range(a):
    com=list(sys.stdin.readline().split())
    if com[0]=='push_front':
        st.insert(0,com[1])
    elif com[0]=='push_back':
        st.append(com[1])
    elif com[0]=='pop_front':
        if len(st)!=0:
            print(st.pop(0))
        else:
            print(-1)
    elif com[0]=='pop_back':
        if len(st)!=0:
            print(st.pop())
        else:
            print(-1)
    elif com[0]=='size':
        print(len(st))
    elif com[0]=='empty':
        if len(st)==0:
            print(1)
        else:
            print(0)
    elif com[0]=='front':
        if len(st)!=0:
            print(st[0])
        else:
            print(-1)
    elif com[0]=='back':
        if len(st)!=0:
            print(st[-1])
        else:
            print(-1)
        
"""insert(0,요소)로 리스트 맨 앞에 추가할 수 있다. 하지만 찾아보면서 deque()를 통해 리스트 맨 앞과 뒤에 추가 삭제가 간편하고 응답시간 또한 짧다고한다.
다음 유형에 적용해서 응답시간을 비교해봐야겠다.
            
