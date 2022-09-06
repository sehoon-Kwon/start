import sys
a=int(input())

def d(n):
    b=9999999 # 1~1,000,000까지
    if n<=18: #한자리 수들은 자기자신*2면 분해합이므로 18까지는 c를 //2로 설정
        c=n//2
    else:
        c=len(str(n))*9 #나머지는 자릿수*9 차만 계산
    
        
    
    for i in range(n-c,n+1):              
        d=i+sum(list(map(int,str(i)))) # n에서 자릿수*9를 뺀것부터 자리수 합이 n과 같고 min으로 설정한 b보다 작으면 b에 i설정
        if d==n and d<b:
            b=i
    if(b==9999999): # 만약 b i로 지정되지않고 빠져나왔으면 b=0으로 설정
        b=0
    print(b)
d(a)
