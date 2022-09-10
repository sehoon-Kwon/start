import sys
num=int(sys.stdin.readline())
st=[]
for i in range(num):
    com=list(sys.stdin.readline().split())
    if com[0]=='push':
        st.append(com[1])
    elif com[0]=='front':
        if len(st)==0:
            print(-1)
        else:
            print(st[0])
    elif com[0]=='back':
        if len(st)==0:
            print(-1)
        else:
            print(st[-1])
    elif com[0]=='size':
        print(len(st))
    elif com[0]=='empty':
        if len(st)!=0:
            print(0)
        else:
            print(1)
    elif com[0]=='pop':
        if len(st)==0:
            print(-1)
        else:
            print(st.pop(0))


        
#마찬가지로 기능구현이다. push는 정수를 큐에 넣고 pop는 가장 앞에 있는 정수를 뺴고 출력. size는 큐의 정수 개수 empty는 비어있으면 1 출력 아니면 0출력 front는 가장 앞에있는 정수 출력, back는 가장 뒤에 있는 정수 출력
            
