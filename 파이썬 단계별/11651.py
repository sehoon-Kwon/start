import sys
a=int(input())
arr=[]
for i in range(a):
    b,c=map(int,sys.stdin.readline().split())
    arr.append((c,b))
arr.sort()
for j in range(a):
    print(arr[j][1],arr[j][0])
    
#꼼수긴하다. 11650은 x좌표를 기준으로 오름차순했다면 이번 문제는 y좌표를 기준으로
#오름차순하는 문제였다. 하지만 단순히 생각해보니 입력을 받을땐 순서를 바꿔서
#받고 sort한 후 출력할때 좌표를 달리 출력하면 단순히 해결할 수 있었다.
