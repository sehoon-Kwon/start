import sys
a=int(sys.stdin.readline())
for i in range(a):
    b=list(sys.stdin.readline().rstrip())
    for j in range(int(len(b)/2)):
        b.remove('(')
        b.remove(')')
    if len(b)==0:
        print('Yes')
    else:
        print('No')
    
        
    


