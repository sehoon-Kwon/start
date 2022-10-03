import sys
a=int(input())
num=list(map(int,sys.stdin.readline().split()))
dp=[0 for i in range(a)]
for i in range(a):
    for j in range(i):
        if num[i]>num[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
Mdp=max(dp)
result=[]
for i in range(a-1,-1,-1):
    if dp[i]==Mdp:
        result.append(num[i])
        Mdp-=1
print(len(result))
print(*result[::-1])

"""
앞서 풀었던 가장 긴 증가하는 부분 수열의 확장 문제이다. 앞선 문제는 길이만 출력하는데에 비해 이번 문제는
가장 긴 증가하는 부분 수열의 길이와 그 수열을 출력하는 문제이다. 처음에는 인덱스만 뽑아서 어떻게 차례로 출력해야할지 고민했는데 역순으로 하면 쉽게 풀리는 문제였다.
먼저 1번문제와 동일하게 이전의 숫자들과 비교해서 수열의 숫자마다 수열의 길이를 구해주고 
구한 dp의 max값을 Mdp로 지정하고 뒤에서부터 for문을 돌려준다. 만약 dp[i]가 Mdp와 동일하다면 result에 삽입해주고
Mdp는 -1을 더해서 그 다음 뒤의 값을 비교한다. 그 후에는 수열의 길이와 큰값부터 삽입했기 떄문에 [:-1]을 통해 뒤에서부터 출력해준다
dp는 가면갈수록 어려워지는거같다. 확실하게 배우고 넘어가야겠다.
"""