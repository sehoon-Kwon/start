import sys
a=int(sys.stdin.readline())
def stack(n):
    cnt=0
    num=[1]
    cnt=2
    result=[]
    for i in range(a):
        b=int(sys.stdin.readline())
        while True:
            if cnt==2:
                    result.append('+')
                
            if num[-1]==b:
                if len(num)==1:
                    result.append('-')
                    break
                elif b<cnt:
                    
                    result.append('-')
                    
                    del num[-1]
                    break
                else:
                    result.append('+')
                    del num[-1]
                    break
                
            if b in num:
                if num[-1]!=b:
                    num[0]=0
                    break
  
            else:  
                
                num.append(cnt)
                result.append('+')
                cnt+=1
    
    

    if num[0]==0:
        print('NO')
    elif b!=1:
        print('NO')
    
    
    else:
        for i in result:
            print(i)


stack(a)
