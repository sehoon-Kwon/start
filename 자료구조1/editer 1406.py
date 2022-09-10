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


        
    
