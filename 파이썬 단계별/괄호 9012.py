import sys
a=int(sys.stdin.readline())
for i in range(a):
    b=list(sys.stdin.readline().rstrip())
    sum=0
    for j in b:
        if j=='(':
            sum+=1
        elif j==')':
            sum-=1
        if sum<0:
            print('NO')
            break
    if sum==0:
        
        print('YES')
    elif sum>0:
        print('NO')
#처음에는 for문을 통해 순서대로 ( 다음 ) 가 나오면 두개를 지우고 다시 탐색해 마지막에 len(b)가 0이 아니면 No를 하는거였는데 del로 지우면 번호가 밀려서 
#내가 생각했던데로 돌아가지 않았다. 배열 문제에 대해서 조금 더 공부해봐야겠다.
        
