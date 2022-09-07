a=int(input())
def findNum(n):
    cnt=0
    num=666
    while True:
        if '666' in str(num): #666이란 문자를 num에서 찾음
            cnt+=1
        if cnt==n: 
            print(num)
            break
        num+=1


findNum(a)
